# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134359782
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
_pick = 6  # 把 6 存入 _pick


def guess(num):  # 定义函数 guess（参数：num）
    if num == _pick:  # 若 num 等于 _pick
        return 0  # 返回 0
    return 1 if num < _pick else -1  # 返回 1 if num 小于 _pick else 减 1


def guessNumber(n):  # 定义函数 guessNumber（参数：元素个数）
    low, high = 1, n  # 把 1, 元素个数 写入 low, high
    while low <= high:  # 循环，直到不满足「low 不超过 high」
        mid = (low + high) // 2  # 把 (low 加 high) 除以 除以 2 存入 中点
        res = guess(mid)  # 把 guess(中点) 存入 结果
        if res == 0:  # 若 结果 等于 0
            return mid  # 返回 中点
        if res == 1:  # 若 结果 等于 1
            low = mid + 1  # 把 中点 加 1 存入 low
        else:  # 否则
            high = mid - 1  # 把 中点 减 1 存入 high


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    _pick = 6  # 把 6 存入 _pick
    print(guessNumber(10))  # 打印输出
