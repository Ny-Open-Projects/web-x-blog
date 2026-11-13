# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134668646
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import bisect  # 引入依赖


def findContentChildren(g, s):  # 定义函数 findContentChildren（参数：g, 字符串）
    # 排序后用指针贪心匹配，剩余饼干用二分查找定位可满足的最小饼干
    g.sort()  # 排序
    s.sort()  # 排序
    j = 0  # 把 0 存入 下标 j
    count = 0  # 把 0 存入 计数
    for child in g:  # 逐个取出 g 的元素（子节点）
        k = bisect.bisect_left(s, child, j)  # 把 bisect.bisect_left(字符串, 子节点, 下标 j) 存入 下标 k
        if k < len(s):  # 若 下标 k 小于 长度(字符串
            count += 1  # 计数累加 1
            j = k + 1  # 把 下标 k 加 1 存入 下标 j
        else:  # 否则
            break  # 跳出循环
    return count  # 返回 计数


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(findContentChildren([1, 2, 3], [1, 1]))  # 打印输出
    print(findContentChildren([1, 2], [1, 2, 3]))  # 打印输出
