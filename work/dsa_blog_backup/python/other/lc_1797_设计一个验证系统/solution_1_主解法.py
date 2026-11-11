# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145354494
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class AuthenticationManager:  # 定义类
    def __init__(self, timeToLive):  # 构造函数：初始化成员
        self.expires_at = {}  # 把 {} 写入 self.expires_at
        self.ttl = timeToLive  # 把 timeToLive 写入 self.ttl

    def generate(self, token, currentTime):  # 定义函数 generate（参数：self, token, currentTime）
        self.expires_at[token] = (
            currentTime + self.ttl
        )  # 把 currentTime 加 self.ttl 写入 self.expires_at[token]

    def renew(self, token, currentTime):  # 定义函数 renew（参数：self, token, currentTime）
        if token in self.expires_at and self.expires_at[token] > currentTime:
            self.expires_at[token] = (
                currentTime + self.ttl
            )  # 把 currentTime 加 self.ttl 写入 self.expires_at[token]
            return 1  # 返回 1
        return 0  # 返回 0

    def countValidTokens(self, currentTime):  # 定义函数 countValidTokens（参数：self, currentTime）
        count = 0  # 把 0 存入 计数
        for token, expire in self.expires_at.items():  # for token, expire in self.expires_at.items():
            if expire > currentTime:  # 若 expire 超过 currentTime
                count += 1  # 计数累加 1
        return count  # 返回 计数


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    auth = AuthenticationManager(5)  # 把 AuthenticationManager(5) 存入 auth
    auth.generate("aaa", 1)  # auth.generate(「aaa」, 1)
    print(auth.countValidTokens(3))  # 打印输出
    print(auth.renew("aaa", 4))  # 打印输出
    print(auth.countValidTokens(6))  # 打印输出
