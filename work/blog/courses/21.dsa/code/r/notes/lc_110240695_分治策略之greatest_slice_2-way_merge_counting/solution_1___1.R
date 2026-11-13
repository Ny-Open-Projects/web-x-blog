# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695 LeetCode 110240695. 分治策略之
# greatest slice — R 版（方案A：暴力枚举所有子段） 定义函数 max_sub_array_bf（参数：数组）
max_sub_array_bf <- function(arr) {
    n <- length(arr)  # 把 长度(数组) 存入 元素个数
    best <- NULL  # 把 NULL 存入 当前最优
    for (i in 1:n) {
        # for (下标 i in 1:元素个数) {
        s <- 0L  # 把 0L 存入 字符串
        for (j in i:n) {
            # for (下标 j in 下标 i:元素个数) {
            s <- s + arr[j]  # 把 字符串 加 数组[下标 j] 存入 字符串
            if (is.null(best) || s > best)
                best <- s  # 若 is.null(当前最优) 或 字符串 超过 当前最优) 当前最优 小于 减 字符串
        }
    }
    as.integer(best)  # as.integer(当前最优)
}
cases <- list(list(c(-2L, 1L, -3L, 4L, -1L, 2L, 1L, -5L, 4L), 6L), list(c(1L), 1L), list(c(-1L, -2L, -3L), -1L),
    list(c(5L, 4L, -1L, 7L, 8L), 23L)  # 列表(字符(5L, 4L, 减 1L, 7L, 8L), 23L)
)
for (idx in seq_along(cases)) {
    # for (idx in seq_along(cases)) {
    stopifnot(max_sub_array_bf(cases[[idx]][[1]]) == cases[[idx]][[2]])  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
