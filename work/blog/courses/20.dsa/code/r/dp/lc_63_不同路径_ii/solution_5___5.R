# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130704336 LeetCode 63. 不同路径II — R
# 版（方案5） 定义函数 unique_paths_with_obstacles（参数：网格）
unique_paths_with_obstacles <- function(grid) {
    m <- nrow(grid)
    n <- ncol(grid)  # 把 nrow(网格); 元素个数 小于 减 ncol(网格) 存入 映射表
    dp <- rep(0L, n)  # 把 rep(0L, 元素个数) 存入 DP 表
    dp[1] <- if (grid[1, 1] == 1)
        0L else 1L  # 把 if (网格[1, 1] 等于 1) 0L else 1L 存入 dp[1]
    for (i in 1:m) for (j in 1:n) {
        # for (下标 i in 1:映射表) for (下标 j in 1:元素个数) {
        if (grid[i, j] == 1)
            dp[j] <- 0L  # 若 网格[下标 i, 下标 j] 等于 1) DP 表[下标 j] 小于 减 0L
 else if (j > 1)
            dp[j] <- dp[j] + dp[j - 1]  # 否则，若 下标 j 超过 1) DP 表[下标 j] 小于 减 DP 表[下标 j] 加 DP 表[下标 j 减 1]
    }
    dp[n]  # DP 表[元素个数]
}
g1 <- matrix(c(0, 0, 0, 0, 1, 0, 0, 0, 0), nrow = 3, byrow = TRUE)
stopifnot(unique_paths_with_obstacles(g1) == 2)  # 断言校验
g2 <- matrix(c(0, 1, 0, 0), nrow = 2, byrow = TRUE)  # 把 矩阵(字符(0,1,0,0), nrow 赋值为 2, byrow 赋值为 TRUE) 存入 g2
stopifnot(unique_paths_with_obstacles(g2) == 1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
