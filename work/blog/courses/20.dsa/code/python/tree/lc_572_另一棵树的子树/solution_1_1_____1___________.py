# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145089820
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isSubtree(root, subRoot):  # 定义函数 isSubtree（参数：根节点, subRoot）
    if not root:
        return False  # 若 not 根节点: return False
    return check(root, subRoot) or isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def check(a, b):  # 定义函数 check（参数：数组, b）
    if not a and not b:
        return True  # 若 not 数组 and not b: return True
    if not a or not b:
        return False  # 若 not 数组 or not b: return False
    if a.val == b.val:
        return check(a.left, b.left) and check(a.right, b.right)
    return False  # 返回 False


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isSubtree(None, None))  # 打印输出
