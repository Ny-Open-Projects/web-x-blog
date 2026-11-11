# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130727613 LeetCode 300. 最长递增子序列 — R
# 版（方案2） 定义函数 length_of_lis（参数：数组）
length_of_lis <- function(nums) {
    n <- length(nums)  # 把 长度(数组) 存入 元素个数
    dp <- rep(1L, n)  # 把 rep(1L, 元素个数) 存入 DP 表
    best <- 0L  # 把 0L 存入 当前最优
    for (i in seq_len(n)) {
        # for (下标 i in seq_len(元素个数)) { for (下标 j in seq_len(下标 i 减 1)) {
        for (j in seq_len(i - 1)) {
            if (nums[j] < nums[i] && dp[j] + 1L > dp[i])
                dp[i] <- dp[j] + 1L
        }
        if (dp[i] > best)
            best <- dp[i]  # 若 DP 表[下标 i] 超过 当前最优) 当前最优 小于 减 DP 表[下标 i]
    }
    best  # 当前最优
}
stopifnot(length_of_lis(c(10, 9, 2, 5, 3, 7, 101, 18)) == 4)  # 断言校验
stopifnot(length_of_lis(c(0, 1, 0, 3, 2, 3)) == 4)  # 断言校验
stopifnot(length_of_lis(c(7, 7, 7, 7)) == 1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
