# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145244140
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def eraseOverlapIntervals(intervals):  # 定义函数 eraseOverlapIntervals（参数：intervals）
    if not intervals:  # 若 not intervals
        return 0  # 返回 0
    intervals.sort(key=lambda x: x[1])  # 排序
    count = 1  # 把 1 存入 计数
    end = intervals[0][1]  # 把 intervals[0][1] 存入 终点
    for i in range(1, len(intervals)):  # 让 下标 i 从 1 到 长度(intervals 遍历
        if intervals[i][0] >= end:  # 若 intervals[下标 i][0] 不低于 终点
            count += 1  # 计数累加 1
            end = intervals[i][1]  # 把 intervals[下标 i][1] 存入 终点
    return len(intervals) - count  # 返回 长度(intervals) 减 计数


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(eraseOverlapIntervals(None))  # 打印输出
