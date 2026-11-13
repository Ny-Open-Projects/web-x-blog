# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144993713
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortedListToBST(head):  # 定义函数 sortedListToBST（参数：头节点）
    def travese(head, tail):  # 定义函数 travese（参数：头节点, 尾节点）
        if head == tail:
            return None  # 若 头节点 等于 尾节点: return None
        fast = head  # 把 头节点 存入 快指针
        slow = head  # 把 头节点 存入 慢指针
        while (
            fast != tail and fast.next != tail
        ):  # 循环，直到不满足「快指针 不等于 尾节点 and 快指针.下一个 不等于 尾节点」
            slow = slow.next  # 把 慢指针.下一个 存入 慢指针
            fast = fast.next.next  # 把 快指针.下一个.下一个 存入 快指针
        root = TreeNode(slow.val)  # 把 TreeNode(慢指针.值) 存入 根节点
        root.left = travese(head, slow)  # 把 travese(头节点,慢指针) 写入 左边界
        root.right = travese(slow.next, tail)  # 把 travese(慢指针.下一个,尾节点) 写入 右边界
        return root  # 返回 根节点

    return travese(head, None)  # 返回 travese(头节点, None)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortedListToBST(None))  # 打印输出
