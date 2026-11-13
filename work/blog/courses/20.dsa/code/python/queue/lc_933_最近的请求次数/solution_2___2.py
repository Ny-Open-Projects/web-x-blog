# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class RecentCounter:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.queue = []  # 把 [] 写入 队列
        self.front = 0  # 把 0 写入 self.front

    def ping(self, t):  # 定义函数 ping（参数：self, 另一字符串）
        self.queue.append(t)  # 把 另一字符串 追加到列表尾部
        while (
            self.queue[self.front] < t - 3000
        ):  # 循环，直到不满足「self.队列[self.front] 小于 另一字符串 减 3000」
            self.front += 1  # self.front累加 1
        return len(self.queue) - self.front  # 返回 长度(self.队列) 减 self.front


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    counter = RecentCounter()  # 把 RecentCounter() 存入 counter
    print(counter.ping(1))  # 打印输出
    print(counter.ping(100))  # 打印输出
    print(counter.ping(3001))  # 打印输出
