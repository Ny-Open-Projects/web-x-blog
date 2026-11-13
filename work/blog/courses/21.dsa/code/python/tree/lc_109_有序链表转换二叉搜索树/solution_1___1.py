# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144993713
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortedListToBST(head):  # 定义函数 sortedListToBST（参数：头节点）
    if not head:
        return None  # 若 not 头节点: return None
    nodes = []  # 把 [] 存入 nodes
    while head:  # 循环，直到不满足「头节点」
        nodes.append(head)  # 把 头节点 追加到列表尾部
        head = head.next  # 把 头节点.下一个 存入 头节点

    def build(left, right):  # 定义函数 build（参数：左边界, 右边界）
        if left > right:
            return None  # 若 左边界 超过 右边界: return None
        mid = (left + right) // 2  # 把 (左边界 加 右边界) 除以 除以 2 存入 中点
        root = TreeNode(nodes[mid].val)  # 把 TreeNode(nodes[中点].值) 存入 根节点
        root.left = build(left, mid - 1)  # 把 build(左边界, 中点 减 1) 写入 左边界
        root.right = build(mid + 1, right)  # 把 build(中点 加 1, 右边界) 写入 右边界
        return root  # 返回 根节点

    return build(0, len(nodes) - 1)  # 返回 build(0, 长度(nodes) 减 1)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortedListToBST(None))  # 打印输出
