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


def recognize_captcha(bg, puzzle):  # 定义函数 recognize_captcha（参数：bg, puzzle）
    bg_edges = detect_edges(bg)  # 把 detect_edges(bg) 存入 bg_edges
    puzzle_edges = detect_edges(puzzle)  # 把 detect_edges(puzzle) 存入 puzzle_edges
    best_x, best_score = 0, -1  # 把 0, 减 1 写入 best_x, best_score
    for x in range(len(bg) - len(puzzle) + 1):  # 让 x 从 长度(bg 遍历
        score = sum(1 for y in range(len(puzzle)) if bg_edges[x + y] and puzzle_edges[y])
        if score > best_score:  # 若 score 超过 best_score
            best_score = score  # 把 score 存入 best_score
            best_x = x  # 把 x 存入 best_x
    return best_x  # 返回 best_x


def build_synthetic(bg_len=8, gap_start=3, puzzle_len=4):
    bg = [10] * bg_len  # 把 [10] 乘 bg_len 存入 bg
    for i in range(
        gap_start, min(gap_start + puzzle_len, bg_len)
    ):  # 让 下标 i 从 gap_start 到 取较小值 gap_start 加 puzzle_len 到 bg_len 遍历
        bg[i] = 200  # 把 200 写入 bg[i]
    puzzle = bg[gap_start : gap_start + puzzle_len]  # 把 bg[gap_start:gap_start 加 puzzle_len] 存入 puzzle
    return bg, puzzle  # 返回 bg, puzzle


def full_pipeline(bg_len=8, gap_start=3, puzzle_len=4):
    """完整识别流水线：构造合成数据 -> 边缘检测 -> 模板匹配 -> 输出缺口位置。"""
    bg, puzzle = build_synthetic(bg_len, gap_start, puzzle_len)
    pred = recognize_captcha(bg, puzzle)  # 把 recognize_captcha(bg, puzzle) 存入 pred
    return {"background": bg, "puzzle": puzzle, "predicted_gap": pred}


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    result = full_pipeline()  # 把 full_pipeline() 存入 结果
    print("背景:", result["background"])  # 打印输出
    print("拼图:", result["puzzle"])  # 打印输出
    print("识别缺口位置:", result["predicted_gap"])  # 打印输出
