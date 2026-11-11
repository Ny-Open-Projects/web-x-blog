# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130455100
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def canPlaceFlowers(flowerbed, n):  # 定义函数 canPlaceFlowers（参数：flowerbed, 元素个数）
    cnt = 0  # 把 0 存入 计数
    m = len(flowerbed)  # 把 长度(flowerbed) 存入 映射表
    for i in range(m):  # 让 下标 i 从 映射表 遍历
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == m - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1  # 把 1 写入 flowerbed[i]
            cnt += 1  # 计数累加 1
            if cnt >= n:  # 若 计数 不低于 元素个数
                return True  # 返回 True
    return cnt >= n  # 返回 计数 不低于 元素个数


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(canPlaceFlowers([1, 0, 0, 0, 1], 1))  # 打印输出
    print(canPlaceFlowers([1, 0, 0, 0, 1], 2))  # 打印输出
    print(canPlaceFlowers([0], 1))  # 打印输出
