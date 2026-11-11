# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
# LeetCode LCP 10. 二叉树任务调度 — Python 版（方案1：深度优先-贪心）


import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 二叉树节点：val 为自身执行时间
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals):  # 层序数组建树，None 表示空节点
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]  # 队列里只放非空节点
    i = 1
    while queue and i < len(vals):
        node = queue.pop(0)  # 出队一个父节点
        if i < len(vals) and vals[i] is not None:  # 左孩子
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:  # 右孩子
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


def dfs(root):  # 返回 [子树总耗时, 两台机器并行可节省的耗时]
    if root is None:  # 空子树：总耗时 0，节省 0
        return [0.0, 0.0]
    a, b = dfs(root.left)  # a: 左子树总耗时, b: 左子树已节省
    c, d = dfs(root.right)  # c: 右子树总耗时, d: 右子树已节省
    if (c - 2 * d <= a and a <= c) or (a - 2 * b <= c and c <= a):
        # 一侧的串行下界落在另一侧的耗时区间内：两台机器互相填空，左右几乎完全并行
        saved = (a + c) / 2.0  # 浮点除法：总和为奇数时会出现 0.5
    elif a - 2 * b > c:
        # 左子树串行段太长：右子树整体塞进左边空闲的那台机器
        saved = b + c
    else:
        # 右子树占主导：左子树整体塞进右边空闲的那台机器
        saved = a + d
    return [a + c + root.val, saved]  # 加上当前节点自身的执行时间


def minimal_exec_time(root):  # 答案 = 子树总和 - 并行节省
    total, saved = dfs(root)
    return total - saved


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    cases = [  # 三个官方用例
        ([47, 74, 31], 121.0),
        ([15, 21, None, 24, None, 27, 26], 87.0),
        ([1, 3, 2, None, None, 4, 4], 7.5),
    ]
    ok = True
    for vals, want in cases:
        got = minimal_exec_time(build_tree(vals))
        if abs(got - want) >= 1e-6:  # 浮点比较用 1e-6 容差
            print("FAIL", vals, "got", got, "want", want)  # 失败打印 FAIL
            ok = False
    if not ok:
        raise SystemExit(1)  # 非零退出
    print("PASS")  # 全部用例通过，输出 PASS
