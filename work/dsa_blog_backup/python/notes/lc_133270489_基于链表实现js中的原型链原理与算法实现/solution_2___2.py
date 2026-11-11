# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class Proto:  # 定义类
    """模拟 JS 对象：属性查找沿原型链向上进行。"""

    def __init__(self, name, parent=None):  # 构造函数：初始化成员
        self.name = name  # 把 name 写入 self.name
        self.props = {}  # 把 {} 写入 self.props
        self.proto = parent  # 把 parent 写入 self.proto

    def set(self, key, value):  # 定义函数 set（参数：self, key, value）
        self.props[key] = value  # 把 value 写入 self.props[key]

    def get(self, key):  # 定义函数 get（参数：self, key）
        cur = self  # 把 self 存入 当前值
        while cur is not None:  # 循环，直到不满足「当前值 is not None」
            if key in cur.props:  # 若 key in 当前值.props
                return cur.props[key]  # 返回 当前值.props[key]
            cur = cur.proto  # 把 当前值.proto 存入 当前值
        return None  # 对应 JS 的 undefined


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    object_proto = Proto("Object.prototype")  # 把 Proto(「Object.prototype」) 存入 object_proto
    object_proto.set("x", "x")  # object_proto.set(「x」, 「x」)
    function_proto = Proto("Function.prototype", object_proto)
    function_proto.set("y", "y")  # function_proto.set(「y」, 「y」)
    array_proto = Proto(
        "Array.prototype", object_proto
    )  # 把 Proto(「Array.prototype」, object_proto) 存入 array_proto
    array_proto.set("z", "z")  # array_proto.set(「z」, 「z」)

    obj = Proto("obj", object_proto)  # 把 Proto(「obj」, object_proto) 存入 obj
    func = Proto("func", function_proto)  # 把 Proto(「func」, function_proto) 存入 func
    arr = Proto("arr", array_proto)  # 把 Proto(「数组」, array_proto) 存入 数组

    print(obj.get("x"))  # x
    print(func.get("y"))  # y
    print(arr.get("z"))  # z
