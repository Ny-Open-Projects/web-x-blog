# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133625091
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def nthSuperUglyNumber(n, primes):  # 定义函数 nthSuperUglyNumber（参数：元素个数, primes）
    dp = [0] * (n + 1)  # 把 [0] 乘 (元素个数 加 1) 存入 DP 表
    m = len(primes)  # 把 长度(primes) 存入 映射表
    pointers = [0] * m  # 每个素数对应的 dp 指针
    nums = [1] * m  # 每个素数当前乘积候选
    for i in range(1, n + 1):  # 让 下标 i 从 1 到 元素个数 加 1 遍历
        min_num = min(nums)  # 把 取较小值 数组) 存入 min_num
        dp[i] = min_num  # 把 min_num 写入 dp[i]
        for j in range(m):  # 让 下标 j 从 映射表 遍历
            if nums[j] == min_num:  # 若 数组[下标 j] 等于 min_num
                pointers[j] += 1  # pointers[j]累加 1
                nums[j] = (
                    dp[pointers[j]] * primes[j]
                )  # 把 DP 表[pointers[下标 j]] 乘 primes[下标 j] 写入 nums[j]
    return dp[n]  # 返回 DP 表[元素个数]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(nthSuperUglyNumber(12, [2, 7, 13, 19]))  # 打印输出
