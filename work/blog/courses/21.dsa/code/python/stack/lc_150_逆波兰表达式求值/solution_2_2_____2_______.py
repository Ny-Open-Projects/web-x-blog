# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113233
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def evalRPN(tokens):  # 定义函数 evalRPN（参数：tokens）
    n = len(tokens)  # 把 长度(tokens) 存入 元素个数
    stack = [0] * ((n + 1) // 2)  # 把 [0] 乘 ((元素个数 加 1) 除以 除以 2) 存入 栈
    index = -1  # 把 减 1 存入 index
    for token in tokens:  # 逐个取出 tokens 的元素（token）
        if token in ("+", "-", "*", "/"):  # 若 token in (「 加 」, 「 加 」, 「 加 」, 「 加 」
            num2 = stack[index]  # 把 栈[index] 存入 num2
            num1 = stack[index - 1]  # 把 栈[index 减 1] 存入 num1
            index -= 1  # index累减 1
            if token == "+":  # 若 token 等于 「 加 」
                stack[index] = num1 + num2  # 把 num1 加 num2 写入 stack[index]
            elif token == "-":  # 否则，若 token 等于 「 减 」
                stack[index] = num1 - num2  # 把 num1 减 num2 写入 stack[index]
            elif token == "*":  # 否则，若 token 等于 「 乘 」
                stack[index] = num1 * num2  # 把 num1 乘 num2 写入 stack[index]
            else:  # 否则
                stack[index] = int(num1 / num2)  # 把 int(num1 除以 num2) 写入 stack[index]
        else:  # 否则
            index += 1  # index累加 1
            stack[index] = int(token)  # 把 int(token) 写入 stack[index]
    return stack[index]  # 返回 栈[index]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(evalRPN(["2", "1", "+", "3", "*"]))  # 打印输出
