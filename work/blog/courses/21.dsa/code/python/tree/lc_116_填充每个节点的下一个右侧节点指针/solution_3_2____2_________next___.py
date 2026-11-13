# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386215
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def connect(root):  # 定义函数 connect（参数：根节点）
    if root == None:
        return root  # 若 根节点 等于 None: return 根节点
    leftmost  # leftmost
    while (
        leftmost != None and leftmost.left != None
    ):  # 循环，直到不满足「leftmost 不等于 None and leftmost.左边界 不等于 None」
        node  # 节点
        while node:  # 循环，直到不满足「节点」
            if node.left and node.right:  # 若 节点.左边界 and 节点.右边界
                node.left.next = node.right  # 把 节点.右边界 写入 下一个
            if (
                node.right and node.next and node.next.left
            ):  # 若 节点.右边界 and 节点.下一个 and 节点.下一个.左边界
                node.right.next = node.next.left  # 把 节点.下一个.左边界 写入 下一个
            node = node.next  # 把 节点.下一个 存入 节点
        leftmost = leftmost.left  # 把 leftmost.左边界 存入 leftmost
    return root  # 返回 根节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(connect(None))  # 打印输出
