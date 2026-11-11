# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130641517 LeetCode 62. 不同路径 — R
# 版（方案1） 定义函数 unique_paths（参数：映射表, 元素个数）
unique_paths <- function(m, n) {
    dp <- rep(1L, n)  # 把 rep(1L, 元素个数) 存入 DP 表
    if (m >= 2 && n >= 2) {
        # 若 映射表 不低于 2 且 元素个数 不低于 2
        for (i in 2:m) for (j in 2:n) dp[j] <- dp[j] + dp[j - 1]
    }
    dp[n]  # DP 表[元素个数]
}
stopifnot(unique_paths(3, 7) == 28)  # 断言校验
stopifnot(unique_paths(3, 2) == 3)  # 断言校验
stopifnot(unique_paths(1, 1) == 1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
