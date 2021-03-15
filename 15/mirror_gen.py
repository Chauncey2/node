import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    originak_write = sys.stdout.write  # 打 猴子补丁

    def reverse_write(text):
        originak_write(text[::-1])

    sys.stdout.write = reverse_write
    # yield 'JABBERWOCKY'
    # # 跳出with 语句块，恢复原来的 sys.stdoiut.write 方法
    # sys.stdout.write = originak_write
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = originak_write
        if msg:
            print(msg)


if __name__ == '__main__':
    print(type(looking_glass))

    with looking_glass() as what:
        print("12345")
        print(what)
    print(what)