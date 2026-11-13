# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130753362
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def postorderTraversal(root):  # 定义函数 postorderTraversal（参数：根节点）
    res = []  # 把 [] 存入 结果
    dump = TreeNode(0)  # 把 TreeNode(0) 存入 dump
    dump.left = root  # 把 根节点 写入 左边界
    cur = dump  # 把 dump 存入 当前值
    while cur:  # 循环，直到不满足「当前值」
        if cur.left:  # 若 当前值.左边界
            pred = cur.left  # 把 当前值.左边界 存入 pred
            while (
                pred.right and pred.right is not cur
            ):  # 循环，直到不满足「pred.右边界 and pred.右边界 is not 当前值」
                pred = pred.right  # 把 pred.右边界 存入 pred
            if not pred.right:  # 若 not pred.右边界
                pred.right = cur  # 把 当前值 写入 右边界
                cur = cur.left  # 把 当前值.左边界 存入 当前值
            else:  # 否则
                rev = []  # 把 [] 存入 rev
                tmp = cur.left  # 把 当前值.左边界 存入 临时变量
                while tmp is not pred:  # 循环，直到不满足「临时变量 is not pred」
                    rev.append(tmp.val)  # 把 临时变量.值 追加到列表尾部
                    tmp = tmp.right  # 把 临时变量.右边界 存入 临时变量
                rev.append(pred.val)  # 把 pred.值 追加到列表尾部
                res.extend(rev[::-1])  # 结果.extend(rev[:: 减 1])
                pred.right = None  # 把 None 写入 右边界
                cur = cur.right  # 把 当前值.右边界 存入 当前值
        else:  # 否则
            cur = cur.right  # 把 当前值.右边界 存入 当前值
    return res  # 返回 结果


def build_tree(vals):  # 定义函数 build_tree（参数：vals）
    if not vals:  # 若 not vals
        return None  # 返回 None
    root = TreeNode(vals[0])  # 把 TreeNode(vals[0]) 存入 根节点
    q = [root]  # 把 [根节点] 存入 节点
    i = 1  # 把 1 存入 下标 i
    while i < len(vals):  # 循环，直到不满足「下标 i 小于 长度(vals」
        node = q.pop(0)  # 把 节点 弹出 0) 存入 节点
        if vals[i] is not None:  # 若 vals[下标 i] is not None
            node.left = TreeNode(vals[i])  # 把 TreeNode(vals[下标 i]) 写入 左边界
            q.append(node.left)  # 把 节点.左边界 追加到列表尾部
        i += 1  # 下标 i累加 1
        if i < len(vals):  # 若 下标 i 小于 长度(vals
            if vals[i] is not None:  # 若 vals[下标 i] is not None
                node.right = TreeNode(vals[i])  # 把 TreeNode(vals[下标 i]) 写入 右边界
                q.append(node.right)  # 把 节点.右边界 追加到列表尾部
            i += 1  # 下标 i累加 1
    return root  # 返回 根节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    root = build_tree([1, None, 2, None, 3])  # 把 build_tree([1, None, 2, None, 3]) 存入 根节点
    print(postorderTraversal(root))  # 打印输出
