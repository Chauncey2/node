# -*- encoding:utf8 -*-
import os
import sys
from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        # hypot返回欧几里得平方根(点到原点的距离)
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, format_spec):
        """
        先使用内置的format函数进行格式化，然后再使用
        str.format()方法返回结果
        """
        if format_spec.endswith('p'):
            # 极坐标
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{},{}>'
        else:
            # 直角坐标
            coords = self
            outer_fmt = "({},{})"
        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*components)

    def __hash__(self):
        return hash(self.__x) ^ hash(self.__y)

    def angle(self):
        return math.atan2(self.y, self.x)

    @classmethod
    def frombytes(cls, octets):
        """备选构造方法，用classmethod装饰器定义
        """
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        # 拆包转换后的memoryview,得到构造对象的一对参数
        return cls(*memv)


if __name__ == '__main__':

    v1 = Vector2d(1, 2)
    v2 = Vector2d(3, 4)
    print(hash(v1))
    print(hash(v2))
    v1.typecode = "f"  # 实例可以覆盖类属性的默认值
    print(v1.typecode)
    print(Vector2d.typecode)
