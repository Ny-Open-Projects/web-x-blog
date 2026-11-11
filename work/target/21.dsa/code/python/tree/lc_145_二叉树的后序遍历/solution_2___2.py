# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130753362
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def postorderTraversal(root):  # 定义函数 postorderTraversal（参数：根节点）
    res = []  # 结果

    def dfs(node):  # 递归：左 → 右 → 根
        if not node:  # 空节点返回
            return
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)

    dfs(root)
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(postorderTraversal(None))  # 打印输出
