# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144992608
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def dfs(node, level, levels):  # 定义函数 dfs（参数：节点, level, levels）
    if node == None:
        return  # 若 节点 等于 None: return
    if level == len(levels):
        levels.append([])  # 若 level 等于 长度(levels): levels 追加 []
    levels[level].append(node.val)  # 把 节点.值 追加到列表尾部
    dfs(node.left, level + 1, levels)  # dfs(节点.左边界, level 加 1, levels)
    dfs(node.right, level + 1, levels)  # dfs(节点.右边界, level 加 1, levels)


def levelOrderBottom(root):  # 定义函数 levelOrderBottom（参数：根节点）
    levels = []  # 把 [] 存入 levels
    dfs(root, 0, levels)  # dfs(根节点, 0, levels)
    return levels.reverse()  # 返回 levels.reverse()


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(dfs(None, None, None))  # 打印输出
