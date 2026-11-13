# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def max_red_rectangle(matrix):  # 定义函数 max_red_rectangle（参数：矩阵）
    n = len(matrix)  # 把 长度(矩阵) 存入 元素个数
    m = len(matrix[0])  # 把 长度(矩阵[0]) 存入 映射表
    ans = 0  # 把 0 存入 答案
    height = [0] * (m + 2)  # 把 [0] 乘 (映射表 加 2) 存入 height
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
                ans = max(ans, now_h * width)  # 把 取较大值 答案, now_h 乘 width) 存入 答案
            stack.append(i)  # 把 下标 i 追加到列表尾部
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # 测试输入数据
    # 4 5
    # .....
    # XXXXX
    # .X...
    # .....
    test_input = [
        ".....",
        "XXXXX",
        ".X...",
        ".....",
    ]
    print(max_red_rectangle(test_input))  # 输出: 6
