# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134623793
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isSymmetric(root):  # 定义函数 isSymmetric（参数：根节点）
    if not root:
        return True  # 若 not 根节点: return True

    def isMirror(l, r):  # 定义函数 isMirror（参数：左指针, 右指针）
        if not l and not r:
            return True  # 若 not 左指针 and not 右指针: return True
        return l.val == r.val and isMirror(l.left, r.right) and isMirror(r.left, l.right)

    return isMirror(root.left, root.right)  # 返回 isMirror(根节点.左边界, 根节点.右边界)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isSymmetric(None))  # 打印输出
