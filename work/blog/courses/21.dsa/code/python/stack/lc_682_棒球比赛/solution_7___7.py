# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734875
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def solve():  # 定义函数 solve（参数：无）
    operations = ["5", "2", "C", "D", "+"]  # 把 [「5」,「5」,「5」,「5」,「5」] 存入 operations
    result = calPoints(operations)  # 把 calPoints(operations) 存入 结果
    print(result)  # 打印输出


def calPoints(operations):  # 定义函数 calPoints（参数：operations）
    scores = []  # 把 [] 存入 scores
    for op in operations:  # 逐个取出 operations 的元素（op）
        if op == "C":  # 若 op 等于 「C」
            scores.pop()  # 弹出栈顶元素
        elif op == "D":  # 否则，若 op 等于 「D」
            scores.append(scores[-1] * 2)  # 把 scores[ 减 1] 乘 2 追加到列表尾部
        elif op == "+":  # 否则，若 op 等于 「 加 」
            scores.append(scores[-1] + scores[-2])  # 把 scores[ 减 1] 加 scores[ 减 2] 追加到列表尾部
        else:  # 否则
            scores.append(int(op))  # 把 int(op 追加到列表尾部
    return sum(scores)  # 返回 累计和(scores)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(solve())  # 打印输出
