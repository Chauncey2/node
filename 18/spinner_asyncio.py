"""
通过线程以动画形式现实文本式旋转  (asyncio实现)
"""
import asyncio

import time
import sys
import itertools


class Signal:
    go = True


@asyncio.coroutine
async def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + '  ' + msg
        write(status)
        flush()
        # \x08 是退格符
        write('\x08' * len(status))
        try:
            # yield from asyncio.sleep(.1)  | version < python3.6
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
        # time.sleep(.1)
        # if not signal.go:
        #     break
    write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_function():
    """模拟等待IO一段时间"""
    yield from asyncio.sleep(.1)
    # time.sleep(1)
    return 42


@asyncio.coroutine
def supervisor():
    # python 3.6 一下版本中的代码实现是 spinner = asyncio.async(spin('thinking')) 创建一个task
    # 而以上的版本，直接可以将async 定义到def之前，将函数直接定义为协程
    spinner = spin('thinking!')

    print('spinner object:',spinner)
    result = yield from slow_function()
    # spinner.cancel()
    return result

    # signal = Signal()
    # spinner = threading.Thread(target=spin, args=('thinking!', signal))
    # print('spinner object:', spinner)
    # spinner.start()
    # result = slow_function()
    # spinner.go = False
    # spinner.join()
    # return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    # result = supervisor()
    # print("Answer:", result)


if __name__ == '__main__':
    main()
