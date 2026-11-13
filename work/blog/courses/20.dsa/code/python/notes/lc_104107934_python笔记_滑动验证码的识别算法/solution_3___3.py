# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def detect_edges(image):  # 定义函数 detect_edges（参数：image）
    edges = [False] * len(image)  # 把 [False] 乘 长度(image) 存入 边集
    for i in range(1, len(image)):  # 让 下标 i 从 1 到 长度(image 遍历
        edges[i] = (
            abs(image[i] - image[i - 1]) > 50
        )  # 把 取绝对值 image[下标 i] 减 image[下标 i 减 1]) 超过 50 写入 edges[i]
    return edges  # 返回 边集


def ncc_match(bg, puzzle):  # 定义函数 ncc_match（参数：bg, puzzle）
    """归一化互相关（NCC）模板匹配：寻找使相关系数最大的横坐标。"""
    best_x, best_score = 0, -float("inf")  # 把 0, 减 float('inf') 写入 best_x, best_score
    n = len(puzzle)  # 把 长度(puzzle) 存入 元素个数
    for x in range(len(bg) - n + 1):  # 让 x 从 长度(bg 遍历
        window = bg[x : x + n]  # 把 bg[x:x 加 元素个数] 存入 window
        bw = sum(window) / n  # 把 累计和(window) 除以 元素个数 存入 bw
        pw = sum(puzzle) / n  # 把 累计和(puzzle) 除以 元素个数 存入 pw
        num = sum((window[i] - bw) * (puzzle[i] - pw) for i in range(n))
        db = (
            sum((v - bw) ** 2 for v in window) ** 0.5
        )  # 把 累计和((值 减 bw) 乘 乘 2 for 值 in window) 乘 乘 0.5 存入 db
        dp = (
            sum((v - pw) ** 2 for v in puzzle) ** 0.5
        )  # 把 累计和((值 减 pw) 乘 乘 2 for 值 in puzzle) 乘 乘 0.5 存入 DP 表
        denom = db * dp  # 把 db 乘 DP 表 存入 denom
        score = num / denom if denom != 0 else 0  # 把 num 除以 denom if denom 不等于 0 else 0 存入 score
        if score > best_score:  # 若 score 超过 best_score
            best_score = score  # 把 score 存入 best_score
            best_x = x  # 把 x 存入 best_x
    return best_x  # 返回 best_x


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    bg = [10, 10, 10, 10, 200, 200, 200, 200]  # 把 [10, 10, 10, 10, 200, 200, 200, 200] 存入 bg
    puzzle = [10, 200, 200, 200]  # 把 [10, 200, 200, 200] 存入 puzzle
    print("NCC 匹配到的横坐标:", ncc_match(bg, puzzle))  # 打印输出
