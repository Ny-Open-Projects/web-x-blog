# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxDepth(root):  # 定义函数 maxDepth（参数：根节点）
    if not root:
        return 0  # 若 not 根节点: return 0
    return 1 + max(
        maxDepth(root.left), maxDepth(root.right)
    )  # 返回 1 加 取较大值 maxDepth(根节点.左边界), maxDepth(根节点.右边界))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxDepth(None))  # 打印输出
