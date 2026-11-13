# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107579658
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def solve_unified(queen=False):  # 定义函数 solve_unified（参数：queen 赋值为 False）
    """转换视角、提炼共性：分书问题与八皇后问题可抽象为同一类“逐列放置 + 安全/合法检查”的回溯问题。
    queen=False 时分书（5 人 5 书，列=书，行=人，受喜好表约束）；
    queen=True 时八皇后（8x8，所有位置均可放）。"""
    SIZE = 8 if queen else 5  # 把 8 if queen else 5 存入 SIZE
    like = [
        [0, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1],
    ]
    Q = [-1] * SIZE  # 把 [ 减 1] 乘 SIZE 存入 Q
    rows = [True] * SIZE  # 把 [True] 乘 SIZE 存入 行数
    if queen:  # 若 queen
        diag1 = [True] * (2 * SIZE - 1)  # 把 [True] 乘 (2 乘 SIZE 减 1) 存入 diag1
        diag2 = [True] * (2 * SIZE - 1)  # 把 [True] 乘 (2 乘 SIZE 减 1) 存入 diag2
    results = []  # 把 [] 存入 results

    def is_valid(row, col):  # 定义函数 is_valid（参数：row, col）
        if queen:  # 若 queen
            return True  # 返回 True
        return like[row][col] == 1  # 返回 like[row][col] 等于 1

    def is_safe(row, col):  # 定义函数 is_safe（参数：row, col）
        if queen:  # 若 queen
            return rows[row] and diag1[col - row + SIZE - 1] and diag2[col + row]
        return rows[row]  # 返回 行数[row]

    def place(col):  # 定义函数 place（参数：col）
        if col == SIZE:  # 若 col 等于 SIZE
            results.append(Q[:])  # 把 复制 Q 追加到列表尾部
            return  # return
        for row in range(SIZE):  # 让 row 从 SIZE 遍历
            if not is_valid(row, col):  # 若 not is_valid(row, col
                continue  # 跳过本轮，进入下一次
            if not is_safe(row, col):  # 若 not is_safe(row, col
                continue  # 跳过本轮，进入下一次
            Q[col] = row  # 把 row 写入 Q[col]
            rows[row] = False  # 把 False 写入 rows[row]
            if queen:  # 若 queen
                d1 = col - row + SIZE - 1  # 把 col 减 row 加 SIZE 减 1 存入 d1
                d2 = col + row  # 把 col 加 row 存入 d2
                diag1[d1] = diag2[d2] = False  # 把 diag2[d2] 赋值为 False 写入 diag1[d1]
            place(col + 1)  # place(col 加 1)
            rows[row] = True  # 把 True 写入 rows[row]
            if queen:  # 若 queen
                diag1[d1] = diag2[d2] = True  # 把 diag2[d2] 赋值为 True 写入 diag1[d1]

    place(0)  # place(0)
    return results  # 返回 results


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    books = solve_unified(queen=False)  # 把 solve_unified(queen 赋值为 False) 存入 books
    queens = solve_unified(queen=True)  # 把 solve_unified(queen 赋值为 True) 存入 queens
    print("分书方案数:", len(books))  # 打印输出
    print("八皇后方案数:", len(queens))  # 打印输出
