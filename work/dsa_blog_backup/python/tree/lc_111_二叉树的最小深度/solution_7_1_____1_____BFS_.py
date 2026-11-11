# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130836270
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minDepth(root):  # 定义函数 minDepth（参数：根节点）
    if not root:
        return 0  # 若 not 根节点: return 0
    queue = [root]  # 把 [根节点] 存入 队列
    depth = 0  # 把 0 存入 深度
    while len(queue):  # 循环，直到不满足「长度(队列」
        size = len(queue)  # 把 长度(队列) 存入 大小
        depth += 1  # 深度累加 1
        for _ in range(size):  # 让 _ 从 大小 遍历
            node = queue.pop(0)  # 把 队列 弹出 0) 存入 节点
            if not node.left and not node.right:
                return depth  # 若 not 节点.左边界 and not 节点.右边界: return 深度
            if node.left:
                queue.append(node.left)  # 若 节点.左边界: 队列 追加 节点.左边界
            if node.right:
                queue.append(node.right)  # 若 节点.右边界: 队列 追加 节点.右边界
    return depth  # 返回 深度


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minDepth(None))  # 打印输出
