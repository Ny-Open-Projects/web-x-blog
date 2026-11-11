# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114201
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def removeDuplicates(s):  # 定义函数 removeDuplicates（参数：字符串）
    stack = []  # 把 [] 存入 栈
    for x in s:  # 逐个取出 字符串 的元素（x）
        if stack and stack[-1] == x:  # 若 栈 and 栈[ 减 1] 等于 x
            stack.pop()  # 弹出栈顶元素
            continue  # 跳过本轮，进入下一次
        stack.append(x)  # 把 x 追加到列表尾部
    return "".join(stack)  # 返回 「」.join(栈)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(removeDuplicates("abc"))  # 打印输出
