# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397916
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def secondGreaterElement(nums):  # 定义函数 secondGreaterElement（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    res = [-1] * n  # 把 [ 减 1] 乘 元素个数 存入 结果
    stack = []  # 把 [] 存入 栈
    # Min-heap simulation using a list (priority queue)
    pq = []  # 把 [] 存入 优先队列

    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        # Process elements from priority queue (second greater found)
        while pq and pq[0][0] < nums[i]:  # 循环，直到不满足「优先队列 and 优先队列[0][0] 小于 数组[下标 i]」
            val, idx = pq.pop(0)  # 把 优先队列 弹出 0) 写入 val, idx
            res[idx] = nums[i]  # 把 数组[下标 i] 写入 res[idx]

        # Find first greater element and add to priority queue
        while (
            stack and nums[stack[-1]] < nums[i]
        ):  # 循环，直到不满足「栈 and 数组[栈[ 减 1]] 小于 数组[下标 i]」
            idx = stack.pop()  # 把 栈 弹出 ) 存入 idx
            # Add to priority queue with value for sorting
            pq.append((nums[idx], idx))  # 把 (数组[idx], idx 追加到列表尾部
            pq.sort()  # Keep sorted as min-heap

        stack.append(i)  # 把 下标 i 追加到列表尾部

    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(secondGreaterElement([1, 2, 3]))  # 打印输出
