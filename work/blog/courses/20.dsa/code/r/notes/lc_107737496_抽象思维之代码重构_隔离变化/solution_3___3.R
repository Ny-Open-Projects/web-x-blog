# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496 LeetCode 107737496.
# 代码重构_隔离变化 — R 版（方案3：螺旋矩阵递归填充）
M <- matrix(0L, nrow = 6L, ncol = 6L)  # 把 矩阵(0L, nrow 赋值为 6L, ncol 赋值为 6L) 存入 M
fill_spiral <- function(num, begin, size) {
    # 定义函数 fill_spiral（参数：num, begin, 大小）
    if (size == 0L)
        return(invisible(num))  # 若 大小 等于 0L) return(invisible(num
    if (size == 1L) {
        # 若 大小 等于 1L
        M[begin + 1L, begin + 1L] <<- num  # M[begin 加 1L, begin 加 1L] 小于 小于 减 num
        return(invisible(num))  # 返回 invisible(num
    }
    for (j in 0:(size - 2L)) {
        # for (下标 j in 0:(大小 减 2L)) {
        M[begin + j + 1L, begin + 1L] <<- num  # M[begin 加 下标 j 加 1L, begin 加 1L] 小于 小于 减 num
        num <- num + 1L  # 把 num 加 1L 存入 num
    }
    for (j in 0:(size - 2L)) {
        # for (下标 j in 0:(大小 减 2L)) {
        M[begin + size, begin + j + 1L] <<- num  # M[begin 加 大小, begin 加 下标 j 加 1L] 小于 小于 减 num
        num <- num + 1L  # 把 num 加 1L 存入 num
    }
    for (j in (size - 1L):1L) {
        # for (下标 j in (大小 减 1L):1L) {
        M[begin + j + 1L, begin + size] <<- num  # M[begin 加 下标 j 加 1L, begin 加 大小] 小于 小于 减 num
        num <- num + 1L  # 把 num 加 1L 存入 num
    }
    for (j in (size - 1L):1L) {
        # for (下标 j in (大小 减 1L):1L) {
        M[begin + 1L, begin + j + 1L] <<- num  # M[begin 加 1L, begin 加 下标 j 加 1L] 小于 小于 减 num
        num <- num + 1L  # 把 num 加 1L 存入 num
    }
    fill_spiral(num, begin + 1L, size - 2L)  # fill_spiral(num, begin 加 1L, 大小 减 2L)
    invisible(NULL)  # invisible(NULL)
}
fmt_row <- function(row) paste(sprintf("%2d", row), collapse = " ")  # 定义函数 fmt_row（参数：row）
fill_spiral(1L, 0L, 6L)  # fill_spiral(1L, 0L, 6L)
want <- c(" 1 20 19 18 17 16", " 2 21 32 31 30 15", " 3 22 33 36 29 14", " 4 23 34 35 28 13", " 5 24 25 26 27 12",
    " 6  7  8  9 10 11"  # 「 6 7 8 9 10 11」
)
for (i in 1:6) {
    # for (下标 i in 1:6) {
    got <- fmt_row(M[i, ])  # 把 fmt_row(M[下标 i, ]) 存入 got
    stopifnot(identical(got, want[i]))  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
