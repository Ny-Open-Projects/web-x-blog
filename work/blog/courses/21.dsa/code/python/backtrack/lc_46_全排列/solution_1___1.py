# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134689827
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def permute(nums):  # 定义函数 permute（参数：数组）
    res = []  # 把 [] 存入 结果

    def backtrack(path):  # 定义函数 backtrack（参数：当前路径）
        if len(path) == len(nums):  # 若 长度(当前路径) 等于 长度(数组
            res.append(path[:])  # 把 复制 当前路径 追加到列表尾部
            return  # return
        for i in range(0, len(nums)):  # 让 下标 i 从 0 到 长度(数组 遍历
            if nums[i] in path:  # 若 数组[下标 i] in 当前路径
                continue  # 跳过本轮，进入下一次
            backtrack(path + [nums[i]])  # backtrack(当前路径 加 [数组[下标 i]])

    backtrack([])  # backtrack([])
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(permute([1, 2, 3]))  # 打印输出
