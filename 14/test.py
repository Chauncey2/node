def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

def chain2(*iterable):
    for i in iterable:
        yield from i




if __name__ == '__main__':
    # s = "ABC"
    # t = tuple(range(3))
    # print(list(chain(s,t)))
    # print(list(chain2(s,t)))  # yield from 语句
    #
    # l = [1,2,3,4,5,6,7,8,9]
    # from functools import reduce
    # # reduce 的第一个参数（函数参数）必须是能够接收两个值的参数，一般用lambda函数表示
    # number_all = reduce(lambda x, y: x+y,l)
    # print(number_all)
    from random import randint


    def d():
        return randint(1, 6)

    sub_d_iterator = iter(d,1)
    # 当遇到“哨符” 1的时候， 
    for item in sub_d_iterator:
        print(item)
    pass