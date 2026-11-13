# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130877211
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def levelOrder(root):  # 定义函数 levelOrder（参数：根节点）
    ret = []  # 把 [] 存入 ret
    if not root:
        return ret  # 若 not 根节点: return ret
    q = [root]  # 把 [根节点] 存入 节点
    while len(q):  # 循环，直到不满足「长度(节点」
        currentLevelSize = len(q)  # 把 长度(节点) 存入 currentLevelSize
        ret.append([])  # 把 [] 追加到列表尾部
        for i in range(currentLevelSize):  # 让 下标 i 从 currentLevelSize 遍历
            node = q.pop(0)  # 把 节点 弹出 0) 存入 节点
            ret[len(ret) - 1].append(node.val)  # 把 节点.值 追加到列表尾部
            if node.left:
                q.append(node.left)  # 若 节点.左边界: 节点 追加 节点.左边界
            if node.right:
                q.append(node.right)  # 若 节点.右边界: 节点 追加 节点.右边界
    return ret  # 返回 ret


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(levelOrder(None))  # 打印输出
