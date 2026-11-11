# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130455100
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def canPlaceFlowers(flowerbed, n):  # 定义函数 canPlaceFlowers（参数：flowerbed, 元素个数）
    l = -1  # 把 减 1 存入 左指针
    r = 0  # 把 0 存入 右指针
    while r <= len(flowerbed):  # 循环，直到不满足「右指针 不超过 长度(flowerbed」
        rv = (
            0 if r == len(flowerbed) else flowerbed[r]
        )  # 把 0 if 右指针 等于 长度(flowerbed) else flowerbed[右指针] 存入 rv
        r += 1  # 右指针累加 1
        if rv == 1:  # 若 rv 等于 1
            l = r  # 把 右指针 存入 左指针
        if r - l == 3:  # 若 右指针 减 左指针 等于 3
            n -= 1  # 元素个数累减 1
            l += 2  # 左指针累加 2
    return n <= 0  # 返回 元素个数 不超过 0


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(canPlaceFlowers([1, 0, 0, 0, 1], 1))  # 打印输出
    print(canPlaceFlowers([1, 0, 0, 0, 1], 2))  # 打印输出
