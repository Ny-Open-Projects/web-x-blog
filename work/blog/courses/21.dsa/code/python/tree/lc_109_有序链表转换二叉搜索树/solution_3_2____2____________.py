# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144993713
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortedListToBST(head):  # 定义函数 sortedListToBST（参数：头节点）
    def getLength(head):  # 定义函数 getLength（参数：头节点）
        length = 0  # 把 0 存入 长度
        while head:  # 循环，直到不满足「头节点」
            length += 1  # 长度累加 1
            head = head.next  # 把 头节点.下一个 存入 头节点
        return length  # 返回 长度

    def buildTree(left, right):  # 定义函数 buildTree（参数：左边界, 右边界）
        nonlocal head  # nonlocal 头节点
        if left > right:
            return None  # 若 左边界 超过 右边界: return None
        mid = (left + right + 1) // 2  # 把 (左边界 加 右边界 加 1) 除以 除以 2 存入 中点
        root = TreeNode(0)  # 把 TreeNode(0) 存入 根节点
        root.left = buildTree(left, mid - 1)  # 把 buildTree(左边界, 中点 减 1) 写入 左边界
        if head:  # 若 头节点
            root.val = head.val  # 把 头节点.值 写入 值
            head = head.next  # 把 头节点.下一个 存入 头节点
        root.right = buildTree(mid + 1, right)  # 把 buildTree(中点 加 1, 右边界) 写入 右边界
        return root  # 返回 根节点

    length = getLength(head)  # 把 getLength(头节点) 存入 长度
    return buildTree(0, length - 1)  # 返回 buildTree(0, 长度 减 1)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortedListToBST(None))  # 打印输出
