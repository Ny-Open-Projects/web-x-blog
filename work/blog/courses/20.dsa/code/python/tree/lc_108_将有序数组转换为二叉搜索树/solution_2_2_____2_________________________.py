# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144993168
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def sortedArrayToBST(nums):  # 定义函数 sortedArrayToBST（参数：数组）
    return helper(nums, 0, len(nums) - 1)  # 返回 helper(数组, 0, 长度(数组) 减 1)


def helper(nums, left, right):  # 定义函数 helper（参数：数组, 左边界, 右边界）
    if left > right:  # 若 左边界 超过 右边界
        return None  # 返回 None
    mid = (left + right + 1) // 2  # 把 (左边界 加 右边界 加 1) 除以 除以 2 存入 中点
    root = TreeNode(nums[mid])  # 把 TreeNode(数组[中点]) 存入 根节点
    root.left = helper(nums, left, mid - 1)  # 把 helper(数组, 左边界, 中点 减 1) 写入 左边界
    root.right = helper(nums, mid + 1, right)  # 把 helper(数组, 中点 加 1, 右边界) 写入 右边界
    return root  # 返回 根节点


def inorder(root):  # 定义函数 inorder（参数：根节点）
    if not root:  # 若 not 根节点
        return []  # 返回 []
    return (
        inorder(root.left) + [root.val] + inorder(root.right)
    )  # 返回 inorder(根节点.左边界) 加 [根节点.值] 加 inorder(根节点.右边界)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    root = sortedArrayToBST([1, 2, 3])  # 把 sortedArrayToBST([1, 2, 3]) 存入 根节点
    print(inorder(root))  # 打印输出
