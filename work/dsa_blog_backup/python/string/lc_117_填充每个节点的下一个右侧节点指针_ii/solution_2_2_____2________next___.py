# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386298
# LeetCode 117. 填充每个节点的下一个右侧节点指针 II · 方案2：使用已建立的 next 指针


import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class Node:  # 定义类
    def __init__(self, val=0, left=None, right=None, next=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界
        self.next = next  # 把 下一个 写入 下一个


def build_node(vals):  # 定义函数 build_node（参数：vals）
    if not vals or vals[0] is None:  # 若 not vals or vals[0] is None
        return None  # 返回 None
    root = Node(vals[0])  # 把 Node(vals[0]) 存入 根节点
    q = [root]  # 把 [根节点] 存入 节点
    i = 1  # 把 1 存入 下标 i
    while q and i < len(vals):  # 循环，直到不满足「节点 and 下标 i 小于 长度(vals」
        node = q.pop(0)  # 把 节点 弹出 0) 存入 节点
        if i < len(vals) and vals[i] is not None:  # 若 下标 i 小于 长度(vals) and vals[下标 i] is not None
            node.left = Node(vals[i])  # 把 Node(vals[下标 i]) 写入 左边界
            q.append(node.left)  # 把 节点.左边界 追加到列表尾部
        i += 1  # 下标 i累加 1
        if i < len(vals) and vals[i] is not None:  # 若 下标 i 小于 长度(vals) and vals[下标 i] is not None
            node.right = Node(vals[i])  # 把 Node(vals[下标 i]) 写入 右边界
            q.append(node.right)  # 把 节点.右边界 追加到列表尾部
        i += 1  # 下标 i累加 1
    return root  # 返回 根节点


def connect(root):  # 定义函数 connect（参数：根节点）
    if not root:  # 若 not 根节点
        return None  # 返回 None
    leftmost = root  # 把 根节点 存入 leftmost
    while leftmost:  # 循环，直到不满足「leftmost」
        cur = leftmost  # 把 leftmost 存入 当前值
        next_start = None  # 把 None 存入 next_start
        prev = None  # 把 None 存入 前一个
        while cur:  # 循环，直到不满足「当前值」
            for ch in (cur.left, cur.right):  # for 字符 in (当前值.左边界, 当前值.右边界):
                if ch:  # 若 字符
                    if prev is None:  # 若 前一个 is None
                        next_start = ch  # 把 字符 存入 next_start
                    else:  # 否则
                        prev.next = ch  # 把 字符 写入 下一个
                    prev = ch  # 把 字符 存入 前一个
            cur = cur.next  # 把 当前值.下一个 存入 当前值
        leftmost = next_start  # 把 next_start 存入 leftmost
    return root  # 返回 根节点


def collect_levels(root):  # 定义函数 collect_levels（参数：根节点）
    res = []  # 把 [] 存入 结果
    leftmost = root  # 把 根节点 存入 leftmost
    while leftmost:  # 循环，直到不满足「leftmost」
        level = []  # 把 [] 存入 level
        cur = leftmost  # 把 leftmost 存入 当前值
        while cur:  # 循环，直到不满足「当前值」
            level.append(cur.val)  # 把 当前值.值 追加到列表尾部
            cur = cur.next  # 把 当前值.下一个 存入 当前值
        res.append(level)  # 把 level 追加到列表尾部
        leftmost = leftmost.left  # 把 leftmost.左边界 存入 leftmost
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    root = build_node([1, 2, 3, 4, 5, None, 7])  # 把 build_node([1, 2, 3, 4, 5, None, 7]) 存入 根节点
    connect(root)  # connect(根节点)
    got = collect_levels(root)  # 把 collect_levels(根节点) 存入 got
    want = [[1], [2, 3], [4, 5, 7]]  # 把 [[1], [2, 3], [4, 5, 7]] 存入 want
    assert got == want, (got, want)  # 断言校验
    assert connect(None) is None  # 断言校验
    single = Node(9)  # 把 Node(9) 存入 single
    connect(single)  # connect(single)
    assert collect_levels(single) == [[9]]  # 断言校验
    print("PASS")  # 全部用例通过，输出 PASS
