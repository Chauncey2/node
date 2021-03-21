"""使用特性验证属性"""


class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        """this is help doc"""
        return self.weight * self.price

    @property
    def weight(self):

        return self.__dict__['weight']

    @weight.setter
    def weight(self, value):
        if value > 0:
            # self.__weight = value
            self.__weight = value
            # self.__dict__['weight'] = value
        else:
            raise ValueError('value must be > 0')

    @weight.getter
    def weight(self):
        """this is help doc for weight attr"""
        return self.__weight * 10


if __name__ == '__main__':
    raisins = LineItem('Golden raisins', 10, 6.95)
    print(raisins.subtotal())  # 输出 69.5
    # raisins.weight = -10       # ValueError: value must be > 0
    print(raisins.subtotal())
    print(raisins.weight)
    help(LineItem)
