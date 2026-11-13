# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145084192
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sumOfLeftLeaves(root):  # 定义函数 sumOfLeftLeaves（参数：根节点）
    leftSum = 0  # 把 0 存入 leftSum

    def travese(node):  # 定义函数 travese（参数：节点）
        pass  # pass
        if not node:
            return  # 若 not 节点: return
        left = node.left  # 把 节点.左边界 存入 左边界
        if left and not left.left and not left.right:  # 若 左边界 and not 左边界.左边界 and not 左边界.右边界
            leftSum += left.val  # leftSum累加 左边界.值
        travese(node.left)  # travese(节点.左边界)
        travese(node.right)  # travese(节点.右边界)

    travese(root)  # travese(根节点)
    return leftSum  # 返回 leftSum


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sumOfLeftLeaves(None))  # 打印输出
