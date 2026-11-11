# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130442145
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isValid(s):  # 定义函数 isValid（参数：字符串）
    stack = []  # 把 [] 存入 栈
    mapping = {")": "(", "}": "{", "]": "["}  # 把 {')': '(', '}': '{', ']': '['} 存入 mapping
    for char in s:  # 逐个取出 字符串 的元素（char）
        if char in mapping:  # 若 char in mapping
            top = stack.pop() if stack else "#"
            if mapping[char] != top:  # 若 mapping[char] 不等于 top
                return False  # 返回 False
        else:  # 否则
            stack.append(char)  # 把 char 追加到列表尾部
    return not stack  # 返回 not 栈


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isValid("abc"))  # 打印输出
