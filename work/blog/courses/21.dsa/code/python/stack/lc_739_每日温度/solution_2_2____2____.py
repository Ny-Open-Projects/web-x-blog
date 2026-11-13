# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145354164
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def dailyTemperatures(temperatures):  # 定义函数 dailyTemperatures（参数：temperatures）
    length = len(temperatures)  # 把 长度(temperatures) 存入 长度
    ans = [0] * length  # 把 [0] 乘 长度 存入 答案
    stack = []  # 把 [] 存入 栈

    for i in range(length):  # 让 下标 i 从 长度 遍历
        temperature = temperatures[i]  # 把 temperatures[下标 i] 存入 temperature
        while (
            stack and temperature > temperatures[stack[-1]]
        ):  # 循环，直到不满足「栈 and temperature 超过 temperatures[栈[ 减 1]]」
            prev_index = stack.pop()  # 把 栈 弹出 ) 存入 prev_index
            ans[prev_index] = i - prev_index  # 把 下标 i 减 prev_index 写入 ans[prev_index]
        stack.append(i)  # 把 下标 i 追加到列表尾部

    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # 打印输出
    print(dailyTemperatures([30, 40, 50, 60]))  # 打印输出
    print(dailyTemperatures([30, 60, 90]))  # 打印输出
