# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145354313
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class BrowserHistory:  # 定义类
    def __init__(self, homepage: str):  # 构造函数：初始化成员
        self.history = [homepage]  # 把 [homepage] 写入 self.history
        self.current = 0  # 把 0 写入 self.current

    def visit(self, url: str) -> None:  # 定义函数 visit（参数：self, url: str）
        # Remove forward history
        self.history = self.history[
            : self.current + 1
        ]  # 把 self.history[:self.current 加 1] 写入 self.history
        self.history.append(url)  # 把 url 追加到列表尾部
        self.current = len(self.history) - 1  # 把 长度(self.history) 减 1 写入 self.current

    def back(self, steps: int) -> str:  # 定义函数 back（参数：self, steps: int）
        self.current = max(0, self.current - steps)  # 把 取较大值 0, self.current 减 steps) 写入 self.current
        return self.history[self.current]  # 返回 self.history[self.current]

    def forward(self, steps: int) -> str:  # 定义函数 forward（参数：self, steps: int）
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]  # 返回 self.history[self.current]


def solve():  # 定义函数 solve（参数：无）
    browser = BrowserHistory("leetcode.com")  # 把 BrowserHistory(「leetcode.com」) 存入 browser
    browser.visit("google.com")  # browser.visit(「google.com」)
    browser.visit("facebook.com")  # browser.visit(「facebook.com」)
    browser.visit("youtube.com")  # browser.visit(「youtube.com」)
    print(browser.back(1))  # "facebook.com"
    print(browser.forward(2))  # "youtube.com"


if __name__ == "__main__":  # 若 __name__ 等于 「__main__」
    solve()  # solve()
