# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386215
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def connect(root):  # 定义函数 connect（参数：根节点）
    if root == None:  # 若 根节点 等于 None
        return root  # 返回 根节点
    Q = [root]  # 把 [根节点] 存入 Q
    while len(Q) > 0:  # 循环，直到不满足「长度(Q) 超过 0」
        size = len(Q)  # 把 长度(Q) 存入 大小
        for i in range(0, size):  # 让 下标 i 从 0 到 大小 遍历
            node = Q.pop(0)  # 把 Q 弹出 0) 存入 节点
            if i < size - 1:  # 若 下标 i 小于 大小 减 1
                node.next = Q[0]  # 把 Q[0] 写入 下一个
            if node.left != None:  # 若 节点.左边界 不等于 None
                Q.append(node.left)  # 把 节点.左边界 追加到列表尾部
            if node.right != None:  # 若 节点.右边界 不等于 None
                Q.append(node.right)  # 把 节点.右边界 追加到列表尾部
    return root  # 返回 根节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(connect(None))  # 打印输出
