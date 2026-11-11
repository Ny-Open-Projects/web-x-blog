# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145096505
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def middleNode(head):  # 定义函数 middleNode（参数：头节点）
    slow = head  # 把 头节点 存入 慢指针
    fast = head  # 把 头节点 存入 快指针
    while fast and fast.next:  # 循环，直到不满足「快指针 and 快指针.下一个」
        slow = slow.next  # 把 慢指针.下一个 存入 慢指针
        fast = fast.next.next  # 把 快指针.下一个.下一个 存入 快指针
    return slow  # 返回 慢指针


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(middleNode(None))  # 打印输出
