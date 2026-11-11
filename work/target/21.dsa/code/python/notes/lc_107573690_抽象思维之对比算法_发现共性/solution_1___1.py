# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107573690
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def climb_stairs_refactored(h):  # 定义函数 climb_stairs_refactored（参数：h）
    # 下楼问题算法重构：用辅助函数隔离"目标/合法性/生成新状态"的差异
    goal = h  # 把 h 存入 goal
    count = 0  # 把 0 存入 计数
    path = []  # 把 [] 存入 当前路径

    def is_done(pos):  # 定义函数 is_done（参数：pos）
        return pos == goal  # 返回 pos 等于 goal

    def is_valid(pos):  # 定义函数 is_valid（参数：pos）
        return 0 <= pos <= goal  # 返回 0 不超过 pos 不超过 goal

    def get_new_pos(pos, k):  # 定义函数 get_new_pos（参数：pos, 下标 k）
        return pos + (k + 1)  # k=0,1,2 -> 步长 1,2,3

    def dfs(pos):  # 定义函数 dfs（参数：pos）
        nonlocal count  # nonlocal 计数
        if is_done(pos):  # 若 is_done(pos
            count += 1  # 计数累加 1
            return  # return
        for k in range(3):  # 让 下标 k 从 3 遍历
            nxt = get_new_pos(pos, k)  # 把 get_new_pos(pos, 下标 k) 存入 nxt
            if not is_valid(nxt):  # 若 not is_valid(nxt
                continue  # 跳过本轮，进入下一次
            path.append(k + 1)  # 把 下标 k 加 1 追加到列表尾部
            dfs(nxt)  # dfs(nxt)
            path.pop()  # 弹出栈顶元素

    dfs(0)  # dfs(0)
    return count  # 返回 计数


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print("重构版下楼方案总数(h=10):", climb_stairs_refactored(10))  # 打印输出
