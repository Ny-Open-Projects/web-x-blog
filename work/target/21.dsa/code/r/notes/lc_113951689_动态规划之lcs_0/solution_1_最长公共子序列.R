# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113951689 LeetCode 113951689. 动态规划之 LCS
# — R 版（最长公共子序列：DP 填表 + 回溯构造）
lcs_table <- function(a, b) {
    # 定义函数 lcs_table（参数：数组, b）
    m <- nchar(a)  # 把 nchar(数组) 存入 映射表
    n <- nchar(b)  # 把 nchar(b) 存入 元素个数
    dp <- matrix(0L, nrow = m + 1L, ncol = n + 1L)  # 把 矩阵(0L, nrow 赋值为 映射表 加 1L, ncol 赋值为 元素个数 加 1L) 存入 DP 表
    if (m >= 1L) {
        # 若 映射表 不低于 1L for (下标 i in 1:映射表) { 若 元素个数 不低于 1L for (下标 j in 1:元素个数) {
        # 若 substr(数组, 下标 i, 下标 i) 等于 substr(b, 下标 j, 下标 j
        for (i in 1:m) {
            if (n >= 1L) {
                for (j in 1:n) {
                  if (substr(a, i, i) == substr(b, j, j)) {
                    dp[i + 1L, j + 1L] <- dp[i, j] + 1L  # DP 表[下标 i 加 1L, 下标 j 加 1L] 小于 减 DP 表[下标 i, 下标 j] 加 1L
                  } else {
                    # 否则
                    dp[i + 1L, j + 1L] <- max(dp[i, j + 1L], dp[i + 1L, j])
                  }
                }
            }
        }
    }
    dp  # DP 表
}
lcs_length <- function(a, b) {
    # 定义函数 lcs_length（参数：数组, b）
    dp <- lcs_table(a, b)  # 把 lcs_table(数组, b) 存入 DP 表
    as.integer(dp[nchar(a) + 1L, nchar(b) + 1L])  # as.integer(DP 表[nchar(数组) 加 1L, nchar(b) 加 1L])
}
lcs_string <- function(a, b) {
    # 定义函数 lcs_string（参数：数组, b）
    dp <- lcs_table(a, b)  # 把 lcs_table(数组, b) 存入 DP 表
    m <- nchar(a)  # 把 nchar(数组) 存入 映射表
    n <- nchar(b)  # 把 nchar(b) 存入 元素个数
    out <- character(0)  # 把 character(0) 存入 out
    i <- m  # 把 映射表 存入 下标 i
    j <- n  # 把 元素个数 存入 下标 j
    while (i > 0L && j > 0L) {
        # 循环，直到不满足「下标 i 超过 0L 且 下标 j 超过 0L」 若 substr(数组, 下标 i, 下标 i) 等于 substr(b,
        # 下标 j, 下标 j
        if (substr(a, i, i) == substr(b, j, j)) {
            out <- c(substr(a, i, i), out)  # 把 字符(substr(数组, 下标 i, 下标 i), out) 存入 out
            i <- i - 1L  # 把 下标 i 减 1L 存入 下标 i
            j <- j - 1L  # 把 下标 j 减 1L 存入 下标 j
        } else if (dp[i, j + 1L] >= dp[i + 1L, j]) {
            # 否则，若 DP 表[下标 i, 下标 j 加 1L] 不低于 DP 表[下标 i 加 1L, 下标 j]
            i <- i - 1L  # 把 下标 i 减 1L 存入 下标 i
        } else {
            # 否则
            j <- j - 1L  # 把 下标 j 减 1L 存入 下标 j
        }
    }
    paste(out, collapse = "")  # 把 「」) 写入 paste(out, collapse
}
is_common_sub <- function(a, b, s) {
    # 定义函数 is_common_sub（参数：数组, b, 字符串）
    ia <- 1L  # 把 1L 存入 ia
    ib <- 1L  # 把 1L 存入 ib
    for (k in 1:nchar(s)) {
        # for (下标 k in 1:nchar(字符串)) {
        ch <- substr(s, k, k)  # 把 substr(字符串, 下标 k, 下标 k) 存入 字符
        while (ia <= nchar(a) && substr(a, ia, ia) != ch) ia <- ia + 1L
        while (ib <= nchar(b) && substr(b, ib, ib) != ch) ib <- ib + 1L
        if (ia > nchar(a) || ib > nchar(b))
            return(FALSE)  # 若 ia 超过 nchar(数组) 或 ib 超过 nchar(b)) return(FALSE
        ia <- ia + 1L  # 把 ia 加 1L 存入 ia
        ib <- ib + 1L  # 把 ib 加 1L 存入 ib
    }
    TRUE  # TRUE
}
cases <- list(list("ABCBDAB", "BDCABA", 4L), list("AGGTAB", "GXTXAYB", 4L), list("abc", "abc", 3L), list("", "abc",
    0L), list("abc", "xyz", 0L)  # 列表(「abc」, 「abc」, 0L)
)
for (idx in seq_along(cases)) {
    # for (idx in seq_along(cases)) {
    got <- lcs_length(cases[[idx]][[1]], cases[[idx]][[2]])  # 把 lcs_length(cases[[idx]][[1]], cases[[idx]][[2]]) 存入 got
    stopifnot(got == cases[[idx]][[3]])  # 断言校验
}
for (p in list(list("ABCBDAB", "BDCABA"), list("AGGTAB", "GXTXAYB"))) {
    s <- lcs_string(p[[1]], p[[2]])  # 把 lcs_string(节点[[1]], 节点[[2]]) 存入 字符串
    stopifnot(nchar(s) == lcs_length(p[[1]], p[[2]]))  # 断言校验
    stopifnot(is_common_sub(p[[1]], p[[2]], s))  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
