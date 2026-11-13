# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134689827
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def permute(nums):  # 定义函数 permute（参数：数组）
    res = []  # 把 [] 存入 结果

    def backtrack(start):  # 定义函数 backtrack（参数：起点）
        if start == len(nums):  # 若 起点 等于 长度(数组
            res.append(nums[:])  # 把 复制 数组 追加到列表尾部
            return  # return
        for i in range(start, len(nums)):  # 让 下标 i 从 起点 到 长度(数组 遍历
            nums[start], nums[i] = (
                nums[i],
                nums[start],
            )  # 把 数组[下标 i], 数组[起点] 写入 nums[start], nums[i]
            backtrack(start + 1)  # backtrack(起点 加 1)
            nums[start], nums[i] = (
                nums[i],
                nums[start],
            )  # 把 数组[下标 i], 数组[起点] 写入 nums[start], nums[i]

    backtrack(0)  # backtrack(0)
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(permute([1, 2, 3]))  # 打印输出
