# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def majorityElement(arr):  # 定义函数 majorityElement（参数：数组）
    """求多数元素（出现次数 > n/2），使用 Boyer-Moore 投票法。无多数元素时返回 -1。"""
    candidate = None  # 把 None 存入 candidate
    count = 0  # 把 0 存入 计数
    for num in arr:  # 逐个取出 数组 的元素（num）
        if count == 0:  # 若 计数 等于 0
            candidate = num  # 把 num 存入 candidate
        count += 1 if num == candidate else -1  # 计数累加 1 if num 等于 candidate else 减 1
    # 验证候选是否真的为多数元素
    if arr.count(candidate) > len(arr) // 2:  # 若 数组.计数(candidate) 超过 长度(数组) 除以 除以 2
        return candidate  # 返回 candidate
    return -1  # 返回 减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(majorityElement([2, 2, 1, 1, 1, 1, 1]))  # 打印输出
    print(majorityElement([1, 2, 3]))  # 打印输出
