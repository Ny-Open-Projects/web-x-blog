# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def get_value(data, path):  # 定义函数 get_value（参数：data, 当前路径）
    """使用指针(游标)逐层下钻，按 path 列表从嵌套字典中取节点值。"""
    node = data  # 把 data 存入 节点
    for key in path:  # 逐个取出 当前路径 的元素（key）
        if not isinstance(node, dict) or key not in node:  # 若 not isinstance(节点, dict) or key not in 节点
            return None  # 返回 None
        node = node[key]  # 把 节点[key] 存入 节点
    return node  # 返回 节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    data = {  # 把 { 存入 data
        "a": {"b": {"c": 1}},
        "d": {"e": 2},
    }
    path = ["a", "b", "c"]  # 把 ['数组', 'b', '字符'] 存入 当前路径
    print("value:", get_value(data, path))  # 打印输出
