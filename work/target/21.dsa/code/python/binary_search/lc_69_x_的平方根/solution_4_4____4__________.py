# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233215
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def mySqrt(x):  # 定义函数 mySqrt（参数：x）
    if x == 0:  # 若 x 等于 0
        return 0  # 返回 0
    C = x  # 把 x 存入 C
    x0 = x  # 把 x 存入 x0
    while True:  # 循环，直到不满足「True」
        xi = 0.5 * (x0 + C / x0)  # 把 0.5 乘 (x0 加 C 除以 x0) 存入 xi
        if abs(x0 - xi) < 1e-7:  # 若 取绝对值 x0 减 xi) 小于 1e 减 7
            break  # 跳出循环
        x0 = xi  # 把 xi 存入 x0
    return int(x0)  # 返回 int(x0)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(mySqrt(1))  # 打印输出
