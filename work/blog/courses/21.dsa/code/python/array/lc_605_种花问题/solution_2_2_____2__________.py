# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130455100
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def canPlaceFlowers(flowerbed, n):  # 定义函数 canPlaceFlowers（参数：flowerbed, 元素个数）
    count = 0  # 把 0 存入 计数
    flowerbed = flowerbed + [0]  # 把 flowerbed 加 [0] 存入 flowerbed
    for i in range(len(flowerbed) - 1):  # 让 下标 i 从 长度(flowerbed 遍历
        if (
            flowerbed[i] == 0 and flowerbed[i + 1] == 0
        ):  # 若 flowerbed[下标 i] 等于 0 and flowerbed[下标 i 加 1] 等于 0
            count += 1  # 计数累加 1
            flowerbed[i + 1] = 1  # 把 1 写入 flowerbed[i + 1]
    return count >= n  # 返回 计数 不低于 元素个数


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(canPlaceFlowers([1, 0, 0, 0, 1], 1))  # 打印输出
    print(canPlaceFlowers([1, 0, 0, 0, 1], 2))  # 打印输出
