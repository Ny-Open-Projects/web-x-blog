# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370422
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class Bitset:  # 定义类
    def __init__(self, size):  # 构造函数：初始化成员
        self.n = size  # 把 大小 写入 元素个数
        self.words = [0] * ((size + 31) // 32)  # 把 [0] 乘 ((大小 加 31) 除以 除以 32) 写入 单词列表
        self.ones = 0  # 把 0 写入 self.ones
        self.reverse = 0  # 把 0 写入 self.reverse

    def _real_flag(self, idx):  # 定义函数 _real_flag（参数：self, idx）
        index = idx // 32  # 把 idx 除以 除以 32 存入 index
        bit = idx % 32  # 把 idx 对…取模 32 存入 bit
        return (
            (self.words[index] >> bit) & 1
        ) ^ self.reverse  # 返回 ((self.单词列表[index] 超过 超过 bit) 按位与 1) 按位异或 self.reverse

    def _set_flag(self, idx, v):  # 定义函数 _set_flag（参数：self, idx, 值）
        index = idx // 32  # 把 idx 除以 除以 32 存入 index
        bit = idx % 32  # 把 idx 对…取模 32 存入 bit
        old = self._real_flag(idx)  # 把 self._real_flag(idx) 存入 old
        if old != v:  # 若 old 不等于 值
            self.ones += v - old  # self.ones累加 (值 减 old)
            physical = v ^ self.reverse  # 把 值 按位异或 self.reverse 存入 physical
            if physical == 1:  # 若 physical 等于 1
                self.words[index] |= 1 << bit  # 把 (1 小于 小于 bit) 写入 self.words[index] |
            else:  # 否则
                self.words[index] &= ~(1 << bit)  # 把 ~(1 小于 小于 bit) 写入 self.words[index] &

    def fix(self, idx):  # 定义函数 fix（参数：self, idx）
        self._set_flag(idx, 1)  # self._set_flag(idx, 1)

    def unfix(self, idx):  # 定义函数 unfix（参数：self, idx）
        self._set_flag(idx, 0)  # self._set_flag(idx, 0)

    def flip(self):  # 定义函数 flip（参数：self）
        self.reverse ^= 1  # 把 1 写入 self.reverse ^
        self.ones = self.n - self.ones  # 把 self.元素个数 减 self.ones 写入 self.ones

    def all(self):  # 定义函数 all（参数：self）
        return self.ones == self.n  # 返回 self.ones 等于 self.元素个数

    def one(self):  # 定义函数 one（参数：self）
        return self.ones > 0  # 返回 self.ones 超过 0

    def count(self):  # 定义函数 count（参数：self）
        return self.ones  # 返回 self.ones

    def toString(self):  # 定义函数 toString（参数：self）
        return "".join(str(self._real_flag(i)) for i in range(self.n))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    bs = Bitset(5)  # 把 Bitset(5) 存入 bs
    bs.fix(0)  # bs.fix(0)
    bs.fix(3)  # bs.fix(3)
    print(bs.toString())  # 打印输出
    print(bs.count())  # 打印输出
    bs.flip()  # bs.flip()
    print(bs.toString())  # 打印输出
    print(bs.count())  # 打印输出
    bs.unfix(0)  # bs.unfix(0)
    print(bs.toString())  # 打印输出
    print(bs.all(), bs.one())  # 打印输出
