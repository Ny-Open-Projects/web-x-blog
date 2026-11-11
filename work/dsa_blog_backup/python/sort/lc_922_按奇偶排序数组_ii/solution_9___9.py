# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134394571
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortArrayByParityII(nums):  # 定义函数 sortArrayByParityII（参数：数组）
    res = [0] * len(nums)  # 把 [0] 乘 长度(数组) 存入 结果
    e = 0  # 把 0 存入 e
    o = 1  # 把 1 存入 o
    for x in nums:  # 逐个取出 数组 的元素（x）
        if x % 2 == 0:  # 若 x 对…取模 2 等于 0
            res[e] = x  # 把 x 写入 res[e]
            e += 2  # e累加 2
        else:  # 否则
            res[o] = x  # 把 x 写入 res[o]
            o += 2  # o累加 2
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortArrayByParityII([4, 2, 5, 7]))  # 打印输出
    print(sortArrayByParityII([2, 3]))  # 打印输出
