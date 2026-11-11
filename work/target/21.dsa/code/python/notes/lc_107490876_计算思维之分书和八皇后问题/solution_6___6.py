# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def n_queens_func():  # 定义函数 n_queens_func（参数：无）
    """八皇后问题（程序优化 / 函数式不可变状态传递）：每次递归传入新的状态副本。"""
    SIZE = 8  # 把 8 存入 SIZE
    results = []  # 把 [] 存入 results

    def place(col, state):  # 定义函数 place（参数：col, state）
        col_row_list, rows, diag1, diag2 = state  # 把 state 写入 col_row_list, rows, diag1, diag2
        if col == SIZE:  # 若 col 等于 SIZE
            results.append(state[0])  # 把 state[0] 追加到列表尾部
            return  # return
        for row in range(SIZE):  # 让 row 从 SIZE 遍历
            d1 = col - row + (SIZE - 1)  # 把 col 减 row 加 (SIZE 减 1) 存入 d1
            d2 = col + row  # 把 col 加 row 存入 d2
            if rows[row] and diag1[d1] and diag2[d2]:  # 若 行数[row] and diag1[d1] and diag2[d2]
                nr = rows[:]
                nr[row] = False  # 把 复制 行数; nr[row] 赋值为 False 存入 nr
                nd1 = diag1[:]
                nd1[d1] = False  # 把 复制 diag1; nd1[d1] 赋值为 False 存入 nd1
                nd2 = diag2[:]
                nd2[d2] = False  # 把 复制 diag2; nd2[d2] 赋值为 False 存入 nd2
                place(
                    col + 1, (state[0] + [row], nr, nd1, nd2)
                )  # place(col 加 1, (state[0] 加 [row], nr, nd1, nd2))

    place(0, ([], [True] * SIZE, [True] * (2 * SIZE - 1), [True] * (2 * SIZE - 1)))
    return results  # 返回 results


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    sols = n_queens_func()  # 把 n_queens_func() 存入 sols
    print("八皇后方案数:", len(sols))  # 打印输出
    print("第一个方案(列->行,0-indexed):", sols[0])  # 打印输出
