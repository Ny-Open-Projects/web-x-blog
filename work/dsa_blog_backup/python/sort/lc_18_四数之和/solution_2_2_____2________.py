# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245574
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def fourSum(nums, target):  # 定义函数 fourSum（参数：数组, 目标值）
    nums.sort()  # 排序
    result = []  # 把 [] 存入 结果
    n = len(nums)  # 把 长度(数组) 存入 元素个数

    def dfs(start, k, remaining, path):  # 定义函数 dfs（参数：起点, 下标 k, remaining, 当前路径）
        if k == 0:  # 若 下标 k 等于 0
            if remaining == 0:  # 若 remaining 等于 0
                result.append(path[:])  # 把 复制 当前路径 追加到列表尾部
            return  # return
        for i in range(start, n - k + 1):  # 让 下标 i 从 起点 到 元素个数 减 k 加 1 遍历（保证还够选 k 个）
            if (
                i > start and nums[i] == nums[i - 1]
            ):  # 若 下标 i 超过 起点 and 数组[下标 i] 等于 数组[下标 i 减 1]
                continue  # 跳过本轮，进入下一次
            if nums[i] * k > remaining:  # 若 数组[下标 i] 乘 下标 k 超过 remaining
                break  # 跳出循环
            if i + 1 < n and nums[i] + nums[i + 1] * (k - 1) > remaining:  # 最小补全都超，后面只会更大
                break  # 跳出循环
            if nums[i] + nums[n - 1] * (k - 1) < remaining:  # 最大补都不足
                continue  # 跳过本轮，进入下一次
                break  # 跳出循环
            path.append(nums[i])  # 把 数组[下标 i] 追加到列表尾部
            dfs(
                i + 1, k - 1, remaining - nums[i], path
            )  # dfs(下标 i 加 1, 下标 k 减 1, remaining 减 数组[下标 i], 当前路径)
            path.pop()  # 弹出栈顶元素

    dfs(0, 4, target, [])  # dfs(0, 4, 目标值, [])
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(fourSum([1, 2, 3], 1))  # 打印输出
