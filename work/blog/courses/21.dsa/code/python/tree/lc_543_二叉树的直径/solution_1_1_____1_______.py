# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145089162
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def diameterOfBinaryTree(root):  # 定义函数 diameterOfBinaryTree（参数：根节点）
    if not root:
        return 0  # 若 not 根节点: return 0
    if not root.left and not root.right:
        return 0  # 若 not 根节点.左边界 and not 根节点.右边界: return 0
    ans = 0  # 把 0 存入 答案

    def depth(node):  # 定义函数 depth（参数：节点）
        if not node:
            return 0  # 若 not 节点: return 0
        leftDepth = depth(node.left)  # 把 深度(节点.左边界) 存入 leftDepth
        rightDepth = depth(node.right)  # 把 深度(节点.右边界) 存入 rightDepth
        ans = max(ans, leftDepth + rightDepth)  # 把 取较大值 答案, leftDepth 加 rightDepth) 存入 答案
        return max(leftDepth, rightDepth) + 1  # 返回 取较大值 leftDepth, rightDepth) 加 1

    depth(root)  # 深度(根节点)
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(diameterOfBinaryTree(None))  # 打印输出
