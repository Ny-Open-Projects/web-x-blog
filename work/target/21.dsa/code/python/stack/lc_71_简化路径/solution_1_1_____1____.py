# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145112805
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def simplifyPath(path):  # 定义函数 simplifyPath（参数：当前路径）
    stk = []  # 把 [] 存入 栈
    for s in path.split("/"):  # 逐个取出 当前路径 的元素（字符串）
        if not s or s == ".":  # 若 not 字符串 or 字符串 等于 '.'
            continue  # 跳过本轮，进入下一次
        if s != "..":  # 若 字符串 不等于 '..'
            stk.append(s)  # 把 字符串 追加到列表尾部
        elif stk:  # 否则，若 栈
            stk.pop()  # 弹出栈顶元素
    return "/" + "/".join(stk)  # 返回 ' 除以 ' 加 ' 除以 '.join(栈)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(simplifyPath("/home/"))  # 打印输出
    print(simplifyPath("/a/./b/../../c/"))  # 打印输出
    print(simplifyPath("/../"))  # 打印输出
