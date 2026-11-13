# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130514894
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def hasCycle(head):  # 定义函数 hasCycle（参数：头节点）
    p1 = head  # 把 头节点 存入 p1
    p2 = head  # 把 头节点 存入 p2
    while p1 and p2.next:  # 循环，直到不满足「p1 and p2.下一个」
        p1 = p1.next  # 把 p1.下一个 存入 p1
        p2 = p2.next.next  # 把 p2.下一个.下一个 存入 p2
        if p1 == p2:  # 若 p1 等于 p2
            return True  # 返回 True
    return False  # 返回 False


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(hasCycle(None))  # 打印输出
