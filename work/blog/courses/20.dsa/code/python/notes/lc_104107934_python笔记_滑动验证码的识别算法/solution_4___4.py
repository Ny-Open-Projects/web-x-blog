# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def best_match_window(bg, puzzle):  # 定义函数 best_match_window（参数：bg, puzzle）
    """滑窗最小绝对差匹配：在每个候选位置计算背景窗口与拼图的绝对差之和，取最小者。"""
    best_x, best_score = 0, float("inf")  # 把 0, float('inf') 写入 best_x, best_score
    n = len(puzzle)  # 把 长度(puzzle) 存入 元素个数
    for x in range(len(bg) - n + 1):  # 让 x 从 长度(bg 遍历
        score = sum(abs(bg[x + y] - puzzle[y]) for y in range(n))
        if score < best_score:  # 若 score 小于 best_score
            best_score = score  # 把 score 存入 best_score
            best_x = x  # 把 x 存入 best_x
    return best_x, best_score  # 返回 best_x, best_score


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    bg = [10, 10, 10, 10, 200, 200, 200, 200]  # 把 [10, 10, 10, 10, 200, 200, 200, 200] 存入 bg
    puzzle = [10, 200, 200, 200]  # 把 [10, 200, 200, 200] 存入 puzzle
    x, score = best_match_window(bg, puzzle)  # 把 best_match_window(bg, puzzle) 写入 x, score
    print("最佳匹配横坐标:", x, " 代价:", score)  # 打印输出
