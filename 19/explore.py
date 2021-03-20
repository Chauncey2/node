from collections import abc
import keyword


class FrozenJson:
    """一个只读接口，使用属性表示法访问Json类对象
    """

    # def __init__(self, mapping):
    #     self.__data = dict(mapping)

    def __new__(cls, args):
        """真实的构造方法"""
        if isinstance(args, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(args, abc.MutableSequence):
            return [cls(item) for item in args]
        else:
            return args

    def __init__(self, mapping):
        """实现方法采用如下所示
            避免擦混入的属性值中含有python内置的关键字，
        """
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            # return FrozenJson.build(self.__data[name])
            return FrozenJson(self.__data[name])

    #  # 实现了__new__特殊方法，这个备选构造方法就不再需要了
    # @classmethod
    # def build(cls, obj):
    #     """
    #     备选构造方法
    #     """
    #     if isinstance(obj, abc.Mapping):
    #         return cls(obj)
    #     elif isinstance(obj, abc.MutableSequence):
    #         return [cls.build(item for item in obj)]
    #     else:
    #         return obj


if __name__ == '__main__':
    grad = FrozenJson({'name': 'aaa', 'class': 1995})
    print(grad.class_)
