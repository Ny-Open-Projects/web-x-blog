# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def detect_edges(image):  # 定义函数 detect_edges（参数：image）
    """边缘检测（一阶差分阈值法）：相邻像素灰度差超过阈值则记为边缘。"""
    edges = [False] * len(image)  # 把 [False] 乘 长度(image) 存入 边集
    for i in range(1, len(image)):  # 让 下标 i 从 1 到 长度(image 遍历
        edges[i] = (
            abs(image[i] - image[i - 1]) > 50
        )  # 把 取绝对值 image[下标 i] 减 image[下标 i 减 1]) 超过 50 写入 edges[i]
    return edges  # 返回 边集


def recognize_captcha(bg, puzzle):  # 定义函数 recognize_captcha（参数：bg, puzzle）
    """模板匹配识别缺口位置：在背景上滑动拼图，统计边缘重合度最高的横坐标。"""
    bg_edges = detect_edges(bg)  # 把 detect_edges(bg) 存入 bg_edges
    puzzle_edges = detect_edges(puzzle)  # 把 detect_edges(puzzle) 存入 puzzle_edges
    best_x, best_score = 0, -1  # 把 0, 减 1 写入 best_x, best_score
    for x in range(len(bg) - len(puzzle) + 1):  # 让 x 从 长度(bg 遍历
        score = 0  # 把 0 存入 score
        for y in range(len(puzzle)):  # 让 y 从 长度(puzzle 遍历
            if bg_edges[x + y] and puzzle_edges[y]:  # 若 bg_edges[x 加 y] and puzzle_edges[y]
                score += 1  # score累加 1
        if score > best_score:  # 若 score 超过 best_score
            best_score = score  # 把 score 存入 best_score
            best_x = x  # 把 x 存入 best_x
    return best_x  # 返回 best_x


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    bg = [10, 10, 10, 10, 200, 200, 200, 200]  # 把 [10, 10, 10, 10, 200, 200, 200, 200] 存入 bg
    puzzle = [10, 200, 200, 200]  # 把 [10, 200, 200, 200] 存入 puzzle
    print("识别到的缺口横坐标:", recognize_captcha(bg, puzzle))  # 打印输出
