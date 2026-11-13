# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import functools  # 引入依赖


def get_value_chain(data, path):  # 定义函数 get_value_chain（参数：data, 当前路径）
    # 使用 reduce 沿着链表指针链依次取值，等价 JS 的 new Function 方式
    return functools.reduce(
        lambda d, k: d[k], path, data
    )  # 返回 functools.reduce(lambda d, 下标 k: d[下标 k], 当前路径, data)


if __name__ == "__main__":  # 若 __name__ 等于 「__main__」
    data = {"a": {"b": {"c": 1}}, "d": {"e": 2}}  # 把 {'数组': {'b': {'字符': 1}}, 'd': {'e': 2}} 存入 data
    path = ["a", "b", "c"]  # 把 ['数组', 'b', '字符'] 存入 当前路径
    print(get_value_chain(data, path))  # 打印输出
