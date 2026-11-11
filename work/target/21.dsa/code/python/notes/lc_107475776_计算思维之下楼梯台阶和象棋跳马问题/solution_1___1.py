# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def climb_stairs(h):  # 定义函数 climb_stairs（参数：h）
    # 下楼梯问题：每步可走 1/2/3 级，递归枚举所有方案并计数（方案1）
    plans = []  # 把 [] 存入 plans
    path = []  # 把 [] 存入 当前路径

    def dfs(remaining):  # 定义函数 dfs（参数：remaining）
        if remaining == 0:  # 若 remaining 等于 0
            plans.append(path[:])  # 把 复制 当前路径 追加到列表尾部
            return  # return
        for step in (3, 2, 1):  # 先尝试大步，与博客一致
            if remaining >= step:  # 若 remaining 不低于 步数
                path.append(step)  # 把 步数 追加到列表尾部
                dfs(remaining - step)  # dfs(remaining 减 步数)
                path.pop()  # 弹出栈顶元素

    dfs(h)  # dfs(h)
    return plans  # 返回 plans


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    h = 6  # 把 6 存入 h
    plans = climb_stairs(h)  # 把 climb_stairs(h) 存入 plans
    print(f"台阶数 {h}，总方案数: {len(plans)}")  # 打印输出
    for i, p in enumerate(plans[:10], 1):  # 同时取 下标 i 与 节点 遍历
        print(f"方案{i}: {p}")  # 打印输出
