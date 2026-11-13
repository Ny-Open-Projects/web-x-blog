# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134668646
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def findContentChildren(g, s):  # 定义函数 findContentChildren（参数：g, 字符串）
    g.sort()  # 排序
    s.sort()  # 排序
    child = 0  # 把 0 存入 子节点
    cookie = 0  # 把 0 存入 cookie
    while child < len(g) and cookie < len(
        s
    ):  # 循环，直到不满足「子节点 小于 长度(g) and cookie 小于 长度(字符串」
        if s[cookie] >= g[child]:  # 若 字符串[cookie] 不低于 g[子节点]
            child += 1  # 子节点累加 1
        cookie += 1  # cookie累加 1
    return child  # 返回 子节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(findContentChildren([1, 2, 3], [1, 1]))  # 打印输出
    print(findContentChildren([1, 2], [1, 2, 3]))  # 打印输出
