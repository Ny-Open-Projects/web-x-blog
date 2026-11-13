# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145052590
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def countNodes(root):  # 定义函数 countNodes（参数：根节点）
    if root == None:
        return 0  # 若 根节点 等于 None: return 0
    return (
        countNodes(root.left) + countNodes(root.right) + 1
    )  # 返回 countNodes(根节点.左边界) 加 countNodes(根节点.右边界) 加 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(countNodes(None))  # 打印输出
