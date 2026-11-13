# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134359782
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
_pick = 6  # 把 6 存入 _pick


def guess(num):  # 定义函数 guess（参数：num）
    if num == _pick:  # 若 num 等于 _pick
        return 0  # 返回 0
    return 1 if num < _pick else -1  # 返回 1 if num 小于 _pick else 减 1


def guessNumber(n):  # 定义函数 guessNumber（参数：元素个数）
    def rec(low, high):  # 定义函数 rec（参数：low, high）
        if low > high:  # 若 low 超过 high
            return -1  # 返回 减 1
        mid = (low + high) // 2  # 把 (low 加 high) 除以 除以 2 存入 中点
        res = guess(mid)  # 把 guess(中点) 存入 结果
        if res == 0:  # 若 结果 等于 0
            return mid  # 返回 中点
        if res == 1:  # 若 结果 等于 1
            return rec(mid + 1, high)  # 返回 rec(中点 加 1, high)
        return rec(1, mid - 1)  # 返回 rec(1, 中点 减 1)

    return rec(1, n)  # 返回 rec(1, 元素个数)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    _pick = 6  # 把 6 存入 _pick
    print(guessNumber(10))  # 打印输出
