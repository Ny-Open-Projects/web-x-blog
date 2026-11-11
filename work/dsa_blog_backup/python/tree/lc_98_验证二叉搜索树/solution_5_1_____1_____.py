# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/131631290
# LeetCode 98. 验证二叉搜索树 · 方案5：递归上下界（lower/upper bound）


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


def _check(n, lo, hi):  # 定义函数 _check（参数：元素个数, 左边界, 右边界）
    if not n:  # 若 not 元素个数
        return True  # 返回 True
    if n.val <= lo or n.val >= hi:  # 若 元素个数.值 不超过 左边界 or 元素个数.值 不低于 右边界
        return False  # 返回 False
    return _check(n.left, lo, n.val) and _check(n.right, n.val, hi)


def isValidBST(root):  # 定义函数 isValidBST（参数：根节点）
    return _check(root, float("-inf"), float("inf"))  # 返回 _check(根节点, float(' 减 inf'), float('inf'))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    cases = [
        ([], True),
        ([1], True),
        ([1, 1], False),
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([10, 5, 15, None, None, 6, 20], False),
        ([3, 1, 5, 0, 2, 4, 6, None, None, None, 3], False),
    ]
    for vals, want in cases:  # for vals, want in cases:
        got = isValidBST(build_tree(vals))  # 把 isValidBST(build_tree(vals)) 存入 got
        assert got == want, (vals, got, want)  # 断言校验
    print("PASS")  # 全部用例通过，输出 PASS
