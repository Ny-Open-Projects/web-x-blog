# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145007192
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def flatten(root):  # 定义函数 flatten（参数：根节点）
    if root == None:
        return  # 若 根节点 等于 None: return
    stack = []  # 把 [] 存入 栈
    stack.append(root)  # 把 根节点 追加到列表尾部
    prev = None  # 把 None 存入 前一个
    while len(stack):  # 循环，直到不满足「长度(栈」
        curr = stack.pop()  # 把 栈 弹出 ) 存入 当前值
        if prev != None:  # 若 前一个 不等于 None
            prev.left = None  # 把 None 写入 左边界
            prev.right = curr  # 把 当前值 写入 右边界
        left = curr.left, right = curr.right  # 把 当前值.左边界, 右边界 赋值为 当前值.右边界 存入 左边界
        if right != None:
            stack.append(right)  # 若 右边界 不等于 None: 栈 追加 右边界
        if left != None:
            stack.append(left)  # 若 左边界 不等于 None: 栈 追加 左边界
        prev = curr  # 把 当前值 存入 前一个


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(flatten(None))  # 打印输出
