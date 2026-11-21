"""classmethod 多态构造器:from_xxx 与 cls 的多态传递。"""
import json


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f):
        return cls((f - 32) * 5 / 9)      # cls 是实际调用的类,不是硬编码

    @classmethod
    def from_json(cls, payload):
        data = json.loads(payload)
        return cls(data["celsius"])

    def __repr__(self):
        return "{}({:.1f}C)".format(type(self).__name__, self.celsius)


class Kelvin(Temperature):
    def __init__(self, celsius):
        super().__init__(celsius)
        self.kelvin = celsius + 273.15


if __name__ == "__main__":
    print(Temperature.from_fahrenheit(100))
    print(Kelvin.from_fahrenheit(100))    # 子类上调用,cls 是 Kelvin:多态构造
    print(Kelvin.from_json('{"celsius": 25}'))
