# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/112548608
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def solve_farmer():  # 定义函数 solve_farmer（参数：无）
    """农夫过河（狼、羊、菜）：状态 (h,w,s,v) 每位 0/1 表示是否在起点岸。
    农夫每次必过河，可单独或带狼/羊/菜之一；无人看管时羊吃菜、狼吃羊则非法。目标全部到达对岸。"""

    def invalid(st):  # 定义函数 invalid（参数：st）
        h, w, s, v = st  # 把 st 写入 h, w, s, v
        if h != s and s == w:  # 若 h 不等于 字符串 and 字符串 等于 权重
            return True  # 返回 True
        if h != s and s == v:  # 若 h 不等于 字符串 and 字符串 等于 值
            return True  # 返回 True
        return False  # 返回 False

    item_index = {"W": 1, "S": 2, "V": 3}  # 把 {'W': 1, 'S': 2, 'V': 3} 存入 item_index
    path = []  # 把 [] 存入 当前路径
    visited = set()  # 把 set() 存入 已访问集合

    def go(st, step):  # 定义函数 go（参数：st, 步数）
        if st == (1, 1, 1, 1):  # 若 st 等于 (1, 1, 1, 1
            return True  # 返回 True
        if st in visited:  # 若 st in 已访问集合
            return False  # 返回 False
        visited.add(st)  # 已访问集合 追加 st)
        h, w, s, v = st  # 把 st 写入 h, w, s, v
        for role in ("-", "W", "S", "V"):  # for role in (' 减 ', 'W', 'S', 'V'):
            ns = list(st)  # 把 列表(st) 存入 ns
            ns[0] = 1 - ns[0]  # 农夫总是过河
            if role != "-":  # 若 role 不等于 ' 减 '
                idx = item_index[role]  # 把 item_index[role] 存入 idx
                # 农夫必须与所带物品在出发前同岸
                if st[0] != st[idx]:  # 若 st[0] 不等于 st[idx]
                    continue  # 跳过本轮，进入下一次
                ns[idx] = 1 - ns[idx]  # 把 1 减 ns[idx] 写入 ns[idx]
            ns = tuple(ns)  # 把 tuple(ns) 存入 ns
            if invalid(ns):  # 若 invalid(ns
                continue  # 跳过本轮，进入下一次
            if go(ns, step + 1):  # 若 go(ns, 步数 加 1
                path.append(role)  # 把 role 追加到列表尾部
                return True  # 返回 True
        return False  # 返回 False

    go((0, 0, 0, 0), 0)  # go((0, 0, 0, 0), 0)
    path.reverse()  # 反转
    return path  # 返回 当前路径


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    plan = solve_farmer()  # 把 solve_farmer() 存入 plan
    # 还原可读方案：H 表示农夫单独过河，其后字母表示带走的角色
    print("农夫过河方案:", " ".join(("H" + (r if r != "-" else "")) for r in plan))  # 打印输出
