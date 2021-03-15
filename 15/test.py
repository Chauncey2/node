# for/else

# while/else

# try/else

import inspect

def simple_coroutine():
    """
    展示了协程的应用
    """
    print("1")
    x = yield
    print(type(x))
    print("2:{}".format(x))

# func = simple_coroutine()
# print(inspect.getgeneratorstate(func))  # GEN_CREATED ===>等待开始
# print(next(func)) # 此时的yield返回的是None
# # 此时的yield返回的是None
# print(inspect.getgeneratorstate(func))  # GEN_SUSPENDED ===> 在yield表达式处暂停
# # send 方法的参数会成为yield的值.send(22) ==> yield 22
# func.send([11,22,44])  # 此时的yield语句返回类型是 <class 'int'>

def simple_core2(a):
    print('-> Started:a = ',a)
    b = yield a
    print('received:{}'.format(b))
    c = a+b
    print("c is {}".format(c))
core = simple_core2(13)
from inspect import getgeneratorstate
print(getgeneratorstate(core))