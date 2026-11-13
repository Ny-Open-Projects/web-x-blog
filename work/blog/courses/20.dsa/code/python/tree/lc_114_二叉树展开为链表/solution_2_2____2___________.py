# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145007192
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def flatten(root):  # 定义函数 flatten（参数：根节点）
    list = []  # 把 [] 存入 列表
    stack = []  # 把 [] 存入 栈
    node = root  # 把 根节点 存入 节点
    while node != None or len(stack):  # 循环，直到不满足「节点 不等于 None or 长度(栈」
        while node != None:  # 循环，直到不满足「节点 不等于 None」
            list.append(node)  # 把 节点 追加到列表尾部
            stack.append(node)  # 把 节点 追加到列表尾部
            node = node.left  # 把 节点.左边界 存入 节点
        node = stack.pop()  # 把 栈 弹出 ) 存入 节点
        node = node.right  # 把 节点.右边界 存入 节点
    size = len(list)  # 把 长度(列表) 存入 大小
    for i in range(1, size):  # 让 下标 i 从 1 到 大小 遍历
        prev = list[i - 1], curr = list[i]  # 把 列表[下标 i 减 1], 当前值 赋值为 列表[下标 i] 存入 前一个
        prev.left = None  # 把 None 写入 左边界
        prev.right = curr  # 把 当前值 写入 右边界


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(flatten(None))  # 打印输出
