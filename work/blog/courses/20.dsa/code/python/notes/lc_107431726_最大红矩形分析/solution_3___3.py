# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def get_result(n, m, matrix):  # 定义函数 get_result（参数：元素个数, 映射表, 矩阵）
    # 单调栈做法 O(n * m)
    ans = 0  # 把 0 存入 答案
    height = [0] * (m + 2)  # height[0] = height[m+1] = 0 哨兵
    for k in range(n):  # 让 下标 k 从 元素个数 遍历
        for i in range(1, m + 1):  # 让 下标 i 从 1 到 映射表 加 1 遍历
            if matrix[k][i - 1] == ".":  # 若 矩阵[下标 k][下标 i 减 1] 等于 '.'
                height[i] += 1  # height[i]累加 1
            else:  # 否则
                height[i] = 0  # 把 0 写入 height[i]
        stack = [0]  # 把 [0] 存入 栈
        for i in range(1, m + 2):  # 让 下标 i 从 1 到 映射表 加 2 遍历
            while height[stack[-1]] > height[i]:  # 循环，直到不满足「height[栈[ 减 1]] 超过 height[下标 i]」
                now_h = height[stack.pop()]  # 把 height[栈 弹出 )] 存入 now_h
                width = i - stack[-1] - 1  # 把 下标 i 减 栈[ 减 1] 减 1 存入 width
                area = now_h * width  # 把 now_h 乘 width 存入 area
                if area > ans:  # 若 area 超过 答案
                    ans = area  # 把 area 存入 答案
            stack.append(i)  # 把 下标 i 追加到列表尾部
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    matrix = [
        ".....",
        "XXXXX",
        ".X...",
        ".....",
    ]
    print(get_result(4, 5, matrix))  # 输出: 6
