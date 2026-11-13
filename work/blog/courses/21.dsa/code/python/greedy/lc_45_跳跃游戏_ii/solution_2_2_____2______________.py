# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145241433
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def jump(nums):  # 定义函数 jump（参数：数组）
    # 正向贪心（BFS 思想）：维护本层最远 end 与下一层最远 max_pos，跨层即 +1 步
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    if n <= 1:  # 若 元素个数 不超过 1
        return 0  # 返回 0
    max_pos = 0  # 把 0 存入 max_pos
    end = 0  # 把 0 存入 终点
    steps = 0  # 把 0 存入 steps
    for i in range(n - 1):  # 让 下标 i 从 元素个数 减 1 遍历
        max_pos = max(max_pos, i + nums[i])  # 把 取较大值 max_pos, 下标 i 加 数组[下标 i]) 存入 max_pos
        if i == end:  # 若 下标 i 等于 终点
            end = max_pos  # 把 max_pos 存入 终点
            steps += 1  # steps累加 1
    return steps  # 返回 steps


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(jump([2, 3, 1, 1, 4]))  # 打印输出
