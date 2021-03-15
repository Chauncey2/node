import contextlib


class LookingGlass:
    """
    自定义的上下文管理器类
    必须实现__enter__ 和 __exit__ ==> 上下文管理器
    """

    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write # 猴子补丁
        return 'JABBERWOCKY'

    def reverse_write(self,text):
        """

        """
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        # write 是IO类的抽象方法
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True

 
if __name__ == '__main__':
    manager = LookingGlass()
    print(manager)
    monster = manager.__enter__()
    print(monster == 'JABBERWOCKY')
    print(monster)
