# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130683917 LeetCode 322. 零钱兑换 — R
# 版（方案3） 定义函数 coin_change（参数：硬币面额, 目标金额）
coin_change <- function(coins, amount) {
    dp <- rep(Inf, amount + 1)  # 把 rep(Inf, 目标金额 加 1) 存入 DP 表
    dp[1] <- 0  # 把 0 存入 dp[1]
    for (a in 1:amount) {
        # for (数组 in 1:目标金额) { for (字符 in 硬币面额) { 若 字符 不超过 数组 且 is.finite(DP 表[数组 减
        # 字符 加 1]
        for (c in coins) {
            if (c <= a && is.finite(dp[a - c + 1])) {
                dp[a + 1] <- min(dp[a + 1], dp[a - c + 1] + 1)  # DP 表[数组 加 1] 小于 减 取较小值 DP 表[数组 加 1], DP 表[数组 减 字符 加 1] 加 1)
            }
        }
    }
    if (is.infinite(dp[amount + 1]))
        -1L else as.integer(dp[amount + 1])
}
stopifnot(coin_change(c(1, 2, 5), 11) == 3)  # 断言校验
stopifnot(coin_change(c(2), 3) == -1)  # 断言校验
stopifnot(coin_change(c(1), 0) == 0)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
