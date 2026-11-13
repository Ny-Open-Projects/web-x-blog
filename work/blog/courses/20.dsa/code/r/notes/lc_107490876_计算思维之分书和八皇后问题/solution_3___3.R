# 来源：https://blog.csdn.net/tyro_java/article/details/107490876 LeetCode 107490876. 分书和八皇后问题 — R
# 版（方案3：八皇后递归 isSafe，行号 1..n） 定义函数 n_queens_safe（参数：元素个数）
n_queens_safe <- function(n) {
    results <- list()  # 把 列表() 存入 results
    board <- rep(0L, n)  # 把 rep(0L, 元素个数) 存入 棋盘
    is_safe <- function(col, row) {
        # 定义函数 is_safe（参数：col, row）
        if (col == 1L)
            return(TRUE)  # 若 col 等于 1L) return(TRUE
        for (c in 1:(col - 1L)) {
            # for (字符 in 1:(col 减 1L)) {
            if (board[c] == row || abs(board[c] - row) == abs(c - col))
                return(FALSE)
        }
        TRUE  # TRUE
    }
    place <- function(col) {
        # 定义函数 place（参数：col） 若 col 超过 元素个数
        if (col > n) {
            results <<- c(results, list(board))  # results 小于 小于 减 字符(results, 列表(棋盘))
            return(invisible(NULL))  # 返回 invisible(NULL
        }
        for (row in 1:n) {
            # for (row in 1:元素个数) { 若 is_safe(col, row
            if (is_safe(col, row)) {
                board[col] <<- row  # 棋盘[col] 小于 小于 减 row
                place(col + 1L)  # place(col 加 1L)
            }
        }
    }
    place(1L)  # place(1L)
    results  # results
}
cases <- list(list(8L, 92L, c(1, 5, 8, 6, 3, 7, 2, 4)), list(1L, 1L, c(1)), list(2L, 0L, NULL), list(4L, 2L, c(2,
    4, 1, 3))  # 列表(4L, 2L, 字符(2, 4, 1, 3))
)
for (idx in seq_along(cases)) {
    # for (idx in seq_along(cases)) {
    sols <- n_queens_safe(cases[[idx]][[1]])  # 把 n_queens_safe(cases[[idx]][[1]]) 存入 sols
    stopifnot(length(sols) == cases[[idx]][[2]])  # 断言校验
    if (!is.null(cases[[idx]][[3]])) {
        # 若 取反 is.null(cases[[idx]][[3]]
        stopifnot(identical(as.integer(sols[[1]]), as.integer(cases[[idx]][[3]])))  # 断言校验
    }
}
cat("PASS\n")  # 全部用例通过，输出 PASS
