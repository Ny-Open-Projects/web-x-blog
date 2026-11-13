# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def get_value_eval(data, path):  # 定义函数 get_value_eval（参数：data, 当前路径）
    # 通过链表指针(动态属性)访问指定节点值，等价于 JS 的 eval(path.join('.'))
    expr = "data" + "".join("[{}]".format(repr(k)) for k in path)
    return eval(expr, {"data": data})  # 返回 eval(expr, {'data': data})


if __name__ == "__main__":  # 若 __name__ 等于 「__main__」
    data = {"a": {"b": {"c": 1}}, "d": {"e": 2}}  # 把 {'数组': {'b': {'字符': 1}}, 'd': {'e': 2}} 存入 data
    path = ["a", "b", "c"]  # 把 ['数组', 'b', '字符'] 存入 当前路径
    print(get_value_eval(data, path))  # 打印输出
