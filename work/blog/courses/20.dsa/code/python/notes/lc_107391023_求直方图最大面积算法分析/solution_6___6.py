# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def get_result(n, h):  # 定义函数 get_result（参数：元素个数, h）
    # 通用输入程序的算法实现（单调栈）
    res = 0  # 把 0 存入 结果
    stack = [0]  # 把 [0] 存入 栈
    for i in range(1, n + 2):  # 让 下标 i 从 1 到 元素个数 加 2 遍历
        while h[stack[-1]] > h[i]:  # 循环，直到不满足「h[栈[ 减 1]] 超过 h[下标 i]」
            now_h = h[stack.pop()]  # 把 h[栈 弹出 )] 存入 now_h
            width = i - stack[-1] - 1  # 把 下标 i 减 栈[ 减 1] 减 1 存入 width
            area = now_h * width  # 把 now_h 乘 width 存入 area
            if area > res:  # 若 area 超过 结果
                res = area  # 把 area 存入 结果
        stack.append(i)  # 把 下标 i 追加到列表尾部
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # 输入格式：第一行 n，第二行 n 个非负整数
    n = 5  # 把 5 存入 元素个数
    heights = [2, 3, 3, 3, 2]  # 把 [2, 3, 3, 3, 2] 存入 heights
    h = [0] + heights + [0]  # 控制 height[0] 和 height[n+1] 均为 0
    print(get_result(n, h))  # 输出: 10
