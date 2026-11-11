# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def detect_edges_sobel(image):  # 定义函数 detect_edges_sobel（参数：image）
    """边缘检测（中心差分法）：用 (p[i+1]-p[i-1])/2 的梯度幅值判定边缘。"""
    edges = [False] * len(image)  # 把 [False] 乘 长度(image) 存入 边集
    if len(image) < 2:  # 若 长度(image) 小于 2
        return edges  # 返回 边集
    edges[0] = abs(image[1] - image[0]) > 50  # 把 取绝对值 image[1] 减 image[0]) 超过 50 写入 edges[0]
    for i in range(1, len(image) - 1):  # 让 下标 i 从 1 到 长度(image 遍历
        edges[i] = (
            abs(image[i + 1] - image[i - 1]) > 50
        )  # 把 取绝对值 image[下标 i 加 1] 减 image[下标 i 减 1]) 超过 50 写入 edges[i]
    edges[-1] = (
        abs(image[-1] - image[-2]) > 50
    )  # 把 取绝对值 image[ 减 1] 减 image[ 减 2]) 超过 50 写入 edges[-1]
    return edges  # 返回 边集


def recognize_captcha(bg, puzzle):  # 定义函数 recognize_captcha（参数：bg, puzzle）
    bg_edges = detect_edges_sobel(bg)  # 把 detect_edges_sobel(bg) 存入 bg_edges
    puzzle_edges = detect_edges_sobel(puzzle)  # 把 detect_edges_sobel(puzzle) 存入 puzzle_edges
    best_x, best_score = 0, -1  # 把 0, 减 1 写入 best_x, best_score
    for x in range(len(bg) - len(puzzle) + 1):  # 让 x 从 长度(bg 遍历
        score = sum(1 for y in range(len(puzzle)) if bg_edges[x + y] and puzzle_edges[y])
        if score > best_score:  # 若 score 超过 best_score
            best_score = score  # 把 score 存入 best_score
            best_x = x  # 把 x 存入 best_x
    return best_x  # 返回 best_x


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    bg = [10, 10, 10, 10, 200, 200, 200, 200]  # 把 [10, 10, 10, 10, 200, 200, 200, 200] 存入 bg
    puzzle = [10, 200, 200, 200]  # 把 [10, 200, 200, 200] 存入 puzzle
    print("识别到的缺口横坐标:", recognize_captcha(bg, puzzle))  # 打印输出
