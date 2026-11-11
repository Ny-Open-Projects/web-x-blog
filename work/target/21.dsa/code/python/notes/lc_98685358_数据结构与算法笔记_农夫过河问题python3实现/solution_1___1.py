# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/98685358
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import deque  # from collections import deque

# 角色位置用四元组表示 (农夫, 狼, 羊, 菜)，0=左岸，1=右岸
# 约束：狼和羊不能单独相处；羊和菜不能单独相处（农夫不在同一岸时）
NAMES = ["F", "W", "G", "C"]  # 把 ['F', 'W', 'G', 'C'] 存入 NAMES


def is_safe(state):  # 定义函数 is_safe（参数：state）
    farmer, wolf, goat, cabbage = state  # 把 state 写入 farmer, wolf, goat, cabbage
    if wolf == goat and farmer != wolf:  # 若 wolf 等于 goat and farmer 不等于 wolf
        return False  # 返回 False
    if goat == cabbage and farmer != goat:  # 若 goat 等于 cabbage and farmer 不等于 goat
        return False  # 返回 False
    return True  # 返回 True


def solve():  # 定义函数 solve（参数：无）
    start = (0, 0, 0, 0)  # 把 (0, 0, 0, 0) 存入 起点
    goal = (1, 1, 1, 1)  # 把 (1, 1, 1, 1) 存入 goal
    prev = {start: None}  # 把 {起点: None} 存入 前一个
    q = deque([start])  # 把 deque([起点]) 存入 节点
    while q:  # 循环，直到不满足「节点」
        cur = q.popleft()  # 把 节点.popleft() 存入 当前值
        if cur == goal:  # 若 当前值 等于 goal
            path = [cur]  # 把 [当前值] 存入 当前路径
            while prev[path[-1]] is not None:  # 循环，直到不满足「前一个[当前路径[ 减 1]] is not None」
                path.append(prev[path[-1]])  # 把 前一个[当前路径[ 减 1]] 追加到列表尾部
            return path[::-1]  # 返回 当前路径[:: 减 1]
        farmer = cur[0]  # 把 当前值[0] 存入 farmer
        for i in range(4):  # 让 下标 i 从 4 遍历
            if i != 0 and cur[i] != farmer:  # 若 下标 i 不等于 0 and 当前值[下标 i] 不等于 farmer
                continue  # 跳过本轮，进入下一次
            nxt = list(cur)  # 把 列表(当前值) 存入 nxt
            nxt[0] = 1 - farmer  # 把 1 减 farmer 写入 nxt[0]
            if i != 0:  # 若 下标 i 不等于 0
                nxt[i] = 1 - farmer  # 把 1 减 farmer 写入 nxt[i]
            nxt = tuple(nxt)  # 把 tuple(nxt) 存入 nxt
            if nxt in prev:  # 若 nxt in 前一个
                continue  # 跳过本轮，进入下一次
            if not is_safe(nxt):  # 若 not is_safe(nxt
                continue  # 跳过本轮，进入下一次
            prev[nxt] = cur  # 把 当前值 写入 prev[nxt]
            q.append(nxt)  # 把 nxt 追加到列表尾部
    return None  # 返回 None


if __name__ == "__main__":  # 若 __name__ 等于 「__main__」
    path = solve()  # 把 solve() 存入 当前路径
    if path is None:  # 若 当前路径 is None
        print("无解")  # 打印输出
    else:  # 否则
        for state in path:  # 逐个取出 当前路径 的元素（state）
            print(state, {NAMES[i]: ("L" if v == 0 else "R") for i, v in enumerate(state)})  # 打印输出
