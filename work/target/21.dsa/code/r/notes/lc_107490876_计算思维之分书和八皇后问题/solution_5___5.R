# 来源：https://blog.csdn.net/tyro_java/article/details/107490876 LeetCode 107490876. 分书和八皇后问题 — R
# 版（方案5：八皇后布尔数组标记，行号 0..n-1） 定义函数 n_queens_bool（参数：元素个数）
n_queens_bool <- function(n) {
    SIZE <- n  # 把 元素个数 存入 SIZE
    OFFSET <- SIZE - 1L  # 把 SIZE 减 1L 存入 OFFSET
    ctx <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 ctx
    ctx$col_row <- rep(0L, SIZE)  # 把 rep(0L, SIZE) 存入 ctx$col_row
    ctx$rows <- rep(TRUE, SIZE)  # 把 rep(TRUE, SIZE) 存入 ctx$rows
    ctx$diag1 <- rep(TRUE, 2L * SIZE - 1L)  # 把 rep(TRUE, 2L 乘 SIZE 减 1L) 存入 ctx$diag1
    ctx$diag2 <- rep(TRUE, 2L * SIZE - 1L)  # 把 rep(TRUE, 2L 乘 SIZE 减 1L) 存入 ctx$diag2
    results <- list()  # 把 列表() 存入 results
    place <- function(col) {
        # 定义函数 place（参数：col） 若 col 等于 SIZE
        if (col == SIZE) {
            results <<- c(results, list(ctx$col_row))  # results 小于 小于 减 字符(results, 列表(ctx$col_row))
            return(invisible(NULL))  # 返回 invisible(NULL
        }
        for (row in 0:(SIZE - 1L)) {
            # for (row in 0:(SIZE 减 1L)) {
            d1 <- col - row + OFFSET + 1L  # R 1 基
            d2 <- col + row + 1L  # 把 col 加 row 加 1L 存入 d2
            if (ctx$rows[row + 1L] && ctx$diag1[d1] && ctx$diag2[d2]) {
                # 若 ctx$行数[row 加 1L] 且 ctx$diag1[d1] 且 ctx$diag2[d2]
                ctx$col_row[col + 1L] <- row  # ctx$col_row[col 加 1L] 小于 减 row
                ctx$rows[row + 1L] <- FALSE  # ctx$行数[row 加 1L] 小于 减 FALSE
                ctx$diag1[d1] <- FALSE  # 把 FALSE 存入 ctx$diag1[d1]
                ctx$diag2[d2] <- FALSE  # 把 FALSE 存入 ctx$diag2[d2]
                place(col + 1L)  # place(col 加 1L)
                ctx$rows[row + 1L] <- TRUE  # ctx$行数[row 加 1L] 小于 减 TRUE
                ctx$diag1[d1] <- TRUE  # 把 TRUE 存入 ctx$diag1[d1]
                ctx$diag2[d2] <- TRUE  # 把 TRUE 存入 ctx$diag2[d2]
            }
        }
    }
    place(0L)  # place(0L)
    results  # results
}
cases <- list(list(8L, 92L, c(0, 4, 7, 5, 2, 6, 1, 3)), list(1L, 1L, c(0)), list(2L, 0L, NULL), list(4L, 2L, c(1,
    3, 0, 2))  # 列表(4L, 2L, 字符(1, 3, 0, 2))
)
for (idx in seq_along(cases)) {
    # for (idx in seq_along(cases)) {
    sols <- n_queens_bool(cases[[idx]][[1]])  # 把 n_queens_bool(cases[[idx]][[1]]) 存入 sols
    stopifnot(length(sols) == cases[[idx]][[2]])  # 断言校验
    if (!is.null(cases[[idx]][[3]])) {
        # 若 取反 is.null(cases[[idx]][[3]]
        stopifnot(identical(as.integer(sols[[1]]), as.integer(cases[[idx]][[3]])))  # 断言校验
    }
}
cat("PASS\n")  # 全部用例通过，输出 PASS
