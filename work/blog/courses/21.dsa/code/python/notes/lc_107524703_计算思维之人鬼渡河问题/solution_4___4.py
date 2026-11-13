# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def solve_with_dir():  # 定义函数 solve_with_dir（参数：无）
    """人鬼渡河（含方向状态的递归版，对应 C++ state{dir,pos}）：
    状态含船行方向 dir(-1 东->西, +1 西->东) 与东岸 (R,G)，移动时按方向加/减决策向量。"""
    D = [(2, 0), (1, 0), (1, 1), (0, 1), (0, 2)]  # 把 [(2, 0), (1, 0), (1, 1), (0, 1), (0, 2)] 存入 D
    start = {"dir": -1, "pos": (3, 3)}  # 把 {'dir': 减 1, 'pos': (3, 3)} 存入 起点
    goal = {"dir": 1, "pos": (0, 0)}  # 把 {'dir': 1, 'pos': (0, 0)} 存入 goal

    def safe(r, g):  # 定义函数 safe（参数：右指针, g）
        return 0 <= r <= 3 and 0 <= g <= 3 and (r == 0 or r == 3 or r == g)

    path = []  # 把 [] 存入 当前路径
    visited = set()  # 把 set() 存入 已访问集合

    def jump(st, step):  # 定义函数 jump（参数：st, 步数）
        if (
            st["pos"] == goal["pos"] and step % 2 == 0
        ):  # 若 st['pos'] 等于 goal['pos'] and 步数 对…取模 2 等于 0
            return True  # 返回 True
        key = (st["pos"], step % 2)  # 把 (st['pos'], 步数 对…取模 2) 存入 key
        if key in visited:  # 若 key in 已访问集合
            return False  # 返回 False
        visited.add(key)  # 已访问集合 追加 key)
        r, g = st["pos"]  # 把 st['pos'] 写入 r, g
        for dr, dg in D:  # for dr, dg in D:
            nr, ng = (
                r + st["dir"] * dr,
                g + st["dir"] * dg,
            )  # 把 右指针 加 st['dir'] 乘 dr, g 加 st['dir'] 乘 dg 写入 nr, ng
            if not safe(nr, ng):  # 若 not safe(nr, ng
                continue  # 跳过本轮，进入下一次
            if jump(
                {"dir": -st["dir"], "pos": (nr, ng)}, step + 1
            ):  # 若 jump({'dir': 减 st['dir'], 'pos': (nr, ng)}, 步数 加 1
                path.append((dr, dg))  # 把 (dr, dg 追加到列表尾部
                return True  # 返回 True
        return False  # 返回 False

    jump(start, 0)  # jump(起点, 0)
    path.reverse()  # 反转
    return path  # 返回 当前路径


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    plan = solve_with_dir()  # 把 solve_with_dir() 存入 plan
    print("人鬼渡河方案(每次上船 人数,鬼数):", plan)  # 打印输出
