# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from threading import Semaphore  # from threading import Semaphore


def solution():  # 定义函数 solution（参数：无）
    class Foo:  # 定义类
        def __init__(self):  # 构造函数：初始化成员
            self.first_done = Semaphore(0)  # 把 Semaphore(0) 写入 self.first_done
            self.second_done = Semaphore(0)  # 把 Semaphore(0) 写入 self.second_done

        def first(self, printFirst):  # 定义函数 first（参数：self, printFirst）
            printFirst()  # printFirst()
            self.first_done.release()  # self.first_done.release()

        def second(self, printSecond):  # 定义函数 second（参数：self, printSecond）
            self.first_done.acquire()  # self.first_done.acquire()
            printSecond()  # printSecond()
            self.second_done.release()  # self.second_done.release()

        def third(self, printThird):  # 定义函数 third（参数：self, printThird）
            self.second_done.acquire()  # self.second_done.acquire()
            printThird()  # printThird()

    return Foo()  # 返回 Foo()


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(solution())  # 打印输出
