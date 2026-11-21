class Positive:
    """data descriptor:校验数值"""
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.name} must be positive")
        obj.__dict__[self.name] = value

class Order:
    price = Positive()
    qty = Positive()
    def __init__(self, price, qty):
        self.price = price
        self.qty = qty

if __name__ == "__main__":
    o = Order(10, 2)
    print(o.price * o.qty)
    try:
        o.qty = -1
    except ValueError as e:
        print("rejected:", e)
    print(Order.price)  # 类上访问返回描述符自身
