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
        return None  # undefined


def instance_of(obj, prototype):  # 定义函数 instance_of（参数：obj, prototype）
    """沿 __proto__ 链查找是否命中 B.prototype（算法实现，方案 4）。"""
    p = obj  # 把 obj 存入 节点
    while p is not None:  # 循环，直到不满足「节点 is not None」
        if p is prototype:  # 若 节点 is prototype
            return True  # 返回 True
        p = p.proto  # 把 节点.proto 存入 节点
    return False  # 返回 False


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    object_proto = Proto("Object.prototype")  # 把 Proto(「Object.prototype」) 存入 object_proto
    object_proto.set("a", "aaa")  # object_proto.set(「数组」, 「数组」)
    function_proto = Proto("Function.prototype", object_proto)
    function_proto.set("b", "bbb")  # function_proto.set(「b」, 「b」)

    obj = Proto("obj", object_proto)  # 把 Proto(「obj」, object_proto) 存入 obj
    func = Proto("func", function_proto)  # 把 Proto(「func」, function_proto) 存入 func

    # 同类型查找
    print(obj.get("a"))  # aaa
    # 不同类型交叉验证
    print(obj.get("b"))  # None (undefined)
    print(func.get("a"))  # aaa
    print(func.get("b"))  # bbb
    print("func instanceof Object:", instance_of(func, object_proto))  # True
