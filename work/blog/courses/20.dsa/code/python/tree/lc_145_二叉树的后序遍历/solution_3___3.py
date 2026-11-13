# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130753362
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def postorderTraversal(root):  # 定义函数 postorderTraversal（参数：根节点）
    ans = []  # 把 [] 存入 答案
    stack = []  # 把 [] 存入 栈
    cur = root  # 把 根节点 存入 当前值
    while cur or len(stack):  # 循环，直到不满足「当前值 or 长度(栈」
        while cur:  # 循环，直到不满足「当前值」
            ans.append(cur.val)  # 把 当前值.值 追加到列表尾部
            stack.append(cur)  # 把 当前值 追加到列表尾部
            cur = cur.right  # 把 当前值.右边界 存入 当前值
        if len(stack):  # 若 长度(栈
            cur = stack.pop()  # 把 栈 弹出 ) 存入 当前值
            cur = cur.left  # 把 当前值.左边界 存入 当前值
    return ans.reverse()  # 返回 答案.reverse()


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(postorderTraversal(None))  # 打印输出
