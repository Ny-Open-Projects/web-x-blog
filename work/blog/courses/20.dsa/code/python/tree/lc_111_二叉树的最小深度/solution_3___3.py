# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130836270
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minDepth(root):  # 定义函数 minDepth（参数：根节点）
    if not root:
        return 0  # 若 not 根节点: return 0
    if not root.left and not root.right:
        return 1  # 若 not 根节点.左边界 and not 根节点.右边界: return 1
    min_depth = float("inf")  # 把 float('inf') 存入 min_depth
    if root.left:
        min_depth = min(
            minDepth(root.left), min_depth
        )  # 若 根节点.左边界: min_depth 赋值为 取较小值 minDepth(根节点.左边界), min_depth
    if root.right:
        min_depth = min(
            minDepth(root.right), min_depth
        )  # 若 根节点.右边界: min_depth 赋值为 取较小值 minDepth(根节点.右边界), min_depth
    return min_depth + 1  # 返回 min_depth 加 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minDepth(None))  # 打印输出
