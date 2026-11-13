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


def find_gap(bg, puzzle):  # 定义函数 find_gap（参数：bg, puzzle）
    """通过背景边缘响应最强处定位缺口：统计各候选起点处与拼图边缘的重合度，返回最佳横坐标。"""
    bg_edges = detect_edges(bg)  # 把 detect_edges(bg) 存入 bg_edges
    puzzle_edges = detect_edges(puzzle)  # 把 detect_edges(puzzle) 存入 puzzle_edges
    responses = []  # 把 [] 存入 responses
    for x in range(len(bg) - len(puzzle) + 1):  # 让 x 从 长度(bg 遍历
        score = sum(1 for y in range(len(puzzle)) if bg_edges[x + y] and puzzle_edges[y])
        responses.append(score)  # 把 score 追加到列表尾部
    best_x = max(range(len(responses)), key=lambda i: responses[i])
    return best_x, responses  # 返回 best_x, responses


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    bg = [10, 10, 10, 10, 200, 200, 200, 200]  # 把 [10, 10, 10, 10, 200, 200, 200, 200] 存入 bg
    puzzle = [10, 200, 200, 200]  # 把 [10, 200, 200, 200] 存入 puzzle
    x, responses = find_gap(bg, puzzle)  # 把 find_gap(bg, puzzle) 写入 x, responses
    print("缺口横坐标:", x)  # 打印输出
    print("各位置响应:", responses)  # 打印输出
