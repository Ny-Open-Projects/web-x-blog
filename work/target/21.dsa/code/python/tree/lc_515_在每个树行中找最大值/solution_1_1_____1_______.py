# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145088842
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def largestValues(root):  # 定义函数 largestValues（参数：根节点）
    if not root:
        return []  # 若 not 根节点: return []
    res = []  # 把 [] 存入 结果

    def dfs(res, root, curHeight):  # 定义函数 dfs（参数：结果, 根节点, curHeight）
        if curHeight == len(res):  # 若 curHeight 等于 长度(结果
            res.append(root.val)  # 把 根节点.值 追加到列表尾部
        else:  # 否则
            res.splice(
                curHeight, 1, max(res[curHeight], root.val)
            )  # 结果.splice(curHeight, 1, 取较大值 结果[curHeight], 根节点.值))
        if root.left:  # 若 根节点.左边界
            dfs(res, root.left, curHeight + 1)  # dfs(结果, 根节点.左边界, curHeight 加 1)
        if root.right:  # 若 根节点.右边界
            dfs(res, root.right, curHeight + 1)  # dfs(结果, 根节点.右边界, curHeight 加 1)

    dfs(res, root, 0)  # dfs(结果, 根节点, 0)
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(largestValues(None))  # 打印输出
