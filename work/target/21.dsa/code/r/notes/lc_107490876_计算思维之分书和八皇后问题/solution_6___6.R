# 来源：https://blog.csdn.net/tyro_java/article/details/107490876 LeetCode 107490876. 分书和八皇后问题 — R
# 版（方案6：八皇后不可变状态函数式） 定义函数 n_queens_func（参数：元素个数）
n_queens_func <- function(n) {
    SIZE <- n  # 把 元素个数 存入 SIZE
    results <- list()  # 把 列表() 存入 results
    place <- function(col, col_row, rows, diag1, diag2) {
        # 定义函数 place（参数：col, col_row, 行数, diag1, diag2） 若 col 等于 SIZE
        if (col == SIZE) {
            results <<- c(results, list(col_row))  # results 小于 小于 减 字符(results, 列表(col_row))
            return(invisible(NULL))  # 返回 invisible(NULL
        }
        for (row in 0:(SIZE - 1L)) {
            # for (row in 0:(SIZE 减 1L)) {
            d1 <- col - row + SIZE  # R 1 基
            d2 <- col + row + 1L  # 把 col 加 row 加 1L 存入 d2
            if (rows[row + 1L] && diag1[d1] && diag2[d2]) {
                # 若 行数[row 加 1L] 且 diag1[d1] 且 diag2[d2]
                nr <- rows
                nr[row + 1L] <- FALSE  # 把 行数; nr[row 加 1L] 小于 减 FALSE 存入 nr
                nd1 <- diag1
                nd1[d1] <- FALSE  # 把 diag1; nd1[d1] 小于 减 FALSE 存入 nd1
                nd2 <- diag2
                nd2[d2] <- FALSE  # 把 diag2; nd2[d2] 小于 减 FALSE 存入 nd2
                place(col + 1L, c(col_row, row), nr, nd1, nd2)  # place(col 加 1L, 字符(col_row, row), nr, nd1, nd2)
            }
        }
    }
    rows0 <- rep(TRUE, SIZE)  # 把 rep(TRUE, SIZE) 存入 rows0
    diag0 <- rep(TRUE, 2L * SIZE - 1L)  # 把 rep(TRUE, 2L 乘 SIZE 减 1L) 存入 diag0
    place(0L, integer(0), rows0, diag0, diag0)  # place(0L, integer(0), rows0, diag0, diag0)
    results  # results
}
cases <- list(list(8L, 92L, c(0, 4, 7, 5, 2, 6, 1, 3)), list(1L, 1L, c(0)), list(2L, 0L, NULL), list(4L, 2L, c(1,
    3, 0, 2))  # 列表(4L, 2L, 字符(1, 3, 0, 2))
)
for (idx in seq_along(cases)) {
    # for (idx in seq_along(cases)) {
    sols <- n_queens_func(cases[[idx]][[1]])  # 把 n_queens_func(cases[[idx]][[1]]) 存入 sols
    stopifnot(length(sols) == cases[[idx]][[2]])  # 断言校验
    if (!is.null(cases[[idx]][[3]])) {
        # 若 取反 is.null(cases[[idx]][[3]]
        stopifnot(identical(as.integer(sols[[1]]), as.integer(cases[[idx]][[3]])))  # 断言校验
    }
}
cat("PASS\n")  # 全部用例通过，输出 PASS
