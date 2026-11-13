# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import deque  # from collections import deque


class RecentCounter:  # 定义类
    # 维护一个队列，只保留 [t-3000, t] 时间窗口内的请求
    def __init__(self):  # 构造函数：初始化成员
        self.q = deque()  # 把 deque() 写入 节点

    def ping(self, t):  # 定义函数 ping（参数：self, 另一字符串）
        self.q.append(t)  # 把 另一字符串 追加到列表尾部
        while self.q[0] < t - 3000:  # 循环，直到不满足「self.节点[0] 小于 另一字符串 减 3000」
            self.q.popleft()  # self.节点.popleft()
        return len(self.q)  # 返回 长度(self.节点)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    rc = RecentCounter()  # 把 RecentCounter() 存入 rc
    print(rc.ping(1))  # 打印输出
    print(rc.ping(100))  # 打印输出
    print(rc.ping(3001))  # 打印输出
