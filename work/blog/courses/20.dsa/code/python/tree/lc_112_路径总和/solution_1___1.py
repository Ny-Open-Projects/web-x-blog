# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130907819
# LeetCode 112. 路径总和 · 方案1：DFS 累加根到当前节点的和（对齐博客算法）


import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def build_tree(vals):  # 定义函数 build_tree（参数：vals）
    if not vals or vals[0] is None:  # 若 not vals or vals[0] is None
        return None  # 返回 None
    root = TreeNode(vals[0])  # 把 TreeNode(vals[0]) 存入 根节点
    q = [root]  # 把 [根节点] 存入 节点
    i = 1  # 把 1 存入 下标 i
    while q and i < len(vals):  # 循环，直到不满足「节点 and 下标 i 小于 长度(vals」
        node = q.pop(0)  # 把 节点 弹出 0) 存入 节点
        if i < len(vals) and vals[i] is not None:  # 若 下标 i 小于 长度(vals) and vals[下标 i] is not None
            node.left = TreeNode(vals[i])  # 把 TreeNode(vals[下标 i]) 写入 左边界
            q.append(node.left)  # 把 节点.左边界 追加到列表尾部
        i += 1  # 下标 i累加 1
        if i < len(vals) and vals[i] is not None:  # 若 下标 i 小于 长度(vals) and vals[下标 i] is not None
            node.right = TreeNode(vals[i])  # 把 TreeNode(vals[下标 i]) 写入 右边界
            q.append(node.right)  # 把 节点.右边界 追加到列表尾部
        i += 1  # 下标 i累加 1
    return root  # 返回 根节点


def hasPathSum(root, targetSum):  # 定义函数 hasPathSum（参数：根节点, targetSum）
    if not root:  # 若 not 根节点
        return False  # 返回 False
    res = False  # 把 False 存入 结果

    def dfs(n, v):  # 定义函数 dfs（参数：元素个数, 值）
        nonlocal res  # nonlocal 结果
        if not n.left and not n.right:  # 若 not 元素个数.左边界 and not 元素个数.右边界
            if v == targetSum:  # 若 值 等于 targetSum
                res = True  # 把 True 存入 结果
            return  # return
        if n.left:  # 若 元素个数.左边界
            dfs(n.left, v + n.left.val)  # dfs(元素个数.左边界, 值 加 元素个数.左边界.值)
        if n.right:  # 若 元素个数.右边界
            dfs(n.right, v + n.right.val)  # dfs(元素个数.右边界, 值 加 元素个数.右边界.值)

    dfs(root, root.val)  # dfs(根节点, 根节点.值)
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    DEMO = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    cases = [
        (DEMO, 22, True),
        (DEMO, 27, True),
        (DEMO, 18, True),
        (DEMO, 26, True),
        (DEMO, 20, False),
        (DEMO, 1, False),
        ([1], 1, True),
        ([1], 2, False),
        ([], 0, False),
        ([1, 2], 3, True),
        ([1, 2], 1, False),
    ]
    for vals, target, want in cases:  # for vals, 目标值, want in cases:
        got = hasPathSum(build_tree(vals), target)  # 把 hasPathSum(build_tree(vals), 目标值) 存入 got
        assert got == want, (vals, target, got, want)  # 断言校验
    print("PASS")  # 全部用例通过，输出 PASS
