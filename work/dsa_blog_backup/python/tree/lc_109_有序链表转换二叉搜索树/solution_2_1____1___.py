# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144993713
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortedListToBST(head):  # 定义函数 sortedListToBST（参数：头节点）
    def getMedian(left, right):  # 定义函数 getMedian（参数：左边界, 右边界）
        fast = left  # 把 左边界 存入 快指针
        slow = left  # 把 左边界 存入 慢指针
        while (
            fast != right and fast.next != right
        ):  # 循环，直到不满足「快指针 不等于 右边界 and 快指针.下一个 不等于 右边界」
            fast = fast.next.next  # 把 快指针.下一个.下一个 存入 快指针
            slow = slow.next  # 把 慢指针.下一个 存入 慢指针
        return slow  # 返回 慢指针

    def buildTree(left, right):  # 定义函数 buildTree（参数：左边界, 右边界）
        if left == right:
            return None  # 若 左边界 等于 右边界: return None
        mid = getMedian(left, right)  # 把 getMedian(左边界, 右边界) 存入 中点
        root = TreeNode(mid.val)  # 把 TreeNode(中点.值) 存入 根节点
        root.left = buildTree(left, mid)  # 把 buildTree(左边界, 中点) 写入 左边界
        root.right = buildTree(mid.next, right)  # 把 buildTree(中点.下一个, 右边界) 写入 右边界
        return root  # 返回 根节点

    return buildTree(head, None)  # 返回 buildTree(头节点, None)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortedListToBST(None))  # 打印输出
