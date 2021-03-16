from collections import namedtuple

Result = namedtuple('Result', 'count average')


# 子生成器
def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
        return Result(count, average)


# 委派生成器
def grouper(results, key):
    while True:
        results[key] = yield from average()


# 客户端代码，即调用方
def main(data):
    results = {}
    for key, value in data.items():
        group = grouper(results, key)
        print()
