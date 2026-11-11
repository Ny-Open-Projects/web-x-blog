# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134625776
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def invertTree(root):  # 定义函数 invertTree（参数：根节点）
    if not root:
        return None  # 若 not 根节点: return None
    queue = [root]  # 把 [根节点] 存入 队列
    while len(queue):  # 循环，直到不满足「长度(队列」
        qTop = queue.pop(0)  # 把 队列 弹出 0) 存入 qTop
        [qTop.left, qTop.right] = [
            qTop.right,
            qTop.left,
        ]  # 把 [qTop.右边界, qTop.左边界] 写入 [qTop.left, qTop.right]
        if qTop.left:
            queue.append(qTop.left)  # 若 qTop.左边界: 队列 追加 qTop.左边界
        if qTop.right:
            queue.append(qTop.right)  # 若 qTop.右边界: 队列 追加 qTop.右边界
    return root  # 返回 根节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(invertTree(None))  # 打印输出
