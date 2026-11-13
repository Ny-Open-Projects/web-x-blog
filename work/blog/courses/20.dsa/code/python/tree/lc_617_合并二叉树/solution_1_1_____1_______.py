# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145090998
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def mergeTrees(t1, t2):  # 定义函数 mergeTrees（参数：两棵树根节点）：对应位置合并
    if not t1:  # t1 空则取 t2
        return t2
    if not t2:  # t2 空则取 t1
        return t1
    t1.val += t2.val  # 值相加
    t1.left = mergeTrees(t1.left, t2.left)  # 递归合并左子树
    t1.right = mergeTrees(t1.right, t2.right)  # 递归合并右子树
    return t1  # 返回 根节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(mergeTrees(None, None))  # 打印输出
