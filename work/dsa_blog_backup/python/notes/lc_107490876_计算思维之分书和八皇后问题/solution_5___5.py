# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def n_queens_bool():  # 定义函数 n_queens_bool（参数：无）
    """八皇后问题（优化回溯，S/L/R 布尔数组标记）：
    用 rows / 两条对角线方向的布尔数组快速判断安全性。"""
    SIZE = 8  # 把 8 存入 SIZE
    col_row = [0] * SIZE  # 把 [0] 乘 SIZE 存入 col_row
    rows = [True] * SIZE  # 把 [True] 乘 SIZE 存入 行数
    diag1 = [True] * (2 * SIZE - 1)  # (col - row + OFFSET)
    diag2 = [True] * (2 * SIZE - 1)  # (col + row)
    OFFSET = SIZE - 1  # 把 SIZE 减 1 存入 OFFSET
    results = []  # 把 [] 存入 results

    def place(col):  # 定义函数 place（参数：col）
        if col == SIZE:  # 若 col 等于 SIZE
            results.append(col_row[:])  # 把 复制 col_row 追加到列表尾部
            return  # return
        for row in range(SIZE):  # 让 row 从 SIZE 遍历
            d1 = col - row + OFFSET  # 把 col 减 row 加 OFFSET 存入 d1
            d2 = col + row  # 把 col 加 row 存入 d2
            if rows[row] and diag1[d1] and diag2[d2]:  # 若 行数[row] and diag1[d1] and diag2[d2]
                col_row[col] = row  # 把 row 写入 col_row[col]
                rows[row] = diag1[d1] = diag2[d2] = (
                    False  # 把 diag1[d1] 赋值为 diag2[d2] 赋值为 False 写入 rows[row]
                )
                place(col + 1)  # place(col 加 1)
                rows[row] = diag1[d1] = diag2[d2] = (
                    True  # 把 diag1[d1] 赋值为 diag2[d2] 赋值为 True 写入 rows[row]
                )

    place(0)  # place(0)
    return results  # 返回 results


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    sols = n_queens_bool()  # 把 n_queens_bool() 存入 sols
    print("八皇后方案数:", len(sols))  # 打印输出
    print("第一个方案(列->行,0-indexed):", sols[0])  # 打印输出
