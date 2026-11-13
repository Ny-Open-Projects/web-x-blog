# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013 LeetCode 116567013. PM — R
# 版（方案1：Brute-Force 主串指针回退） 定义函数 match_v1（参数：节点, 另一字符串）
match_v1 <- function(p, t) {
    n <- nchar(t)
    m <- nchar(p)  # 把 nchar(另一字符串); 映射表 小于 减 nchar(节点) 存入 元素个数
    i <- 1L
    j <- 1L  # 把 1L; 下标 j 小于 减 1L 存入 下标 i
    while (j <= m && i <= n) {
        # 循环，直到不满足「下标 j 不超过 映射表 且 下标 i 不超过 元素个数」 若 substr(另一字符串, 下标 i,
        # 下标 i) 等于 substr(节点, 下标 j, 下标 j
        if (substr(t, i, i) == substr(p, j, j)) {
            i <- i + 1L
            j <- j + 1L  # 把 下标 i 加 1L; 下标 j 小于 减 下标 j 加 1L 存入 下标 i
        } else {
            # 否则
            i <- i - j + 2L  # 主串回退（1 基）
            j <- 1L  # 把 1L 存入 下标 j
        }
    }
    if (j > m)
        return(i - j)  # 若 下标 j 超过 映射表) return(下标 i 减 下标 j
    -1L  # 减 1L
}
T <- "now is the time for all good people to come"  # 把 「now is the time for all good people to come」 存入 T
cases <- list(list("people", T, 29L), list("good", T, 24L), list("xyz", T, -1L), list("a", "", -1L), list("is",
    T, 4L)  # 列表(「is」, T, 4L)
)
for (idx in seq_along(cases)) {
    # for (idx in seq_along(cases)) {
    got <- match_v1(cases[[idx]][[1]], cases[[idx]][[2]])  # 把 match_v1(cases[[idx]][[1]], cases[[idx]][[2]]) 存入 got
    stopifnot(got == cases[[idx]][[3]])  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
