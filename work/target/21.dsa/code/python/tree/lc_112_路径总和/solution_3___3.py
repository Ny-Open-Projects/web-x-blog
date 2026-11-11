# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130907819
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def hasPathSum(root, targetSum):  # 定义函数 hasPathSum（参数：根节点, targetSum）
    if not root:
        return False  # 若 not 根节点: return False
    if not root.left and not root.right:
        return (
            root.val == targetSum
        )  # 若 not 根节点.左边界 and not 根节点.右边界: return 根节点.值 等于 targetSum
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(hasPathSum(None, None))  # 打印输出
