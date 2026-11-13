# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233874
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def permuteUnique(nums):  # 定义函数 permuteUnique（参数：数组）
    nums.sort()  # 排序
    res = []  # 把 [] 存入 结果
    used = [False] * len(nums)  # 把 [False] 乘 长度(数组) 存入 已用标记

    def backtrack(path):  # 定义函数 backtrack（参数：当前路径）
        if len(path) == len(nums):  # 若 长度(当前路径) 等于 长度(数组
            res.append(path[:])  # 把 复制 当前路径 追加到列表尾部
            return  # return
        for i in range(len(nums)):  # 让 下标 i 从 长度(数组 遍历
            if used[i]:  # 若 已用标记[下标 i]
                continue  # 跳过本轮，进入下一次
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue  # 跳过本轮，进入下一次
            used[i] = True  # 把 True 写入 used[i]
            path.append(nums[i])  # 把 数组[下标 i] 追加到列表尾部
            backtrack(path)  # backtrack(当前路径)
            path.pop()  # 弹出栈顶元素
            used[i] = False  # 把 False 写入 used[i]

    backtrack([])  # backtrack([])
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(permuteUnique([1, 1, 2]))  # 打印输出
