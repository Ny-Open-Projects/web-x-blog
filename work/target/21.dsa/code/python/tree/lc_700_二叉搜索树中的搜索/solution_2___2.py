# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091703
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def searchBST(root, val):  # 定义函数 searchBST（参数：根节点, 值）
    while root:  # 循环，直到不满足「根节点」
        if root.val == val:  # 若 根节点.值 等于 值
            return root  # 返回 根节点
        root = (
            root.left if val < root.val else root.right
        )  # 把 根节点.左边界 if 值 小于 根节点.值 else 根节点.右边界 存入 根节点
    return None  # 返回 None


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
    root = build_tree([4, 2, 7, 1, 3])  # 把 build_tree([4, 2, 7, 1, 3]) 存入 根节点
    r = searchBST(root, 2)  # 把 searchBST(根节点, 2) 存入 右指针
    print(r.val if r else None)  # 打印输出
