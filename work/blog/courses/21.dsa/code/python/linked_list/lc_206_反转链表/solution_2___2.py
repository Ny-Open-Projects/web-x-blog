# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130510175
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class ListNode:  # 定义类
    def __init__(self, val=0, next=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.next = next  # 把 下一个 写入 下一个


def reverseList(head):  # 定义函数 reverseList（参数：头节点）
    result = None  # 把 None 存入 结果
    while head:  # 循环，直到不满足「头节点」
        temp = head.next  # 把 头节点.下一个 存入 临时变量
        head.next = result  # 把 结果 写入 下一个
        result = head  # 把 头节点 存入 结果
        head = temp  # 把 临时变量 存入 头节点
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    head = ListNode(1, ListNode(2, ListNode(3)))  # 把 ListNode(1, ListNode(2, ListNode(3))) 存入 头节点
    new_head = reverseList(head)  # 把 reverseList(头节点) 存入 new_head
    vals = []  # 把 [] 存入 vals
    while new_head:  # 循环，直到不满足「new_head」
        vals.append(new_head.val)  # 把 new_head.值 追加到列表尾部
        new_head = new_head.next  # 把 new_head.下一个 存入 new_head
    print(vals)  # 打印输出
