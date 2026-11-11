# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107573690
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import namedtuple  # from collections import namedtuple

# 通用算法框架：把"判断结束 / 产生新状态 / 判断是否合法"抽象为参数，与或图递归求解
Position = namedtuple("Position", ["x", "y"])  # 把 namedtuple('Position', ['x', 'y']) 存入 Position
MOVES = [Position(1, 2), Position(2, 1), Position(2, -1), Position(1, -2)]
GOAL = Position(8, 4)  # 把 Position(8, 4) 存入 GOAL


def generic_search(start, is_done, is_valid, get_new_pos, n_moves):
    # 通用递归枚举框架：返回从 start 到达目标的方案总数
    count = 0  # 把 0 存入 计数

    def dfs(pos):  # 定义函数 dfs（参数：pos）
        nonlocal count  # nonlocal 计数
        if is_done(pos):  # 若 is_done(pos
            count += 1  # 计数累加 1
            return  # return
        for k in range(n_moves):  # 让 下标 k 从 n_moves 遍历
            nxt = get_new_pos(pos, k)  # 把 get_new_pos(pos, 下标 k) 存入 nxt
            if not is_valid(nxt):  # 若 not is_valid(nxt
                continue  # 跳过本轮，进入下一次
            dfs(nxt)  # dfs(nxt)

    dfs(start)  # dfs(起点)
    return count  # 返回 计数


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    start = Position(0, 0)  # 把 Position(0, 0) 存入 起点
    total = generic_search(
        start,
        is_done=lambda p: p.x == GOAL.x and p.y == GOAL.y,
        is_valid=lambda p: 0 <= p.x <= 8 and 0 <= p.y <= 4,
        get_new_pos=lambda p, k: Position(p.x + MOVES[k].x, p.y + MOVES[k].y),
        n_moves=4,
    )
    print("通用框架求解跳马方案总数:", total)  # 打印输出
