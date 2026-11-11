# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def topKFrequent(nums, k):  # 定义函数 topKFrequent（参数：数组, 下标 k）
    map = {}  # 把 {} 存入 映射表
    for n in nums:  # 逐个取出 数组 的元素（元素个数）
        map[n] = map.get(n, 0) + 1  # 把 映射表 查找 元素个数, 0) 加 1 写入 map[n]
    list = sorted(map.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in list[:k]]  # 返回 [item[0] for item in 列表[:下标 k]]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(topKFrequent([1, 2, 3], 1))  # 打印输出
