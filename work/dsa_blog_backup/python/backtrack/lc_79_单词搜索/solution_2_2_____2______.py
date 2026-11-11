# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145240191
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def exist(board, word):  # 定义函数 exist（参数：棋盘, 单词）
    if not board or not board[0]:  # 若 not 棋盘 or not 棋盘[0]
        return False  # 返回 False
    rows, cols = len(board), len(board[0])  # 把 长度(棋盘), 长度(棋盘[0]) 写入 rows, cols

    def backtrack(r, c, idx):  # 定义函数 backtrack（参数：右指针, 字符, idx）
        if idx == len(word):  # 若 idx 等于 长度(单词
            return True  # 返回 True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return False  # 返回 False
        temp = board[r][c]  # 把 棋盘[右指针][字符] 存入 临时变量
        board[r][c] = "#"
        found = (
            backtrack(r + 1, c, idx + 1)  # 把 (backtrack(右指针 加 1, 字符, idx 加 1) or 存入 found
            or backtrack(r - 1, c, idx + 1)  # backtrack(右指针 减 1, 字符, idx 加 1) or
            or backtrack(r, c + 1, idx + 1)  # backtrack(右指针, 字符 加 1, idx 加 1) or
            or backtrack(r, c - 1, idx + 1)
        )  # backtrack(右指针, 字符 减 1, idx 加 1))
        board[r][c] = temp  # 把 临时变量 写入 board[r][c]
        return found  # 返回 found

    for r in range(rows):  # 让 右指针 从 行数 遍历
        for c in range(cols):  # 让 字符 从 列数 遍历
            if backtrack(r, c, 0):  # 若 backtrack(右指针, 字符, 0
                return True  # 返回 True
    return False  # 返回 False


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(exist(None, "abc"))  # 打印输出
