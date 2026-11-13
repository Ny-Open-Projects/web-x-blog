# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def leastInterval(tasks, n):  # 定义函数 leastInterval（参数：tasks, 元素个数）
    from collections import Counter  # from collections import Counter

    count = Counter(tasks)  # 把 Counter(tasks) 存入 计数
    max_count = max(count.values())  # 把 取较大值 计数.values()) 存入 max_count
    max_count_tasks = sum(1 for v in count.values() if v == max_count)
    return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(leastInterval(["A", "A", "A", "B", "B", "B"], 2))  # 打印输出
