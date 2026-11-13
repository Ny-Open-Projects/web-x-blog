# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130613988 LeetCode 583. 两个字符串的删除操作
# — R 版（方案2） 定义函数 min_distance_del（参数：w1, w2）
min_distance_del <- function(w1, w2) {
    chars1 <- strsplit(w1, "")[[1]]  # 把 strsplit(w1, 「」)[[1]] 存入 chars1
    chars2 <- strsplit(w2, "")[[1]]  # 把 strsplit(w2, 「」)[[1]] 存入 chars2
    m <- length(chars1)
    n <- length(chars2)  # 把 长度(chars1); 元素个数 小于 减 长度(chars2) 存入 映射表
    dp <- 0:n  # 把 0:元素个数 存入 DP 表
    for (i in 1:m) {
        # for (下标 i in 1:映射表) {
        prev_diag <- dp[1]  # 把 DP 表[1] 存入 prev_diag
        dp[1] <- i  # 把 下标 i 存入 dp[1]
        for (j in 1:n) {
            # for (下标 j in 1:元素个数) {
            tmp <- dp[j + 1]  # 把 DP 表[下标 j 加 1] 存入 临时变量
            dp[j + 1] <- if (chars1[i] == chars2[j])
                prev_diag else 1 + min(prev_diag, dp[j + 1], dp[j])
            prev_diag <- tmp  # 把 临时变量 存入 prev_diag
        }
    }
    dp[n + 1]  # DP 表[元素个数 加 1]
}
stopifnot(min_distance_del("sea", "eat") == 2)  # 断言校验
stopifnot(min_distance_del("leetcode", "etco") == 4)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
