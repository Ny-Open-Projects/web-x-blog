# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134668646
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def findContentChildren(g, s):  # 定义函数 findContentChildren（参数：g, 字符串）
    # 双指针：遍历孩子，为其寻找第一块能满足的最小饼干；计满足条件的孩子数
    g.sort()  # 排序
    s.sort()  # 排序
    j = 0  # 把 0 存入 下标 j
    n = len(s)  # 把 长度(字符串) 存入 元素个数
    count = 0  # 把 0 存入 计数
    for child in g:  # 逐个取出 g 的元素（子节点）
        while (
            j < n and s[j] < child
        ):  # 循环，直到不满足「下标 j 小于 元素个数 and 字符串[下标 j] 小于 子节点」
            j += 1  # 下标 j累加 1
        if j < n:  # 若 下标 j 小于 元素个数
            count += 1  # 计数累加 1
            j += 1  # 下标 j累加 1
        else:  # 否则
            break  # 跳出循环
    return count  # 返回 计数


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(findContentChildren([1, 2, 3], [1, 1]))  # 打印输出
    print(findContentChildren([1, 2], [1, 2, 3]))  # 打印输出
