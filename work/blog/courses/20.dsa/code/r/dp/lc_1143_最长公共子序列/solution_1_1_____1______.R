# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631 LeetCode 1143. 最长公共子序列 — R
# 版（方案1） 定义函数 lcs_len（参数：t1, t2）
lcs_len <- function(t1, t2) {
    chars1 <- strsplit(t1, "")[[1]]  # 把 strsplit(t1, 「」)[[1]] 存入 chars1
    chars2 <- strsplit(t2, "")[[1]]  # 把 strsplit(t2, 「」)[[1]] 存入 chars2
    m <- length(chars1)
    n <- length(chars2)  # 把 长度(chars1); 元素个数 小于 减 长度(chars2) 存入 映射表
    dp <- rep(0L, n + 1)  # 把 rep(0L, 元素个数 加 1) 存入 DP 表
    for (i in 1:m) {
        # for (下标 i in 1:映射表) {
        prev_diag <- 0L  # 把 0L 存入 prev_diag
        for (j in 1:n) {
            # for (下标 j in 1:元素个数) {
            tmp <- dp[j + 1]  # 把 DP 表[下标 j 加 1] 存入 临时变量
            dp[j + 1] <- if (chars1[i] == chars2[j])
                prev_diag + 1L else max(dp[j + 1], dp[j])
            prev_diag <- tmp  # 把 临时变量 存入 prev_diag
        }
    }
    dp[n + 1]  # DP 表[元素个数 加 1]
}
stopifnot(lcs_len("abcde", "ace") == 3)  # 断言校验
stopifnot(lcs_len("abc", "abc") == 3)  # 断言校验
stopifnot(lcs_len("abc", "def") == 0)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
