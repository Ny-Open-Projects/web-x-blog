# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145354164
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def dailyTemperatures(temperatures):  # 定义函数 dailyTemperatures（参数：temperatures）
    length = len(temperatures)  # 把 长度(temperatures) 存入 长度
    ans = [0] * length  # 把 [0] 乘 长度 存入 答案
    next_warmer = [float("inf")] * 101  # 把 [float('inf')] 乘 101 存入 next_warmer

    for i in range(length - 1, -1, -1):  # 让 下标 i 从 长度 减 1 倒数回去（每步减 1）
        warmer_index = float("inf")  # 把 float('inf') 存入 warmer_index
        t = temperatures[i]  # 把 temperatures[下标 i] 存入 另一字符串

        # Find the nearest warmer day
        for temp in range(t + 1, 101):  # 让 临时变量 从 另一字符串 加 1 到 101 遍历
            if next_warmer[temp] < warmer_index:  # 若 next_warmer[临时变量] 小于 warmer_index
                warmer_index = next_warmer[temp]  # 把 next_warmer[临时变量] 存入 warmer_index

        if warmer_index < float("inf"):  # 若 warmer_index 小于 float('inf'
            ans[i] = warmer_index - i  # 把 warmer_index 减 下标 i 写入 ans[i]

        next_warmer[t] = i  # 把 下标 i 写入 next_warmer[t]

    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # 打印输出
    print(dailyTemperatures([30, 40, 50, 60]))  # 打印输出
    print(dailyTemperatures([30, 60, 90]))  # 打印输出
