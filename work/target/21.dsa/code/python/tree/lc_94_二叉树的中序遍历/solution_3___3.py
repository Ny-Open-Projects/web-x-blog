# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130743564
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def inorderTraversal(root):  # 定义函数 inorderTraversal（参数：根节点）
    result = []  # 把 [] 存入 结果
    stk = []  # 把 [] 存入 栈
    while root or len(stk):  # 循环，直到不满足「根节点 or 长度(栈」
        while root:  # 循环，直到不满足「根节点」
            stk.append(root)  # 把 根节点 追加到列表尾部
            root = root.left  # 把 根节点.左边界 存入 根节点
        root = stk.pop()  # 把 栈 弹出 ) 存入 根节点
        result.append(root.val)  # 把 根节点.值 追加到列表尾部
        root = root.right  # 把 根节点.右边界 存入 根节点
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(inorderTraversal(None))  # 打印输出
