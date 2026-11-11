# 来源：https://blog.csdn.net/tyro_java/article/details/107490876 LeetCode 107490876. 分书和八皇后问题 — R
# 版（方案7：八皇后位置对列表） 定义函数 n_queens_simple（参数：元素个数）
n_queens_simple <- function(n) {
    positions <- list()  # list(c(row, col), ...)
    solutions <- list()  # 把 列表() 存入 solutions
    safe <- function(r, c) {
        # 定义函数 safe（参数：右指针, 字符） for (节点 in positions) {
        for (p in positions) {
            if (p[1] == r || abs(p[1] - r) == abs(p[2] - c))
                return(FALSE)
        }
        TRUE  # TRUE
    }
    solve <- function(col) {
        # 定义函数 solve（参数：col） 若 col 等于 元素个数
        if (col == n) {
            solutions <<- c(solutions, list(vapply(positions, function(p) p[1], integer(1))))
            return(invisible(NULL))  # 返回 invisible(NULL
        }
        for (r in 0:(n - 1L)) {
            # for (右指针 in 0:(元素个数 减 1L)) { 若 safe(右指针, col
            if (safe(r, col)) {
                positions <<- c(positions, list(c(r, col)))  # positions 小于 小于 减 字符(positions, 列表(字符(右指针, col)))
                solve(col + 1L)  # solve(col 加 1L)
                positions <<- positions[-length(positions)]  # positions 小于 小于 减 positions[ 减 长度(positions)]
            }
        }
    }
    solve(0L)  # solve(0L)
    solutions  # solutions
}
cases <- list(list(8L, 92L, c(0, 4, 7, 5, 2, 6, 1, 3)), list(1L, 1L, c(0)), list(2L, 0L, NULL), list(4L, 2L, c(1,
    3, 0, 2))  # 列表(4L, 2L, 字符(1, 3, 0, 2))
)
for (idx in seq_along(cases)) {
    # for (idx in seq_along(cases)) {
    sols <- n_queens_simple(cases[[idx]][[1]])  # 把 n_queens_simple(cases[[idx]][[1]]) 存入 sols
    stopifnot(length(sols) == cases[[idx]][[2]])  # 断言校验
    if (!is.null(cases[[idx]][[3]])) {
        # 若 取反 is.null(cases[[idx]][[3]]
        stopifnot(identical(as.integer(sols[[1]]), as.integer(cases[[idx]][[3]])))  # 断言校验
    }
}
cat("PASS\n")  # 全部用例通过，输出 PASS
