# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134394571
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortArrayByParityII(nums):  # 定义函数 sortArrayByParityII（参数：数组）
    nums.sort()  # 排序
    res = [0] * len(nums)  # 把 [0] 乘 长度(数组) 存入 结果
    odd = 1  # 把 1 存入 odd
    even = 0  # 把 0 存入 even
    for item in nums:  # 逐个取出 数组 的元素（item）
        if item % 2 == 1:  # 若 item 对…取模 2 等于 1
            res[odd] = item  # 把 item 写入 res[odd]
            odd += 2  # odd累加 2
        else:  # 否则
            res[even] = item  # 把 item 写入 res[even]
            even += 2  # even累加 2
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortArrayByParityII([4, 2, 5, 7]))  # 打印输出
