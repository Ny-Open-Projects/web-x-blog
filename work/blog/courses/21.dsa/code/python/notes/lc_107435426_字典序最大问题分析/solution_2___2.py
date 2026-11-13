# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107435426
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def get_result_linear(n, ele):  # 定义函数 get_result_linear（参数：元素个数, ele）
    """字典序最大的出栈序列 —— 线性版 O(n)：预处理 maxElement[i] = max(ele[i:])。"""
    ans = []  # 把 [] 存入 答案
    stack = []  # 把 [] 存入 栈
    # 预处理：倒序求后缀最大值
    max_element = [0] * n  # 把 [0] 乘 元素个数 存入 max_element
    max_element[n - 1] = ele[n - 1]  # 把 ele[元素个数 减 1] 写入 max_element[n - 1]
    for i in range(n - 2, -1, -1):  # 让 下标 i 从 元素个数 减 2 倒数回去（每步减 1）
        max_element[i] = max(
            max_element[i + 1], ele[i]
        )  # 把 取较大值 max_element[下标 i 加 1], ele[下标 i]) 写入 max_element[i]
    i = 0  # 把 0 存入 下标 i
    while i < n:  # 循环，直到不满足「下标 i 小于 元素个数」
        mx = max_element[i]  # 把 max_element[下标 i] 存入 mx
        if stack and ele[stack[-1]] > mx:  # 若 栈 and ele[栈[ 减 1]] 超过 mx
            ans.append(ele[stack.pop()])  # 把 ele[栈 弹出 追加到列表尾部
        else:  # 否则
            while mx != ele[i]:  # 循环，直到不满足「mx 不等于 ele[下标 i]」
                stack.append(i)  # 把 下标 i 追加到列表尾部
                i += 1  # 下标 i累加 1
            ans.append(ele[i])  # 把 ele[下标 i] 追加到列表尾部
            i += 1  # 下标 i累加 1
    while stack:  # 循环，直到不满足「栈」
        ans.append(ele[stack.pop()])  # 把 ele[栈 弹出 追加到列表尾部
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    n = 5  # 把 5 存入 元素个数
    ele = [4, 1, 3, 5, 2]  # 把 [4, 1, 3, 5, 2] 存入 ele
    print(get_result_linear(n, ele))  # [5, 3, 2, 1, 4]
