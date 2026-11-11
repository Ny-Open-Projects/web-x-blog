# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxDepth(root):  # 定义函数 maxDepth（参数：根节点）
    dep = 0  # 把 0 存入 dep

    def dfs(n, l):  # 定义函数 dfs（参数：元素个数, 左指针）
        nonlocal dep  # nonlocal dep
        if not n:
            return  # 若 not 元素个数: return
        if not n.left and not n.right:
            dep = max(
                dep, l
            )  # 若 not 元素个数.左边界 and not 元素个数.右边界: dep 赋值为 取较大值 dep, 左指针
        dfs(n.left, l + 1)  # dfs(元素个数.左边界, 左指针 加 1)
        dfs(n.right, l + 1)  # dfs(元素个数.右边界, 左指针 加 1)

    dfs(root, 1)  # dfs(根节点, 1)
    return dep  # 返回 dep


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxDepth(None))  # 打印输出
