# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def place(
    num, row, col, direction, n, m
):  # 定义函数 place（参数：num, row, col, direction, 元素个数, 映射表）
    """根据前一位置、方向(DRUL)与边界规则确定下一个摆放数据的位置（方案 7）。

    使用 dict 模拟 C++ 的 switch 分派。
    """
    handlers = {  # 把 { 存入 handlers
        "D": lambda: (row + 1, col) if (row + 1 < n and m[row + 1][col] == 0) else (row, col + 1, "R"),
        "R": lambda: (row, col + 1) if (col + 1 < n and m[row][col + 1] == 0) else (row - 1, col, "U"),
        "U": lambda: (row - 1, col) if (row - 1 >= 0 and m[row - 1][col] == 0) else (row, col - 1, "L"),
        "L": lambda: (row, col - 1) if (col - 1 >= 0 and m[row][col - 1] == 0) else (row + 1, col, "D"),
    }
    return handlers[direction]()  # 返回 handlers[direction]()


def fill_spiral(n):  # 定义函数 fill_spiral（参数：元素个数）
    m = [[0] * n for _ in range(n)]  # 把 [[0] 乘 元素个数 for _ in range(元素个数)] 存入 映射表
    row = col = 0  # 把 col 赋值为 0 存入 row
    direction = "D"  # 把 'D' 存入 direction
    num = 1  # 把 1 存入 num
    while num <= n * n:  # 循环，直到不满足「num 不超过 元素个数 乘 元素个数」
        m[row][col] = num  # 把 num 写入 m[row][col]
        num += 1  # num累加 1
        res = place(
            num, row, col, direction, n, m
        )  # 把 place(num, row, col, direction, 元素个数, 映射表) 存入 结果
        row, col = res[0], res[1]  # 把 结果[0], 结果[1] 写入 row, col
        if len(res) == 3:  # 若 长度(结果) 等于 3
            direction = res[2]  # 把 结果[2] 存入 direction
    return m  # 返回 映射表


def print_matrix(m):  # 定义函数 print_matrix（参数：映射表）
    for row in m:  # 逐个取出 映射表 的元素（row）
        print(" ".join(f"{x:2d}" for x in row))  # 打印输出


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print_matrix(fill_spiral(6))  # print_matrix(fill_spiral(6))
