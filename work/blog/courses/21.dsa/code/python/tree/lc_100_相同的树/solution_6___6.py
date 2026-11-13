# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134622591
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isSameTree(p, q):  # 定义函数 isSameTree（参数：节点, 节点）
    if not p and not q:
        return True  # 若 not 节点 and not 节点: return True
    if p.val != q.val:
        return False  # 若 节点.值 不等于 节点.值: return False
    queue1 = [p]  # 把 [节点] 存入 queue1
    queue2 = [q]  # 把 [节点] 存入 queue2
    while len(queue1) and len(queue2):  # 循环，直到不满足「长度(queue1) and 长度(queue2」
        pTop = queue1.pop(0)  # 把 queue1 弹出 0) 存入 pTop
        qTop = queue2.pop(0)  # 把 queue2 弹出 0) 存入 qTop
        if pTop.val != qTop.val:
            return False  # 若 pTop.值 不等于 qTop.值: return False
        pLeft = pTop.left  # 把 pTop.左边界 存入 pLeft
        pRight = pTop.right  # 把 pTop.右边界 存入 pRight
        qLeft = qTop.left  # 把 qTop.左边界 存入 qLeft
        qRight = qTop.right  # 把 qTop.右边界 存入 qRight
        if (pLeft and not qLeft) or (not pLeft and qLeft):
            return False
        if (pRight and not qRight) or (not pRight and qRight):
            return False
        if pLeft:
            queue1.append(pLeft)  # 若 pLeft: queue1 追加 pLeft
        if pRight:
            queue1.append(pRight)  # 若 pRight: queue1 追加 pRight
        if qLeft:
            queue2.append(qLeft)  # 若 qLeft: queue2 追加 qLeft
        if qRight:
            queue2.append(qRight)  # 若 qRight: queue2 追加 qRight
    return not len(queue1) and not len(queue2)  # 返回 not 长度(queue1) and not 长度(queue2)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isSameTree(None, None))  # 打印输出
