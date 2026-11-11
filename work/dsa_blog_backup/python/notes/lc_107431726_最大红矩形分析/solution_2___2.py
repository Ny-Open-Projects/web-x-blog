# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def get_result(n, m, matrix):  # 定义函数 get_result（参数：元素个数, 映射表, 矩阵）
    # 卡位做法 O(n * m^2)
    ans = 0  # 把 0 存入 答案
    height = [0] * (m + 2)  # 把 [0] 乘 (映射表 加 2) 存入 height
    for k in range(n):  # 让 下标 k 从 元素个数 遍历
        for i in range(1, m + 1):  # 让 下标 i 从 1 到 映射表 加 1 遍历
            if matrix[k][i - 1] == ".":  # 若 矩阵[下标 k][下标 i 减 1] 等于 '.'
                height[i] += 1  # height[i]累加 1
            else:  # 否则
                height[i] = 0  # 把 0 写入 height[i]
        for a in range(1, m + 1):  # 让 数组 从 1 到 映射表 加 1 遍历
            cur_h = height[a]  # 把 height[数组] 存入 cur_h
            # 找左卡位点
            lo = a - 1  # 把 数组 减 1 存入 左边界
            while (
                lo >= 1 and height[lo] >= cur_h
            ):  # 循环，直到不满足「左边界 不低于 1 and height[左边界] 不低于 cur_h」
                lo -= 1  # 左边界累减 1
            # 找右卡位点
            hi = a + 1  # 把 数组 加 1 存入 右边界
            while (
                hi <= m and height[hi] >= cur_h
            ):  # 循环，直到不满足「右边界 不超过 映射表 and height[右边界] 不低于 cur_h」
                hi += 1  # 右边界累加 1
            area = (hi - lo - 1) * cur_h  # 把 (右边界 减 左边界 减 1) 乘 cur_h 存入 area
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
