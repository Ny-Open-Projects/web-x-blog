# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113233
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def evalRPN(tokens):  # 定义函数 evalRPN（参数：tokens）
    stack = []  # 把 [] 存入 栈
    for token in tokens:  # 逐个取出 tokens 的元素（token）
        if token not in ("+", "-", "*", "/"):  # 若 token not in (「 加 」, 「 加 」, 「 加 」, 「 加 」
            stack.append(int(token))  # 把 int(token 追加到列表尾部
        else:  # 否则
            num2 = stack.pop()  # 把 栈 弹出 ) 存入 num2
            num1 = stack.pop()  # 把 栈 弹出 ) 存入 num1
            if token == "+":  # 若 token 等于 「 加 」
                stack.append(num1 + num2)  # 把 num1 加 num2 追加到列表尾部
            elif token == "-":  # 否则，若 token 等于 「 减 」
                stack.append(num1 - num2)  # 把 num1 减 num2 追加到列表尾部
            elif token == "*":  # 否则，若 token 等于 「 乘 」
                stack.append(num1 * num2)  # 把 num1 乘 num2 追加到列表尾部
            else:  # 否则
                # Truncate toward zero
                stack.append(int(num1 / num2))  # 把 int(num1 除以 num2 追加到列表尾部
    return stack.pop()  # 返回 栈 弹出 )


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(evalRPN(["2", "1", "+", "3", "*"]))  # 打印输出
    print(evalRPN(["4", "13", "5", "/", "+"]))  # 打印输出
