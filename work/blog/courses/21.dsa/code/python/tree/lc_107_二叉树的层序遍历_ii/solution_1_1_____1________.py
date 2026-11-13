# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144992608
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def levelOrderBottom(root):  # 定义函数 levelOrderBottom（参数：根节点）
    levelOrder = []  # 把 [] 存入 levelOrder
    if root == None:
        return levelOrder  # 若 根节点 等于 None: return levelOrder
    queue = [root]  # 把 [根节点] 存入 队列
    while len(queue) > 0:  # 循环，直到不满足「长度(队列) 超过 0」
        level = []  # 把 [] 存入 level
        size = len(queue)  # 把 长度(队列) 存入 大小
        for i in range(size):  # 让 下标 i 从 大小 遍历
            node = queue.pop(0)  # 把 队列 弹出 0) 存入 节点
            level.append(node.val)  # 把 节点.值 追加到列表尾部
            if node.left != None:
                queue.append(node.left)  # 若 节点.左边界 不等于 None: 队列 追加 节点.左边界
            if node.right != None:
                queue.append(node.right)  # 若 节点.右边界 不等于 None: 队列 追加 节点.右边界
        levelOrder.insert(0, level)  # levelOrder 插入 0, level)
    return levelOrder  # 返回 levelOrder


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(levelOrderBottom(None))  # 打印输出
