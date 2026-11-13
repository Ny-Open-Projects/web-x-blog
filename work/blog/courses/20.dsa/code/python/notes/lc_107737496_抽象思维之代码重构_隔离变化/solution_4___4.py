# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def place_fill(n):  # 定义函数 place_fill（参数：元素个数）
    """依据前一位置、方向（DRUL 逆时针）与边界规则确定下一个摆放位置（方案 4）。"""
    m = [[0] * n for _ in range(n)]  # 把 [[0] 乘 元素个数 for _ in range(元素个数)] 存入 映射表
    row = col = 0  # 把 col 赋值为 0 存入 row
    direction = "D"  # D 向下, R 向右, U 向上, L 向左（逆时针）
    num = 1  # 把 1 存入 num
    total = n * n  # 把 元素个数 乘 元素个数 存入 总和
    while num <= total:  # 循环，直到不满足「num 不超过 总和」
        m[row][col] = num  # 把 num 写入 m[row][col]
        num += 1  # num累加 1
        if direction == "D":  # 若 direction 等于 'D'
            if (
                row + 1 < n and m[row + 1][col] == 0
            ):  # 若 row 加 1 小于 元素个数 and 映射表[row 加 1][col] 等于 0
                row += 1  # row累加 1
            else:  # 否则
                direction = "R"  # 把 'R' 存入 direction
                col += 1  # col累加 1
        elif direction == "R":  # 否则，若 direction 等于 'R'
            if (
                col + 1 < n and m[row][col + 1] == 0
            ):  # 若 col 加 1 小于 元素个数 and 映射表[row][col 加 1] 等于 0
                col += 1  # col累加 1
            else:  # 否则
                direction = "U"  # 把 'U' 存入 direction
                row -= 1  # row累减 1
        elif direction == "U":  # 否则，若 direction 等于 'U'
            if row - 1 >= 0 and m[row - 1][col] == 0:  # 若 row 减 1 不低于 0 and 映射表[row 减 1][col] 等于 0
                row -= 1  # row累减 1
            else:  # 否则
                direction = "L"  # 把 'L' 存入 direction
                col -= 1  # col累减 1
        else:  # 'L'
            if col - 1 >= 0 and m[row][col - 1] == 0:  # 若 col 减 1 不低于 0 and 映射表[row][col 减 1] 等于 0
                col -= 1  # col累减 1
            else:  # 否则
                direction = "D"  # 把 'D' 存入 direction
                row += 1  # row累加 1
    return m  # 返回 映射表


def print_matrix(m):  # 定义函数 print_matrix（参数：映射表）
    for row in m:  # 逐个取出 映射表 的元素（row）
        print(" ".join(f"{x:2d}" for x in row))  # 打印输出


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print_matrix(place_fill(6))  # print_matrix(place_fill(6))
