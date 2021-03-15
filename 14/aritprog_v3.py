# 该库中有很多生成器，在python中，生成器有很多作用
import itertools


def aritprog_gen(begin, step, end=None):
    first = type(begin + step)(begin) # 强转类型
    print("first:{}".format(first))
    ap_gen = itertools.count(first, step)
    if end is not None:
        # ap_gen 本事是一个无上限的生成器，但是使用了talkwhile之后，就编程了一个有限的生成器
        # iterator.takewhile(Bool,gen_fun)
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen



if __name__ == '__main__':
     flag = aritprog_gen(1,2,10) # 迭代器
     print(next(flag))
     print(next(flag))
     print(next(flag))
     itertools.chain