def quantity(storage_name):
    """特性工厂函数"""

    def qty_getter(instance):
        """this is help doc"""
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)


class LineItem:
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    raisins = LineItem('Golden raisins', 10, 6.95)
    print(raisins.subtotal())  # 输出 69.5
    # raisins.weight = -10       # ValueError: value must be > 0
    print(raisins.subtotal())
    print(raisins.weight)
    help(LineItem)
