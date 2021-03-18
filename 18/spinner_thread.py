"""
通过线程以动画形式现实文本式旋转
"""
import threading
import itertools
import time
import sys


class Signal:
    go = True


def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + '  ' + msg
        write(status)
        flush()
        # \x08 是退格符
        write('\x08' * len(status))
        time.sleep(.1)
        if not signal.go:
            break
    write(' ' * len(status) + '\x08' * len(status))


def slow_function():
    """模拟等待IO一段时间"""
    time.sleep(1)
    return 42


def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking!', signal))
    print('spinner object:', spinner)
    spinner.start()
    result = slow_function()
    spinner.go = False
    spinner.join()
    return result


def main():
    result = supervisor()
    print("Answer:", result)


if __name__ == '__main__':
    main()
