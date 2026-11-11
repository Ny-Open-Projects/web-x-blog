# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134359782
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
_pick = 6  # 把 6 存入 _pick


def guess(num):  # 定义函数 guess（参数：num）
    if num > _pick:  # 若 num 超过 _pick
        return -1  # 返回 减 1
    elif num < _pick:  # 否则，若 num 小于 _pick
        return 1  # 返回 1
    return 0  # 返回 0


def guessNumber(n):  # 定义函数 guessNumber（参数：元素个数）
    left, right = 1, n  # 把 1, 元素个数 写入 left, right
    while left <= right:  # 循环，直到不满足「左边界 不超过 右边界」
        mid = (left + right) // 2  # 把 (左边界 加 右边界) 除以 除以 2 存入 中点
        g = guess(mid)  # 把 guess(中点) 存入 g
        if g == 0:  # 若 g 等于 0
            return mid  # 返回 中点
        elif g == 1:  # 否则，若 g 等于 1
            left = mid + 1  # 把 中点 加 1 存入 左边界
        else:  # 否则
            right = mid - 1  # 把 中点 减 1 存入 右边界
    return -1  # 返回 减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(guessNumber(10))  # 打印输出
