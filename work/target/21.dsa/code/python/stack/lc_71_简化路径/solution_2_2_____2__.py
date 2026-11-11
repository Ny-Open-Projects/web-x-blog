# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145112805
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def simplifyPath(path):  # 定义函数 simplifyPath（参数：当前路径）
    names = path.split("/")  # 把 当前路径.split(「 除以 」) 存入 names
    stack = []  # 把 [] 存入 栈
    for name in names:  # 逐个取出 names 的元素（name）
        if name == "..":  # 若 name 等于 「..」
            if stack:  # 若 栈
                stack.pop()  # 弹出栈顶元素
        elif name and name != ".":  # 否则，若 name and name 不等于 「.」
            stack.append(name)  # 把 name 追加到列表尾部
    return "/" + "/".join(stack)  # 返回 「 除以 」 加 「 除以 」.join(栈)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(simplifyPath("/home/"))  # 打印输出
    print(simplifyPath("/a/./b/../../c/"))  # 打印输出
    print(simplifyPath("/../"))  # 打印输出
