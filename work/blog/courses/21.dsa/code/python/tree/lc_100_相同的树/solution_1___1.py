# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134622591
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isSameTree(p, q):  # 定义函数 isSameTree（参数：节点, 节点）
    if not p and not q:
        return True  # 若 not 节点 and not 节点: return True
    if p.val != q.val:
        return False  # 若 节点.值 不等于 节点.值: return False
    return isSameTree(p.left, q.left) and isSameTree(
        p.right, q.right
    )  # 返回 isSameTree(节点.左边界, 节点.左边界) and isSameTree(节点.右边界, 节点.右边界)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isSameTree(None, None))  # 打印输出
