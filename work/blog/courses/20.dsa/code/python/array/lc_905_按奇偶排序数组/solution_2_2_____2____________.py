# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145588341
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortArrayByParity(nums):  # 定义函数 sortArrayByParity（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    res = [0] * n  # 把 [0] 乘 元素个数 存入 结果
    left, right = 0, n - 1  # 把 0, 元素个数 减 1 写入 left, right
    for num in nums:  # 逐个取出 数组 的元素（num）
        if num % 2 == 0:  # 若 num 对…取模 2 等于 0
            res[left] = num  # 把 num 写入 res[left]
            left += 1  # 左边界累加 1
        else:  # 否则
            res[right] = num  # 把 num 写入 res[right]
            right -= 1  # 右边界累减 1
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortArrayByParity([1, 2, 3]))  # 打印输出
