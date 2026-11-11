# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144830623
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def longestConsecutive(nums):  # 定义函数 longestConsecutive（参数：数组）
    num_set = set()  # 把 set() 存入 num_set
    for num in nums:  # 逐个取出 数组 的元素（num）
        num_set.add(num)  # num_set 追加 num)
    longestStreak = 0  # 把 0 存入 longestStreak
    for num in num_set:  # 逐个取出 num_set 的元素（num）
        if (num - 1) not in num_set:  # 若 num 减 1) not in num_set
            currentNum = num  # 把 num 存入 currentNum
            currentStreak = 1  # 把 1 存入 currentStreak
            while (currentNum + 1) in num_set:  # 循环，直到不满足「currentNum 加 1) in num_set」
                currentNum += 1  # currentNum累加 1
                currentStreak += 1  # currentStreak累加 1
            longestStreak = max(
                longestStreak, currentStreak
            )  # 把 取较大值 longestStreak, currentStreak) 存入 longestStreak
    return longestStreak  # 返回 longestStreak


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(longestConsecutive([1, 2, 3]))  # 打印输出
