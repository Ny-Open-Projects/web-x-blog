# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114201
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def removeDuplicates(s):  # 定义函数 removeDuplicates（参数：字符串）
    stk = []  # 把 [] 存入 栈
    for ch in s:  # 逐个取出 字符串 的元素（字符）
        if stk and stk[-1] == ch:  # 若 栈 and 栈[ 减 1] 等于 字符
            stk.pop()  # 弹出栈顶元素
        else:  # 否则
            stk.append(ch)  # 把 字符 追加到列表尾部
    return "".join(stk)  # 返回 「」.join(栈)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(removeDuplicates("abc"))  # 打印输出
