# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145088842
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def largestValues(root):  # 定义函数 largestValues（参数：根节点）
    if not root:
        return []  # 若 not 根节点: return []
    res = []  # 把 [] 存入 结果
    queue = [root]  # 把 [根节点] 存入 队列
    while len(queue):  # 循环，直到不满足「长度(队列」
        len = len(queue)  # 把 长度(队列) 存入 长度
        maxVal = -Number.MAX_VALUE  # 把 减 Number.MAX_VALUE 存入 maxVal
        while len > 0:  # 循环，直到不满足「长度 超过 0」
            len -= 1  # 长度累减 1
            t = queue.pop(0)  # 把 队列 弹出 0) 存入 另一字符串
            maxVal = max(maxVal, t.val)  # 把 取较大值 maxVal, 另一字符串.值) 存入 maxVal
            if t.left:  # 若 另一字符串.左边界
                queue.append(t.left)  # 把 另一字符串.左边界 追加到列表尾部
            if t.right:  # 若 另一字符串.右边界
                queue.append(t.right)  # 把 另一字符串.右边界 追加到列表尾部
        res.append(maxVal)  # 把 maxVal 追加到列表尾部
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(largestValues(None))  # 打印输出
