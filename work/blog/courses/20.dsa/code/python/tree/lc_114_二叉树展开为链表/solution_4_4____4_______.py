# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145007192
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def flatten(root):  # 定义函数 flatten（参数：根节点）
    curr = root  # 把 根节点 存入 当前值
    while curr != None:  # 循环，直到不满足「当前值 不等于 None」
        if curr.left != None:  # 若 当前值.左边界 不等于 None
            next = curr.left  # 把 当前值.左边界 存入 下一个
            predecessor = next  # 把 下一个 存入 predecessor
            while predecessor.right != None:  # 循环，直到不满足「predecessor.右边界 不等于 None」
                predecessor = predecessor.right  # 把 predecessor.右边界 存入 predecessor
            predecessor.right = curr.right  # 把 当前值.右边界 写入 右边界
            curr.left = None  # 把 None 写入 左边界
            curr.right = next  # 把 下一个 写入 右边界
        curr = curr.right  # 把 当前值.右边界 存入 当前值


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(flatten(None))  # 打印输出
