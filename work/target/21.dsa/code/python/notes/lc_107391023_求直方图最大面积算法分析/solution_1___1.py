# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def get_result(n, h):  # 定义函数 get_result（参数：元素个数, h）
    # 算法1：蛮力 O(n^3)
    # h 为 1 下标数组，h[0]=h[n+1]=0
    res = 0  # 把 0 存入 结果
    for a in range(1, n + 1):  # 让 数组 从 1 到 元素个数 加 1 遍历
        for b in range(a, n + 1):  # 让 b 从 数组 到 元素个数 加 1 遍历
            min_h = 50000  # 把 50000 存入 min_h
            for c in range(a, b + 1):  # 让 字符 从 数组 到 b 加 1 遍历
                if h[c] < min_h:  # 若 h[字符] 小于 min_h
                    min_h = h[c]  # 把 h[字符] 存入 min_h
            area = (b - a + 1) * min_h  # 把 (b 减 数组 加 1) 乘 min_h 存入 area
            if area > res:  # 若 area 超过 结果
                res = area  # 把 area 存入 结果
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # 输入：5 ; 2 3 3 3 2
    h = [0, 2, 3, 3, 3, 2, 0]  # 把 [0, 2, 3, 3, 3, 2, 0] 存入 h
    print(get_result(5, h))  # 输出: 10
