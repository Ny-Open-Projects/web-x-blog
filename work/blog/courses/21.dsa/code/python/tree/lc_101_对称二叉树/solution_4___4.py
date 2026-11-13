# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134623793
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isSymmetric(root):  # 定义函数 isSymmetric（参数：根节点）
    if not root or (not root.left and not root.right):
        return True  # 若 not 根节点 or (not 根节点.左边界 and not 根节点.右边界): return True
    queue = [root.left, root.right]  # 把 [根节点.左边界, 根节点.右边界] 存入 队列
    while len(queue):  # 循环，直到不满足「长度(队列」
        left = queue.pop(0)  # 把 队列 弹出 0) 存入 左边界
        right = queue.pop(0)  # 把 队列 弹出 0) 存入 右边界
        if not left and not right:
            continue  # 若 not 左边界 and not 右边界: continue
        if not left or not right:
            return False  # 若 not 左边界 or not 右边界: return False
        if left.val != right.val:
            return False  # 若 左边界.值 不等于 右边界.值: return False
        queue.append(left.left)  # 把 左边界.左边界 追加到列表尾部
        queue.append(right.right)  # 把 右边界.右边界 追加到列表尾部
        queue.append(left.right)  # 把 左边界.右边界 追加到列表尾部
        queue.append(right.left)  # 把 右边界.左边界 追加到列表尾部
    return True  # 返回 True


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isSymmetric(None))  # 打印输出
