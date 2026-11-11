# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107579658 LeetCode 107579658.
# 转换视角，提炼共性 — R 版（抽象思维之转换视角：统一分书问题与八皇后的回溯框架） queen=FALSE:
# 分书问题（5人，like 偏好矩阵）; queen=TRUE: 八皇后
LIKE <- matrix(c(0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1  # 0, 1, 0, 0, 1
),
    nrow = 5, byrow = TRUE)  # 把 5, byrow 赋值为 TRUE) 写入 ), nrow
solve_unified <- function(queen) {
    # 定义函数 solve_unified（参数：queen）
    SIZE <- if (queen)
        8L else 5L  # 把 if (queen) 8L else 5L 存入 SIZE
    ctx <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 ctx
    ctx$Q <- rep(-1L, SIZE)  # 把 rep( 减 1L, SIZE) 存入 ctx$Q
    ctx$rows <- rep(TRUE, SIZE)  # 把 rep(TRUE, SIZE) 存入 ctx$rows
    ctx$diag1 <- rep(TRUE, 2L * SIZE - 1L)  # 把 rep(TRUE, 2L 乘 SIZE 减 1L) 存入 ctx$diag1
    ctx$diag2 <- rep(TRUE, 2L * SIZE - 1L)  # 把 rep(TRUE, 2L 乘 SIZE 减 1L) 存入 ctx$diag2
    results <- list()  # 把 列表() 存入 results
    is_valid <- function(row, col) {
        # 定义函数 is_valid（参数：row, col）
        if (queen)
            return(TRUE)  # 若 queen) return(TRUE
        LIKE[row + 1L, col + 1L] == 1  # 把 赋值为 1 写入 LIKE[row + 1L, col + 1L]
    }
    is_safe <- function(row, col) {
        # 定义函数 is_safe（参数：row, col） 若 queen
        if (queen) {
            ctx$rows[row + 1L] && ctx$diag1[col - row + SIZE] && ctx$diag2[col + row + 1L]
        } else {
            # 否则
            ctx$rows[row + 1L]  # ctx$行数[row 加 1L]
        }
    }
    place <- function(col) {
        # 定义函数 place（参数：col） 若 col 等于 SIZE
        if (col == SIZE) {
            results <<- c(results, list(ctx$Q))  # results 小于 小于 减 字符(results, 列表(ctx$Q))
            return(invisible(NULL))  # 返回 invisible(NULL
        }
        for (row in 0:(SIZE - 1L)) {
            # for (row in 0:(SIZE 减 1L)) {
            if (!is_valid(row, col))
                next  # 若 取反 is_valid(row, col)) 下一个
            if (!is_safe(row, col))
                next  # 若 取反 is_safe(row, col)) 下一个
            ctx$Q[col + 1L] <- row  # ctx$Q[col 加 1L] 小于 减 row
            ctx$rows[row + 1L] <- FALSE  # ctx$行数[row 加 1L] 小于 减 FALSE
            if (queen) {
                # 若 queen
                ctx$diag1[col - row + SIZE] <- FALSE  # ctx$diag1[col 减 row 加 SIZE] 小于 减 FALSE
                ctx$diag2[col + row + 1L] <- FALSE  # ctx$diag2[col 加 row 加 1L] 小于 减 FALSE
            }
            place(col + 1L)  # place(col 加 1L)
            ctx$rows[row + 1L] <- TRUE  # ctx$行数[row 加 1L] 小于 减 TRUE
            if (queen) {
                # 若 queen
                ctx$diag1[col - row + SIZE] <- TRUE  # ctx$diag1[col 减 row 加 SIZE] 小于 减 TRUE
                ctx$diag2[col + row + 1L] <- TRUE  # ctx$diag2[col 加 row 加 1L] 小于 减 TRUE
            }
        }
    }
    place(0L)  # place(0L)
    results  # results
}
want <- list(c(1L, 2L, 0L, 3L, 4L), c(1L, 4L, 0L, 3L, 2L))  # 把 列表(字符(1L, 2L, 0L, 3L, 4L), 字符(1L, 4L, 0L, 3L, 2L)) 存入 want
got <- solve_unified(FALSE)  # 把 solve_unified(FALSE) 存入 got
stopifnot(length(got) == 2L)  # 断言校验
for (i in 1:2) {
    # for (下标 i in 1:2) {
    stopifnot(identical(as.integer(got[[i]]), as.integer(want[[i]])))  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
