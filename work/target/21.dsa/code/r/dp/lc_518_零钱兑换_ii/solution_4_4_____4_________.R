# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734179 LeetCode 518. 零钱兑换II — R
# 版（方案4） 定义函数 change_ways（参数：目标金额, 硬币面额）
change_ways <- function(amount, coins) {
    dp <- rep(0L, amount + 1)  # 把 rep(0L, 目标金额 加 1) 存入 DP 表
    dp[1] <- 1L  # 把 1L 存入 dp[1]
    for (c in coins) {
        # for (字符 in 硬币面额) { 若 字符 不超过 目标金额
        if (c <= amount) {
            for (a in c:amount) dp[a + 1] <- dp[a + 1] + dp[a - c + 1]
        }
    }
    dp[amount + 1]  # DP 表[目标金额 加 1]
}
stopifnot(change_ways(5, c(1, 2, 5)) == 4)  # 断言校验
stopifnot(change_ways(3, c(2)) == 0)  # 断言校验
stopifnot(change_ways(10, c(1, 2, 5)) == 10)  # 断言校验
stopifnot(change_ways(0, c(1, 2)) == 1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
