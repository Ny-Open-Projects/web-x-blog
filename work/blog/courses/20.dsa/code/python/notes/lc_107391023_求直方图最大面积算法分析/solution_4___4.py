# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def get_result(n, h):  # 定义函数 get_result（参数：元素个数, h）
    # 算法4：单调栈（哨兵版本）
    res = 0  # 把 0 存入 结果
    stack = [0]  # 把 [0] 存入 栈
    for i in range(1, n + 2):  # 遍历到 n+1，h[n+1]=0 作为右哨兵
        while h[stack[-1]] > h[i]:  # 循环，直到不满足「h[栈[ 减 1]] 超过 h[下标 i]」
            now_h = h[stack.pop()]  # 把 h[栈 弹出 )] 存入 now_h
            width = i - stack[-1] - 1  # 把 下标 i 减 栈[ 减 1] 减 1 存入 width
            area = now_h * width  # 把 now_h 乘 width 存入 area
            if area > res:  # 若 area 超过 结果
                res = area  # 把 area 存入 结果
        stack.append(i)  # 把 下标 i 追加到列表尾部
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    h = [0, 2, 3, 3, 3, 2, 0]  # 把 [0, 2, 3, 3, 3, 2, 0] 存入 h
    print(get_result(5, h))  # 输出: 10
