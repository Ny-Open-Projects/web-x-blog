# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def get_result(n, h):  # 定义函数 get_result（参数：元素个数, h）
    # 算法5：单调栈（形式转换，i 从 0 开始）
    res = 0  # 把 0 存入 结果
    stack = []  # 把 [] 存入 栈
    i = 0  # 把 0 存入 下标 i
    while i < n + 2:  # 循环，直到不满足「下标 i 小于 元素个数 加 2」
        if not stack or h[stack[-1]] <= h[i]:  # 若 not 栈 or h[栈[ 减 1]] 不超过 h[下标 i]
            stack.append(i)  # 把 下标 i 追加到列表尾部
            i += 1  # 下标 i累加 1
        else:  # 否则
            now_h = h[stack.pop()]  # 把 h[栈 弹出 )] 存入 now_h
            width = i - stack[-1] - 1  # 把 下标 i 减 栈[ 减 1] 减 1 存入 width
            area = now_h * width  # 把 now_h 乘 width 存入 area
            if area > res:  # 若 area 超过 结果
                res = area  # 把 area 存入 结果
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    h = [0, 2, 3, 3, 3, 2, 0]  # 把 [0, 2, 3, 3, 3, 2, 0] 存入 h
    print(get_result(5, h))  # 输出: 10
