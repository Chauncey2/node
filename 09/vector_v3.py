# -*- encoding:utf8 -*-
from array import array
import reprlib
import math
import numbers
import operator
import functools



class Vector:
    typecode = "b"
    shortcut_names ="xyzt"

    def __init__(self,components):
        self._components = array(self.typecode,components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes(ord(self.typecode))+
                bytes(self._components))

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    # __getitem__ 协议，使得 Vector类可以变成可迭代对象，然后Vector类就成了序列
    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index,slice):
            return cls(self._components[index])
        elif isinstance(index,numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integer'
            raise TypeError(msg.format(cls=cls))

    # 当实现了getattr和setattr，就可以使用. 调用和设置属性值
    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))  # raise 语句可以捕获异常

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    @classmethod
    def frombytes(cls, octets):
        """备选构造方法，用classmethod装饰器定义
        """
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        # 拆包转换后的memoryview,得到构造对象的一对参数
        return cls(*memv)

    def __eq__(self, other):
        # return tuple(self) == tuple(other)
        if len(self) != len(other): return False
        for a,b in zip(self,other):
            if a != b: return False
        return True

    def __hash__(self):
        # hashs = map(hash,self._components)
        hashs = (hash(x) for x in self._components)
        # operator.xor函数做的是一种异或操作
        return functools.reduce(operator.xor,hashs,0)


if __name__ == '__main__':
    v1 = Vector([1,2,3])
    print(v1[0])
    for item in v1:
        print(item)
    print(v1[1:4])
    print(v1.x)
    v1.x = 0
    # print(v1.x)