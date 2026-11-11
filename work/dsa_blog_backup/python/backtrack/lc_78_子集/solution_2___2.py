# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134701204
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def subsets(nums):  # 定义函数 subsets（参数：数组）
    res = []  # 把 [] 存入 结果

    def backtrack(start, path):  # 定义函数 backtrack（参数：起点, 当前路径）
        res.append(path[:])  # 把 复制 当前路径 追加到列表尾部
        for i in range(start, len(nums)):  # 让 下标 i 从 起点 到 长度(数组 遍历
            path.append(nums[i])  # 把 数组[下标 i] 追加到列表尾部
            backtrack(i + 1, path)  # backtrack(下标 i 加 1, 当前路径)
            path.pop()  # 弹出栈顶元素

    backtrack(0, [])  # backtrack(0, [])
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(subsets([1, 2, 3]))  # 打印输出
