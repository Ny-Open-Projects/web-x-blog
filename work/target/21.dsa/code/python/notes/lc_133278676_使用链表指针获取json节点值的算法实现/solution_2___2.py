# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def get_value(data, path):  # 定义函数 get_value（参数：data, 当前路径）
    result = data  # 把 data 存入 结果
    for k in path:  # 逐个取出 当前路径 的元素（下标 k）
        result = result[k]  # 把 结果[下标 k] 存入 结果
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 「__main__」
    data = {"a": {"b": {"c": 1}}, "d": {"e": 2}}  # 把 {'数组': {'b': {'字符': 1}}, 'd': {'e': 2}} 存入 data
    path = ["a", "b", "c"]  # 把 ['数组', 'b', '字符'] 存入 当前路径
    print(get_value(data, path))  # 打印输出
