# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829143
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import bisect  # 引入依赖


def findNumberOfLIS(nums):  # 定义函数 findNumberOfLIS（参数：数组）
    # 贪心 + 二分查找（O(n log n)）
    dp = []  # dp[i] 为长度 i+1 的递增子序列的结尾值列表（有序）
    cnt = []  # cnt[i] 为 dp[i] 对应计数的前缀和，cnt[i][0] = 0
    for x in nums:  # 逐个取出 数组 的元素（x）
        # 找到第一个结尾值 >= x 的层级
        i = bisect.bisect_left(
            [lvl[0] for lvl in dp], x
        )  # 把 bisect.bisect_left([lvl[0] for lvl in DP 表], x) 存入 下标 i
        c = 1  # 把 1 存入 字符
        if i > 0:  # 若 下标 i 超过 0
            # 能够接在长度 i 的、结尾 < x 的序列之后
            smaller = bisect.bisect_left(
                dp[i - 1], x
            )  # 把 bisect.bisect_left(DP 表[下标 i 减 1], x) 存入 smaller
            c = cnt[i - 1][smaller]  # 把 计数[下标 i 减 1][smaller] 存入 字符
        if i == len(dp):  # 若 下标 i 等于 长度(DP 表
            dp.append([x])  # 把 [x] 追加到列表尾部
            cnt.append([0, c])  # 把 [0, 字符] 追加到列表尾部
        else:  # 否则
            dp[i].append(x)  # 把 x 追加到列表尾部
            cnt[i].append(cnt[i][-1] + c)  # 把 计数[下标 i][ 减 1] 加 字符 追加到列表尾部
    return cnt[-1][-1] if cnt else 0  # 返回 计数[ 减 1][ 减 1] if 计数 else 0


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(findNumberOfLIS([1, 3, 5, 4, 7]))  # 打印输出
