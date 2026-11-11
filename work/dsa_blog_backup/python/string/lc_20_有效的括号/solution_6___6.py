# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130442145
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isValid3(s):  # 定义函数 isValid3（参数：字符串）
    if len(s) % 2 == 1:  # 若 长度(字符串) 对…取模 2 等于 1
        return False  # 返回 False
    pairs = {")": "(", "}": "{", "]": "["}  # 把 {')': '(', '}': '{', ']': '['} 存入 pairs
    stack = []  # 把 [] 存入 栈
    for c in s:  # 逐个取出 字符串 的元素（字符）
        if c in pairs:  # 若 字符 in pairs
            if not stack or stack[-1] != pairs[c]:  # 若 not 栈 or 栈[ 减 1] 不等于 pairs[字符]
                return False  # 返回 False
            stack.pop()  # 弹出栈顶元素
        else:  # 否则
            stack.append(c)  # 把 字符 追加到列表尾部
    return not stack  # 返回 not 栈


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isValid3("abc"))  # 打印输出
