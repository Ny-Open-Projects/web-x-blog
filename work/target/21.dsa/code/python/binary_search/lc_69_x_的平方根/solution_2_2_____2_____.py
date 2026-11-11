# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233215
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def mySqrt(x):  # 定义函数 mySqrt（参数：x）
    l, r, ans = 0, x, -1  # 把 0, x, 减 1 写入 l, r, ans
    while l <= r:  # 循环，直到不满足「左指针 不超过 右指针」
        mid = l + (r - l) // 2  # 把 左指针 加 (右指针 减 左指针) 除以 除以 2 存入 中点
        if mid * mid <= x:  # 若 中点 乘 中点 不超过 x
            ans = mid  # 把 中点 存入 答案
            l = mid + 1  # 把 中点 加 1 存入 左指针
        else:  # 否则
            r = mid - 1  # 把 中点 减 1 存入 右指针
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(mySqrt(8))  # 打印输出
