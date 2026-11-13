# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134394571
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortArrayByParityII(nums):  # 定义函数 sortArrayByParityII（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    ans = [0] * n  # 把 [0] 乘 元素个数 存入 答案
    i, j = 0, 1  # 把 0, 1 写入 i, j
    for x in nums:  # 逐个取出 数组 的元素（x）
        if x % 2 == 0:  # 若 x 对…取模 2 等于 0
            ans[i] = x  # 把 x 写入 ans[i]
            i += 2  # 下标 i累加 2
        else:  # 否则
            ans[j] = x  # 把 x 写入 ans[j]
            j += 2  # 下标 j累加 2
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortArrayByParityII([4, 2, 5, 7]))  # 打印输出
