# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import namedtuple  # from collections import namedtuple

Position = namedtuple("Position", ["x", "y"])  # 把 namedtuple('Position', ['x', 'y']) 存入 Position
MOVES = [Position(1, 2), Position(2, 1), Position(2, -1), Position(1, -2)]
START = Position(0, 0)  # 把 Position(0, 0) 存入 START
GOAL = Position(8, 4)  # 把 Position(8, 4) 存入 GOAL


def is_valid(pos):  # 定义函数 is_valid（参数：pos）
    return 0 <= pos.x <= 8 and 0 <= pos.y <= 4  # 返回 0 不超过 pos.x 不超过 8 and 0 不超过 pos.y 不超过 4


def is_goal(pos):  # 定义函数 is_goal（参数：pos）
    return pos.x == GOAL.x and pos.y == GOAL.y  # 返回 pos.x 等于 GOAL.x and pos.y 等于 GOAL.y


def horse_jump_count():  # 定义函数 horse_jump_count（参数：无）
    # 象棋跳马问题（方案6）：将合法性/终止判断隔离为辅助函数
    count = 0  # 把 0 存入 计数

    def jump(pos):  # 定义函数 jump（参数：pos）
        nonlocal count  # nonlocal 计数
        if is_goal(pos):  # 若 is_goal(pos
            count += 1  # 计数累加 1
            return  # return
        for mv in MOVES:  # 逐个取出 MOVES 的元素（mv）
            nxt = Position(pos.x + mv.x, pos.y + mv.y)  # 把 Position(pos.x 加 mv.x, pos.y 加 mv.y) 存入 nxt
            if not is_valid(nxt):  # 若 not is_valid(nxt
                continue  # 跳过本轮，进入下一次
            jump(nxt)  # jump(nxt)

    jump(START)  # jump(START)
    return count  # 返回 计数


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print("跳马方案总数(0,0)->(8,4):", horse_jump_count())  # 打印输出
