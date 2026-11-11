# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130907819
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def hasPathSum(root, targetSum):  # 定义函数 hasPathSum（参数：根节点, targetSum）
    if not root:
        return False  # 若 not 根节点: return False
    q = [[root, root.val]]  # 把 [[根节点, 根节点.值]] 存入 节点
    while len(q):  # 循环，直到不满足「长度(节点」
        first = q.pop(0)  # 把 节点 弹出 0) 存入 first
        [n, v] = first  # 把 first 写入 [n, v]
        if not n.left and not n.right and v == targetSum:
            return True
        if n.left:
            q.append(
                [n.left, v + n.left.val]
            )  # 若 元素个数.左边界: 节点 追加 [元素个数.左边界, 值 加 元素个数.左边界.值]
        if n.right:
            q.append(
                [n.right, v + n.right.val]
            )  # 若 元素个数.右边界: 节点 追加 [元素个数.右边界, 值 加 元素个数.右边界.值]
    return False  # 返回 False


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(hasPathSum(None, None))  # 打印输出
