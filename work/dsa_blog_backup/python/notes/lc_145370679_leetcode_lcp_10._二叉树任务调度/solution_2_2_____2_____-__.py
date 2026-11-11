# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
# LeetCode LCP 10. 二叉树任务调度 — Python 版（方案2：深度优先-优化）


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


def dfs(root):  # 返回 [子树总耗时, 子树最小完成时间 max_exec]
    if root is None:  # 空子树
        return [0.0, 0.0]
    left_sum, left_exec = dfs(root.left)  # 左子树的总耗时与最小完成时间
    right_sum, right_exec = dfs(root.right)
    # 当前任务自身必须独占串行跑完；孩子任务两条机器可穿插：
    # 下界取「较慢的一侧」与「两侧工作量均分到两台机器」的较大者
    parallel = (left_sum + right_sum) / 2.0  # 两台机器均摊左右子树总工作量（浮点）
    max_exec = root.val + max(max(left_exec, right_exec), parallel)
    return [left_sum + right_sum + root.val, max_exec]


def minimal_exec_time(root):  # 答案 = 整棵树的最小完成时间
    return dfs(root)[1]


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
