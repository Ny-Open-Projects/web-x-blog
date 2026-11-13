# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145240015
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def combine(n, k):  # 定义函数 combine（参数：元素个数, 下标 k）
    result = []  # 把 [] 存入 结果

    def backtrack(start, path):  # 定义函数 backtrack（参数：起点, 当前路径）
        if len(path) == k:  # 若 长度(当前路径) 等于 下标 k
            result.append(path[:])  # 把 复制 当前路径 追加到列表尾部
            return  # return
        for i in range(start, n + 1):  # 让 下标 i 从 起点 到 元素个数 加 1 遍历
            path.append(i)  # 把 下标 i 追加到列表尾部
            backtrack(i + 1, path)  # backtrack(下标 i 加 1, 当前路径)
            path.pop()  # 弹出栈顶元素

    backtrack(1, [])  # backtrack(1, [])
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(combine(1, 1))  # 打印输出
