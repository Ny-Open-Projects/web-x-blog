# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013 LeetCode 116567013. PM — R
# 版（方案2：Brute-Force 双循环对齐） 定义函数 match_v2（参数：节点, 另一字符串）
match_v2 <- function(p, t) {
    n <- nchar(t)
    m <- nchar(p)  # 把 nchar(另一字符串); 映射表 小于 减 nchar(节点) 存入 元素个数
    if (m == 0L || n < m)
        return(-1L)  # 若 映射表 等于 0L 或 元素个数 小于 映射表) return( 减 1L
    for (i in 1:(n - m + 1L)) {
        # for (下标 i in 1:(元素个数 减 映射表 加 1L)) {
        j <- 1L  # 把 1L 存入 下标 j
        while (j <= m && substr(t, i + j - 1L, i + j - 1L) == substr(p, j, j)) {
            j <- j + 1L  # 把 下标 j 加 1L 存入 下标 j
        }
        if (j > m)
            return(i - 1L)  # 若 下标 j 超过 映射表) return(下标 i 减 1L
    }
    -1L  # 减 1L
}
T <- "now is the time for all good people to come"  # 把 「now is the time for all good people to come」 存入 T
cases <- list(list("people", T, 29L), list("time", T, 11L), list("all", T, 20L), list("xyz", T, -1L), list("a",
    "", -1L), list("is", T, 4L)  # 列表(「xyz」, T, 减 1L), 列表(「xyz」, 「xyz」, 减 1L), 列表(「xyz」, T, 4L)
)
for (idx in seq_along(cases)) {
    # for (idx in seq_along(cases)) {
    got <- match_v2(cases[[idx]][[1]], cases[[idx]][[2]])  # 把 match_v2(cases[[idx]][[1]], cases[[idx]][[2]]) 存入 got
    stopifnot(got == cases[[idx]][[3]])  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
