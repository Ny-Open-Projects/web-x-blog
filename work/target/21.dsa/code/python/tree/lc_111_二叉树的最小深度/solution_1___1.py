# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130836270
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minDepth(root):  # 定义函数 minDepth（参数：根节点）
    if not root:
        return 0  # 若 not 根节点: return 0
    q = [[root, 1]]  # 把 [[根节点, 1]] 存入 节点
    while len(q):  # 循环，直到不满足「长度(节点」
        [n, l] = q.pop(0)  # 把 节点 弹出 0) 写入 [n, l]
        if not n.left and not n.right:  # 若 not 元素个数.左边界 and not 元素个数.右边界
            return l  # 返回 左指针
        n.left and q.append([n.left, l + 1])  # 把 [元素个数.左边界, 左指针 加 1] 追加到列表尾部
        n.right and q.append([n.right, l + 1])  # 把 [元素个数.右边界,左指针 加 1] 追加到列表尾部


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minDepth(None))  # 打印输出
