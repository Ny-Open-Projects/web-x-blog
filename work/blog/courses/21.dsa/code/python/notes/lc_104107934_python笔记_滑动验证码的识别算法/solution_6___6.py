# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def build_synthetic(bg_len=8, gap_start=3, puzzle_len=4):
    """构造合成数据：背景在前段为低灰度、缺口处出现高灰度跳变，拼图即从缺口处截取的片段。"""
    bg = [10] * bg_len  # 把 [10] 乘 bg_len 存入 bg
    for i in range(
        gap_start, min(gap_start + puzzle_len, bg_len)
    ):  # 让 下标 i 从 gap_start 到 取较小值 gap_start 加 puzzle_len 到 bg_len 遍历
        bg[i] = 200  # 把 200 写入 bg[i]
    puzzle = bg[gap_start : gap_start + puzzle_len]  # 把 bg[gap_start:gap_start 加 puzzle_len] 存入 puzzle
    return bg, puzzle  # 返回 bg, puzzle


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    bg, puzzle = build_synthetic()  # 把 build_synthetic() 写入 bg, puzzle
    print("背景:", bg)  # 打印输出
    print("拼图:", puzzle)  # 打印输出
    print("拼图长度:", len(puzzle), " 背景长度:", len(bg))  # 打印输出
