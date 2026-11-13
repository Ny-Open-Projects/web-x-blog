# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130590161 LeetCode 115. 不同的子序列 — R
# 版（方案2） 定义函数 num_distinct（参数：字符串, 另一字符串）
num_distinct <- function(s, t) {
    chars_s <- strsplit(s, "")[[1]]  # 把 strsplit(字符串, 「」)[[1]] 存入 chars_s
    chars_t <- strsplit(t, "")[[1]]  # 把 strsplit(另一字符串, 「」)[[1]] 存入 chars_t
    m <- length(chars_s)
    n <- length(chars_t)  # 把 长度(chars_s); 元素个数 小于 减 长度(chars_t) 存入 映射表
    dp <- c(1L, rep(0L, n))  # 把 字符(1L, rep(0L, 元素个数)) 存入 DP 表
    for (i in 1:m) {
        # for (下标 i in 1:映射表) { for (下标 j in 元素个数:1) {
        for (j in n:1) {
            if (chars_s[i] == chars_t[j])
                dp[j + 1] <- dp[j + 1] + dp[j]
        }
    }
    dp[n + 1]  # DP 表[元素个数 加 1]
}
stopifnot(num_distinct("rabbbit", "rabbit") == 3)  # 断言校验
stopifnot(num_distinct("babgbag", "bag") == 5)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
