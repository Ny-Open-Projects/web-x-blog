# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def solve_iterative():  # 定义函数 solve_iterative（参数：无）
    """人鬼渡河（迭代回溯版，对应 C++ transfer_state）：
    状态为东岸 (R,G)，每一步按方向（奇步东->西，偶步西->东）套用 5 种摆渡决策，
    用 visited 防止重复状态，找到第一个到达 (0,0) 的方案。"""
    D = [(2, 0), (1, 0), (1, 1), (0, 1), (0, 2)]  # 把 [(2, 0), (1, 0), (1, 1), (0, 1), (0, 2)] 存入 D
    start, goal = (3, 3), (0, 0)  # 把 (3, 3), (0, 0) 写入 start, goal

    def safe(r, g):  # 定义函数 safe（参数：右指针, g）
        return 0 <= r <= 3 and 0 <= g <= 3 and (r == 0 or r == 3 or r == g)

    path = []  # 把 [] 存入 当前路径
    visited = set()  # 把 set() 存入 已访问集合

    def dfs(state, step):  # 定义函数 dfs（参数：state, 步数）
        if state == goal:  # 若 state 等于 goal
            return True  # 返回 True
        key = (state, step % 2)  # 把 (state, 步数 对…取模 2) 存入 key
        if key in visited:  # 若 key in 已访问集合
            return False  # 返回 False
        visited.add(key)  # 已访问集合 追加 key)
        r, g = state  # 把 state 写入 r, g
        odd = step % 2 == 1  # 奇步：东->西（减法）
        for dr, dg in D:  # for dr, dg in D:
            if odd:  # 若 odd
                if r < dr or g < dg:  # 若 右指针 小于 dr or g 小于 dg
                    continue  # 跳过本轮，进入下一次
                nr, ng = r - dr, g - dg  # 把 右指针 减 dr, g 减 dg 写入 nr, ng
            else:  # 否则
                if (3 - r) < dr or (3 - g) < dg:  # 若 3 减 右指针) 小于 dr or (3 减 g) 小于 dg
                    continue  # 跳过本轮，进入下一次
                nr, ng = r + dr, g + dg  # 把 右指针 加 dr, g 加 dg 写入 nr, ng
            if not safe(nr, ng):  # 若 not safe(nr, ng
                continue  # 跳过本轮，进入下一次
            if dfs((nr, ng), step + 1):  # 若 dfs((nr, ng), 步数 加 1
                path.append((dr, dg))  # 把 (dr, dg 追加到列表尾部
                return True  # 返回 True
        return False  # 返回 False

    dfs(start, 1)  # dfs(起点, 1)
    path.reverse()  # 反转
    return path  # 返回 当前路径


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    plan = solve_iterative()  # 把 solve_iterative() 存入 plan
    print("人鬼渡河方案(每次上船 人数,鬼数):", plan)  # 打印输出
    print("总步数:", len(plan))  # 打印输出
