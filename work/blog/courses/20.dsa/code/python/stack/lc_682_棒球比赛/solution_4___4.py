# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734875
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def calPoints(operations):  # 定义函数 calPoints（参数：operations）
    result = []  # 把 [] 存入 结果
    for item in operations:  # 逐个取出 operations 的元素（item）
        if item == "C":  # 若 item 等于 「C」
            if result:  # 若 结果
                result.pop()  # 弹出栈顶元素
        elif item == "D":  # 否则，若 item 等于 「D」
            result.append(result[-1] * 2)  # 把 结果[ 减 1] 乘 2 追加到列表尾部
        elif item == "+":  # 否则，若 item 等于 「 加 」
            result.append(result[-1] + result[-2])  # 把 结果[ 减 1] 加 结果[ 减 2] 追加到列表尾部
        else:  # 否则
            result.append(int(item))  # 把 int(item 追加到列表尾部
    return sum(result)  # 返回 累计和(结果)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(calPoints(["5", "2", "C", "D", "+"]))  # 打印输出
