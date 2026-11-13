# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130771847 LeetCode 673. 最长递增子序列的个数
# — R 版（方案2） 定义函数 find_number_of_lis（参数：数组）
find_number_of_lis <- function(nums) {
    n <- length(nums)  # 把 长度(数组) 存入 元素个数
    dp <- rep(1L, n)
    cnt <- rep(1L, n)  # 把 rep(1L, 元素个数); 计数 小于 减 rep(1L, 元素个数) 存入 DP 表
    best <- 0L
    res <- 0L  # 把 0L; 结果 小于 减 0L 存入 当前最优
    for (i in seq_len(n)) {
        # for (下标 i in seq_len(元素个数)) { for (下标 j in seq_len(下标 i 减 1)) { 若 数组[下标 j] 小于
        # 数组[下标 i]
        for (j in seq_len(i - 1)) {
            if (nums[j] < nums[i]) {
                if (dp[j] + 1L > dp[i]) {
                  dp[i] <- dp[j] + 1L
                  cnt[i] <- cnt[j]
                } else if (dp[j] + 1L == dp[i])
                  cnt[i] <- cnt[i] + cnt[j]
            }
        }
        if (dp[i] > best) {
            best <- dp[i]
            res <- cnt[i]
        } else if (dp[i] == best)
            res <- res + cnt[i]  # 否则，若 DP 表[下标 i] 等于 当前最优) 结果 小于 减 结果 加 计数[下标 i]
    }
    res  # 结果
}
stopifnot(find_number_of_lis(c(1, 3, 5, 4, 7)) == 2)  # 断言校验
stopifnot(find_number_of_lis(c(2, 2, 2, 2, 2)) == 5)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
