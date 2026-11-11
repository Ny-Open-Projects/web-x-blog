# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130442145
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isValid(s):  # 定义函数 isValid（参数：字符串）
    stack = []  # 把 [] 存入 栈
    pairs = {")": "(", "]": "[", "}": "{"}  # 把 {')': '(', ']': '[', '}': '{'} 存入 pairs
    for ch in s:  # 逐个取出 字符串 的元素（字符）
        if ch in pairs:  # 若 字符 in pairs
            top = stack.pop() if stack else "#"
            if top != pairs[ch]:  # 若 top 不等于 pairs[字符]
                return False  # 返回 False
        else:  # 否则
            stack.append(ch)  # 把 字符 追加到列表尾部
    return not stack  # 返回 not 栈


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isValid("()"))  # 打印输出
    print(isValid("()[]{}"))  # 打印输出
    print(isValid("(]"))  # 打印输出
