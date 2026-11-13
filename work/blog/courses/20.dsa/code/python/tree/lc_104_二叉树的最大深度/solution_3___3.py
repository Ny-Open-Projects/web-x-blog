# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxDepth(root):  # 定义函数 maxDepth（参数：根节点）
    if not root:
        return 0  # 若 not 根节点: return 0
    q = [root]  # 把 [根节点] 存入 节点
    dep = 0  # 把 0 存入 dep
    while len(q):  # 循环，直到不满足「长度(节点」
        len = len(q)  # 把 长度(节点) 存入 长度
        while len:  # 循环，直到不满足「长度」
            n = q.pop(0)  # 把 节点 弹出 0) 存入 元素个数
            if n.left:
                q.append(n.left)  # 若 元素个数.左边界: 节点 追加 元素个数.左边界
            if n.right:
                q.append(n.right)  # 若 元素个数.右边界: 节点 追加 元素个数.右边界
            len -= 1  # 长度累减 1
        dep += 1  # dep累加 1
    return dep  # 返回 dep


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxDepth(None))  # 打印输出
