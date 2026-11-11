# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107573690
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import namedtuple  # from collections import namedtuple

Position = namedtuple("Position", ["x", "y"])  # 把 namedtuple('Position', ['x', 'y']) 存入 Position
MOVES = [Position(1, 2), Position(2, 1), Position(2, -1), Position(1, -2)]
GOAL = Position(8, 4)  # 把 Position(8, 4) 存入 GOAL


def horse_jump_refactored():  # 定义函数 horse_jump_refactored（参数：无）
    # 跳马问题算法重构：与下楼共用同一套递归框架，仅差异部分由辅助函数隔离
    count = 0  # 把 0 存入 计数

    def is_done(pos):  # 定义函数 is_done（参数：pos）
        return pos.x == GOAL.x and pos.y == GOAL.y  # 返回 pos.x 等于 GOAL.x and pos.y 等于 GOAL.y

    def is_valid(pos):  # 定义函数 is_valid（参数：pos）
        return 0 <= pos.x <= 8 and 0 <= pos.y <= 4  # 返回 0 不超过 pos.x 不超过 8 and 0 不超过 pos.y 不超过 4

    def get_new_pos(pos, k):  # 定义函数 get_new_pos（参数：pos, 下标 k）
        return Position(
            pos.x + MOVES[k].x, pos.y + MOVES[k].y
        )  # 返回 Position(pos.x 加 MOVES[下标 k].x, pos.y 加 MOVES[下标 k].y)

    def dfs(pos):  # 定义函数 dfs（参数：pos）
        nonlocal count  # nonlocal 计数
        if is_done(pos):  # 若 is_done(pos
            count += 1  # 计数累加 1
            return  # return
        for k in range(4):  # 让 下标 k 从 4 遍历
            nxt = get_new_pos(pos, k)  # 把 get_new_pos(pos, 下标 k) 存入 nxt
            if not is_valid(nxt):  # 若 not is_valid(nxt
                continue  # 跳过本轮，进入下一次
            dfs(nxt)  # dfs(nxt)

    dfs(Position(0, 0))  # dfs(Position(0, 0))
    return count  # 返回 计数


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print("重构版跳马方案总数(0,0)->(8,4):", horse_jump_refactored())  # 打印输出
