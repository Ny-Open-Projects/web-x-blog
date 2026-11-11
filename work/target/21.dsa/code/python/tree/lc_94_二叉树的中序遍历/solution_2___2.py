# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130743564
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def inorderTraversal(root):  # 定义函数 inorderTraversal（参数：根节点）
    result = []  # 把 [] 存入 结果

    def dfs(node):  # 定义函数 dfs（参数：节点）
        pass  # pass
        if not node:
            return  # 若 not 节点: return
        dfs(node.left)  # dfs(节点.左边界)
        result.append(node.val)  # 把 节点.值 追加到列表尾部
        dfs(node.right)  # dfs(节点.右边界)

    dfs(root)  # dfs(根节点)
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(inorderTraversal(None))  # 打印输出
