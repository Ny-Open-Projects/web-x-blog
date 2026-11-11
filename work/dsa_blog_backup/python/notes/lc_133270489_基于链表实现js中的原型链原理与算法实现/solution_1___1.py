# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class Proto:  # 定义类
    """模拟 JS 对象：拥有自己的属性 dict 与指向父原型的 __proto__。"""

    def __init__(self, name, parent=None):  # 构造函数：初始化成员
        self.name = name  # 把 name 写入 self.name
        self.props = {}  # 把 {} 写入 self.props
        self.proto = parent  # 把 parent 写入 self.proto

    def set(self, key, value):  # 定义函数 set（参数：self, key, value）
        self.props[key] = value  # 把 value 写入 self.props[key]


def instance_of(obj, prototype):  # 定义函数 instance_of（参数：obj, prototype）
    """模拟 JS 的 instanceof：沿 __proto__ 链寻找是否命中 B.prototype。"""
    p = obj  # 把 obj 存入 节点
    while p is not None:  # 循环，直到不满足「节点 is not None」
        if p is prototype:  # 若 节点 is prototype
            return True  # 返回 True
        p = p.proto  # 把 节点.proto 存入 节点
    return False  # 返回 False


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # 构造原型链：Object.prototype <- (null)
    object_proto = Proto("Object.prototype", None)  # 把 Proto(「Object.prototype」, None) 存入 object_proto
    function_proto = Proto("Function.prototype", object_proto)
    array_proto = Proto(
        "Array.prototype", object_proto
    )  # 把 Proto(「Array.prototype」, object_proto) 存入 array_proto

    obj = Proto("obj", object_proto)  # 把 Proto(「obj」, object_proto) 存入 obj
    func = Proto("func", function_proto)  # 把 Proto(「func」, function_proto) 存入 func
    arr = Proto("arr", array_proto)  # 把 Proto(「数组」, array_proto) 存入 数组

    print(instance_of(obj, object_proto))  # True
    print(instance_of(func, function_proto))  # True
    print(instance_of(func, object_proto))  # True
    print(instance_of(arr, array_proto))  # True
    print(instance_of(arr, object_proto))  # True
