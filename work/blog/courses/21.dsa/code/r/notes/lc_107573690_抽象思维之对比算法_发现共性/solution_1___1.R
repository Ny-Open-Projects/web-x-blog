# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107573690 抽象思维之对比算法 发现共性 — R
# 版（方案1） 定义函数 climb_stairs_refactored（参数：元素个数）
climb_stairs_refactored <- function(n) {
    if (n == 0)
        return(1)  # 若 元素个数 等于 0) return(1
    if (n < 0)
        return(0)  # 若 元素个数 小于 0) return(0
    dp <- rep(0, n + 1)  # 把 rep(0, 元素个数 加 1) 存入 DP 表
    dp[1] <- 1  # 把 1 存入 dp[1]
    for (i in 1:n) {
        # for (下标 i in 1:元素个数) {
        dp[i + 1] <- dp[i]  # DP 表[下标 i 加 1] 小于 减 DP 表[下标 i]
        if (i >= 2)
            dp[i + 1] <- dp[i + 1] + dp[i - 1]
        if (i >= 3)
            dp[i + 1] <- dp[i + 1] + dp[i - 2]
    }
    dp[n + 1]  # DP 表[元素个数 加 1]
}
stopifnot(climb_stairs_refactored(10) == 274, climb_stairs_refactored(3) == 4)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
