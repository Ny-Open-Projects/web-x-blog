# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130877211
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def levelOrder(root):  # 定义函数 levelOrder（参数：根节点）
    if not root:
        return []  # 若 not 根节点: return []
    q = [[root, 0]]  # 把 [[根节点, 0]] 存入 节点
    res = []  # 把 [] 存入 结果
    while len(q):  # 循环，直到不满足「长度(节点」
        [n, l] = q.pop(0)  # 把 节点 弹出 0) 写入 [n, l]
        if not res[l]:  # 若 not 结果[左指针]
            res.append([n.val])  # 把 [元素个数.值] 追加到列表尾部
        else:  # 否则
            res[l].append(n.val)  # 把 元素个数.值 追加到列表尾部
        n.left and q.append([n.left, l + 1])  # 把 [元素个数.左边界, 左指针 加 1] 追加到列表尾部
        n.right and q.append([n.right, l + 1])  # 把 [元素个数.右边界, 左指针 加 1] 追加到列表尾部
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(levelOrder(None))  # 打印输出
