# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144994166
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isBalanced(root):  # 定义函数 isBalanced（参数：根节点）
    def height(node):  # 定义函数 height（参数：节点）
        if not node:
            return 0  # 若 not 节点: return 0
        leftHeight = height(node.left)  # 把 height(节点.左边界) 存入 leftHeight
        rightHeight = height(node.right)  # 把 height(节点.右边界) 存入 rightHeight
        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1  # 返回 减 1
        return max(leftHeight, rightHeight) + 1  # 返回 取较大值 leftHeight, rightHeight) 加 1

    return height(root) != -1  # 返回 height(根节点) 不等于 减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isBalanced(None))  # 打印输出
