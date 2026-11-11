# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850725
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def rob(root):  # 定义函数 rob（参数：根节点）
    def dfs(node):  # 定义函数 dfs（参数：节点）
        if node == None:
            return [0, 0]  # 若 节点 等于 None: return [0, 0]
        l = dfs(node.left)  # 把 dfs(节点.左边界) 存入 左指针
        r = dfs(node.right)  # 把 dfs(节点.右边界) 存入 右指针
        selected = node.val + l[1] + r[1]  # 把 节点.值 加 左指针[1] 加 右指针[1] 存入 selected
        notSelected = max(l[0], l[1]) + max(
            r[0], r[1]
        )  # 把 取较大值 左指针[0], 左指针[1]) 加 取较大值 右指针[0], 右指针[1]) 存入 notSelected
        return [selected, notSelected]  # 返回 [selected, notSelected]

    rootStatus = dfs(root)  # 把 dfs(根节点) 存入 rootStatus
    return max(rootStatus[0], rootStatus[1])  # 返回 取较大值 rootStatus[0], rootStatus[1])


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(rob(None))  # 打印输出
