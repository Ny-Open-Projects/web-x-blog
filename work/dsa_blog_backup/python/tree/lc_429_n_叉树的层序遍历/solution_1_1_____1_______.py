# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145088458
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def levelOrder(root):  # 定义函数 levelOrder（参数：N 叉树根节点）
    if not root:  # 空树返回
        return []
    res = []  # 结果
    q = [root]  # 队列
    while q:  # 逐层处理
        level = []  # 当前层值
        nxt = []  # 下一层节点
        for node in q:  # 遍历当前层
            level.append(node.val)
            for child in (node.children or []):  # 子节点入下一层
                nxt.append(child)
        res.append(level)
        q = nxt
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(levelOrder(None))  # 打印输出
