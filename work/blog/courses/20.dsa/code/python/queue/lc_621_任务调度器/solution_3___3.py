# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import Counter  # from collections import Counter


def leastInterval(tasks, n):  # 定义函数 leastInterval（参数：tasks, 元素个数）
    # 贪心模拟：每轮从剩余任务里挑出现次数最多的前 n+1 个执行（其余为冷却），
    # 最后一轮只计实际执行数，不补冷却
    cnt = list(Counter(tasks).values())  # 把 列表(Counter(tasks).values()) 存入 计数
    time = 0  # 把 0 存入 time
    while cnt:  # 循环，直到不满足「计数」
        cnt.sort(reverse=True)  # 排序
        used = 0  # 把 0 存入 已用标记
        for i in range(min(n + 1, len(cnt))):  # 让 下标 i 从 取较小值 元素个数 加 1 到 长度(计数 遍历
            if cnt[i] > 0:  # 若 计数[下标 i] 超过 0
                cnt[i] -= 1  # cnt[i]累减 1
                used += 1  # 已用标记累加 1
        cnt = [c for c in cnt if c > 0]  # 把 [字符 for 字符 in 计数 if 字符 超过 0] 存入 计数
        time += (n + 1) if cnt else used  # time累加 (元素个数 加 1) if 计数 else 已用标记
    return time  # 返回 time


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(leastInterval(["A", "A", "A", "B", "B", "B"], 2))  # 打印输出
