# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134625776
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def invertTree(root):  # 定义函数 invertTree（参数：根节点）：左右子树递归交换
    if not root:  # 空节点返回
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)  # 交换并递归
    return root  # 返回 根节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(invertTree(None))  # 打印输出
