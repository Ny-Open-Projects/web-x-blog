# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145089162
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def diameterOfBinaryTree(root):  # 定义函数 diameterOfBinaryTree（参数：根节点）
    len = 0  # 把 0 存入 长度

    def dfs(root):  # 定义函数 dfs（参数：根节点）
        pass  # pass
        if not root:
            return 0  # 若 not 根节点: return 0
        left = dfs(root.left)  # 把 dfs(根节点.左边界) 存入 左边界
        right = dfs(root.right)  # 把 dfs(根节点.右边界) 存入 右边界
        len = max(len, left + right)  # 把 取较大值 长度,左边界 加 右边界) 存入 长度
        return max(left, right) + 1  # 返回 取较大值 左边界,右边界) 加 1

    dfs(root)  # dfs(根节点)
    return len  # 返回 长度


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(diameterOfBinaryTree(None))  # 打印输出
