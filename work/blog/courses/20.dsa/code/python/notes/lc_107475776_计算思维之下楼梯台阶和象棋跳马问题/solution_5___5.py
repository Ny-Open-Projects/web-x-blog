# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import namedtuple  # from collections import namedtuple

Position = namedtuple("Position", ["x", "y"])  # 把 namedtuple('Position', ['x', 'y']) 存入 Position


def horse_jump_count():  # 定义函数 horse_jump_count（参数：无）
    # 象棋跳马问题（方案5）：用结构(命名元组)表示落点坐标
    moves = [Position(1, 2), Position(2, 1), Position(2, -1), Position(1, -2)]
    count = 0  # 把 0 存入 计数

    def jump(pos):  # 定义函数 jump（参数：pos）
        nonlocal count  # nonlocal 计数
        if pos.x == 8 and pos.y == 4:  # 若 pos.x 等于 8 and pos.y 等于 4
            count += 1  # 计数累加 1
            return  # return
        for mv in moves:  # 逐个取出 moves 的元素（mv）
            nxt = Position(pos.x + mv.x, pos.y + mv.y)  # 把 Position(pos.x 加 mv.x, pos.y 加 mv.y) 存入 nxt
            if (
                nxt.x < 0 or nxt.x > 8 or nxt.y < 0 or nxt.y > 4
            ):  # 若 nxt.x 小于 0 or nxt.x 超过 8 or nxt.y 小于 0 or nxt.y 超过 4
                continue  # 跳过本轮，进入下一次
            jump(nxt)  # jump(nxt)

    jump(Position(0, 0))  # jump(Position(0, 0))
    return count  # 返回 计数


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print("跳马方案总数(0,0)->(8,4):", horse_jump_count())  # 打印输出
