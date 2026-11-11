# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233215
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def mySqrt(x):  # 定义函数 mySqrt（参数：x）
    if x < 2:  # 若 x 小于 2
        return x  # 返回 x
    left, right = 1, x // 2  # 把 1, x 除以 除以 2 写入 left, right
    while left <= right:  # 循环，直到不满足「左边界 不超过 右边界」
        mid = (left + right) // 2  # 把 (左边界 加 右边界) 除以 除以 2 存入 中点
        square = mid * mid  # 把 中点 乘 中点 存入 square
        if square == x:  # 若 square 等于 x
            return mid  # 返回 中点
        elif square < x:  # 否则，若 square 小于 x
            left = mid + 1  # 把 中点 加 1 存入 左边界
        else:  # 否则
            right = mid - 1  # 把 中点 减 1 存入 右边界
    return right  # 返回 右边界


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(mySqrt(8))  # 打印输出
