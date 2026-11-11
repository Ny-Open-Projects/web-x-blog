# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def get_result(n, m, matrix):  # 定义函数 get_result（参数：元素个数, 映射表, 矩阵）
    # 蛮力做法 O(n * m^3)
    ans = 0  # 把 0 存入 答案
    height = [0] * (m + 2)  # height[1..m] 为当前行的列高，左右哨兵为 0
    for k in range(n):  # 让 下标 k 从 元素个数 遍历
        for i in range(1, m + 1):  # 让 下标 i 从 1 到 映射表 加 1 遍历
            if matrix[k][i - 1] == ".":  # 若 矩阵[下标 k][下标 i 减 1] 等于 '.'
                height[i] += 1  # height[i]累加 1
            else:  # 否则
                height[i] = 0  # 把 0 写入 height[i]
        for a in range(1, m + 1):  # 让 数组 从 1 到 映射表 加 1 遍历
            for b in range(a, m + 1):  # 让 b 从 数组 到 映射表 加 1 遍历
                min_h = 50000  # 把 50000 存入 min_h
                for c in range(a, b + 1):  # 让 字符 从 数组 到 b 加 1 遍历
                    if height[c] < min_h:  # 若 height[字符] 小于 min_h
                        min_h = height[c]  # 把 height[字符] 存入 min_h
                area = (b - a + 1) * min_h  # 把 (b 减 数组 加 1) 乘 min_h 存入 area
                if area > ans:  # 若 area 超过 答案
                    ans = area  # 把 area 存入 答案
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    matrix = [
        ".....",
        "XXXXX",
        ".X...",
        ".....",
    ]
    print(get_result(4, 5, matrix))  # 输出: 6
