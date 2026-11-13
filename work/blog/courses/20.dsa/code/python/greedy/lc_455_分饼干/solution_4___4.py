# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134668646
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def findContentChildren(g, s):  # 定义函数 findContentChildren（参数：g, 字符串）
    # 贪心：对每个孩子分配 >= 其胃口的最小饼干（计数版，避免越界）
    g.sort()  # 排序
    s.sort()  # 排序
    i = j = 0  # 把 下标 j 赋值为 0 存入 下标 i
    while i < len(g) and j < len(s):  # 循环，直到不满足「下标 i 小于 长度(g) and 下标 j 小于 长度(字符串」
        if s[j] >= g[i]:  # 若 字符串[下标 j] 不低于 g[下标 i]
            i += 1  # 下标 i累加 1
        j += 1  # 下标 j累加 1
    return i  # 返回 下标 i


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(findContentChildren([1, 2, 3], [1, 1]))  # 打印输出
    print(findContentChildren([1, 2], [1, 2, 3]))  # 打印输出
