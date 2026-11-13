# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134429994
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def firstMissingPositive(nums):  # 定义函数 firstMissingPositive（参数：数组）
    if not nums:  # 若 not 数组
        return 1  # 返回 1
    m = {}  # 把 {} 存入 映射表
    max_val = float("-inf")  # 把 float(' 减 inf') 存入 max_val
    for item in nums:  # 逐个取出 数组 的元素（item）
        if item <= 0:  # 若 item 不超过 0
            continue  # 跳过本轮，进入下一次
        m[item] = 1  # 把 1 写入 m[item]
        max_val = max(max_val, item)  # 把 取较大值 max_val, item) 存入 max_val
    min_positive = 1  # 把 1 存入 min_positive
    while min_positive <= max_val:  # 循环，直到不满足「min_positive 不超过 max_val」
        if min_positive not in m:  # 若 min_positive not in 映射表
            return min_positive  # 返回 min_positive
        min_positive += 1  # min_positive累加 1
    return min_positive  # 返回 min_positive


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(firstMissingPositive([1, 2, 3]))  # 打印输出
