# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144830623
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def longestConsecutive(nums):  # 定义函数 longestConsecutive（参数：数组）
    num_set = set(nums)  # 把 set(数组) 存入 num_set
    longest = 0  # 把 0 存入 longest
    for num in num_set:  # 逐个取出 num_set 的元素（num）
        if num - 1 not in num_set:  # 若 num 减 1 not in num_set
            current_num = num  # 把 num 存入 current_num
            current_streak = 1  # 把 1 存入 current_streak
            while current_num + 1 in num_set:  # 循环，直到不满足「current_num 加 1 in num_set」
                current_num += 1  # current_num累加 1
                current_streak += 1  # current_streak累加 1
            longest = max(longest, current_streak)  # 把 取较大值 longest, current_streak) 存入 longest
    return longest  # 返回 longest


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(longestConsecutive([1, 2, 3]))  # 打印输出
