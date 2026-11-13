# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091535
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def constructMaximumBinaryTree(nums):  # 定义函数 constructMaximumBinaryTree（参数：数组）
    if not nums:  # 若 not 数组
        return None  # 返回 None
    idx = 0  # 把 0 存入 idx
    for i in range(len(nums)):  # 让 下标 i 从 长度(数组 遍历
        if nums[i] > nums[idx]:  # 若 数组[下标 i] 超过 数组[idx]
            idx = i  # 把 下标 i 存入 idx
    root = TreeNode(nums[idx])  # 把 TreeNode(数组[idx]) 存入 根节点
    root.left = constructMaximumBinaryTree(
        nums[:idx]
    )  # 把 constructMaximumBinaryTree(数组[:idx]) 写入 左边界
    root.right = constructMaximumBinaryTree(
        nums[idx + 1 :]
    )  # 把 constructMaximumBinaryTree(数组[idx 加 1:]) 写入 右边界
    return root  # 返回 根节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    root = constructMaximumBinaryTree(
        [3, 2, 1, 6, 0, 5]
    )  # 把 constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]) 存入 根节点
    print(root.val if root else None)  # 打印输出
