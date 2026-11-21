class Typed:
    """数据描述符:带类型校验的属性"""
    def __init__(self, expected):
        self.expected = expected
        self.name = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self                      # 类访问返回描述符自身
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if not isinstance(value, self.expected):
            raise TypeError(f"{self.name} expects {self.expected.__name__}")
        obj.__dict__[self.name] = value

class Order:
    qty = Typed(int)
    price = Typed(float)

    def __init__(self, qty, price):
        self.qty = qty
        self.price = price

if __name__ == "__main__":
    o = Order(3, 9.9)
    print(o.qty, o.price)
    o.qty = 5
    print("updated:", o.qty)
    try:
        o.price = "cheap"
    except TypeError as e:
        print("rejected:", e)
    print("class access returns descriptor:", type(Order.qty).__name__)
