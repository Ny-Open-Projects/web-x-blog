# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386298
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def connect(root):  # 定义函数 connect（参数：根节点）：next 指针逐层串联
    if not root:  # 若 not 根节点
        return None  # 返回 None
    head = root  # 每层起点
    while head:  # 逐层向下
        dummy = type(head)(0)  # 层内哑节点
        tail = dummy
        p = head
        while p:  # 沿 next 链遍历当前层
            if p.left:  # 左孩子入下一层链
                tail.next = p.left
                tail = tail.next
            if p.right:  # 右孩子入下一层链
                tail.next = p.right
                tail = tail.next
            p = p.next
        head = dummy.next  # 下一层起点
    return root  # 返回 根节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(connect(None))  # 打印输出
