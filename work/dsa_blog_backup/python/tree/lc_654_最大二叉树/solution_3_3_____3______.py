# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091535
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def constructMaximumBinaryTree(nums):  # 定义函数 constructMaximumBinaryTree（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    if n == 0:  # 若 元素个数 等于 0
        return None  # 返回 None
    stack = []  # 把 [] 存入 栈
    tree = [
        TreeNode(nums[i]) for i in range(n)
    ]  # 把 [TreeNode(数组[下标 i]) for 下标 i in range(元素个数)] 存入 tree
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        while (
            stack and nums[i] > nums[stack[-1]]
        ):  # 循环，直到不满足「栈 and 数组[下标 i] 超过 数组[栈[ 减 1]]」
            tree[i].left = tree[stack[-1]]  # 把 tree[栈[ 减 1]] 写入 左边界
            stack.pop()  # 弹出栈顶元素
        if stack:  # 若 栈
            tree[stack[-1]].right = tree[i]  # 把 tree[下标 i] 写入 右边界
        stack.append(i)  # 把 下标 i 追加到列表尾部
    return tree[stack[0]]  # 返回 tree[栈[0]]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    root = constructMaximumBinaryTree(
        [3, 2, 1, 6, 0, 5]
    )  # 把 constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]) 存入 根节点
    print(root.val if root else None)  # 打印输出
