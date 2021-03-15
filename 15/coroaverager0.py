"""计算移动平均值的协程
协程的作用更像一个生成器，
但是对于协程，调用方可以通过send函数向协程中发送值
"""
from functools import wraps
def coroutine(func):
    """协程预激活装饰器"""
    def primer(*args,**kwargs):
        gen = func(*args,**kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

from inspect import getgeneratorstate
core_avg = averager()

# 激活协程
next(core_avg)
print(core_avg.send(10))
print(core_avg.send(20))
# del core_avg
core_avg.close()
print(getgeneratorstate(core_avg))

