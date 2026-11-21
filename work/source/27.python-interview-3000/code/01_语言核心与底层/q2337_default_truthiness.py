"""真值判定的默认规则:不定义 __bool__ 与 __len__ 的对象恒为真。"""
import io


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y


class EmptyBox:
    """什么协议都没定义:内部再空也恒为真。"""


class Box:
    """定义 __len__ 后,空箱为假。"""

    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)


if __name__ == "__main__":
    print("Point(0,0) 真值:", bool(Point(0, 0)))     # True:默认规则
    print("EmptyBox() 真值:", bool(EmptyBox()))      # True

    box = Box()
    print("空 Box 真值:", bool(box))                 # False
    box.items.append("x")
    print("装东西后真值:", bool(box))                # True

    empty_file = io.StringIO("")
    print("空文件对象恒真:", bool(empty_file))        # True
    print("但读出的内容为假:", bool(empty_file.read()))

    print("or 短路返回操作数本身:", Point(0, 0) or "默认点")
