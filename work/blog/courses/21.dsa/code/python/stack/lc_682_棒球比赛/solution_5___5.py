# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734875
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def calPoints(operations):  # 定义函数 calPoints（参数：operations）
    numStack = []  # 把 [] 存入 numStack

    def sum_nums(nums):  # 定义函数 sum_nums（参数：数组）
        return sum(nums)  # 返回 累计和(数组)

    operationMap = {  # 把 { 存入 operationMap
        "C": lambda: numStack.pop(),
        "D": lambda: numStack.append(numStack[-1] * 2),
        "+": lambda: numStack.append(sum_nums(numStack[-2:])),
    }

    for o in operations:  # 逐个取出 operations 的元素（o）
        if o.lstrip("-").isdigit() or (o.startswith("-") and o[1:].isdigit()):
            numStack.append(int(o))  # 把 int(o 追加到列表尾部
        else:  # 否则
            operationMap[o]()  # operationMap[o]()

    return sum(numStack)  # 返回 累计和(numStack)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(calPoints(["5", "2", "C", "D", "+"]))  # 打印输出
