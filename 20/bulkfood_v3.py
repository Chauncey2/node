class Quantity:
    """描述符类"""

    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        """
        参数中，
        self是描述符实例
        instance 是托管实例
        """
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value must be > 0')


class LineItem:
    """托管类"""

    # 存储属性  描述符实例
    weight = Quantity('weight')
    # 存储属性  描述符实例
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    # 托管实例
    one = LineItem('one', 10, 2.5)
