# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496 LeetCode 107737496.
# 代码重构_隔离变化 — R 版（方案7：螺旋矩阵分派表 place） 定义函数 place_step（参数：row, col, direction,
# 元素个数, 映射表）
place_step <- function(row, col, direction, n, m) {
    handlers <- list(D = function() {
        # 把 function() { 存入 D
        if (row + 1L <= n && m[row + 1L, col] == 0L) return(list(row + 1L, col, NULL))
        list(row, col + 1L, "R")  # 列表(row, col 加 1L, 「R」)
    }, R = function() {
        # 把 function() { 存入 R
        if (col + 1L <= n && m[row, col + 1L] == 0L) return(list(row, col + 1L, NULL))
        list(row - 1L, col, "U")  # 列表(row 减 1L, col, 「U」)
    }, U = function() {
        # 把 function() { 存入 U
        if (row - 1L >= 1L && m[row - 1L, col] == 0L) return(list(row - 1L, col, NULL))
        list(row, col - 1L, "L")  # 列表(row, col 减 1L, 「L」)
    }, L = function() {
        # 把 function() { 存入 L
        if (col - 1L >= 1L && m[row, col - 1L] == 0L) return(list(row, col - 1L, NULL))
        list(row + 1L, col, "D")  # 列表(row 加 1L, col, 「D」)
    })
    handlers[[direction]]()  # handlers[[direction]]()
}
fill_spiral <- function(n) {
    # 定义函数 fill_spiral（参数：元素个数）
    m <- matrix(0L, nrow = n, ncol = n)  # 把 矩阵(0L, nrow 赋值为 元素个数, ncol 赋值为 元素个数) 存入 映射表
    row <- 1L
    col <- 1L  # 把 1L; col 小于 减 1L 存入 row
    direction <- "D"  # 把 「D」 存入 direction
    num <- 1L  # 把 1L 存入 num
    while (num <= n * n) {
        # 循环，直到不满足「num 不超过 元素个数 乘 元素个数」
        m[row, col] <- num  # 映射表[row, col] 小于 减 num
        num <- num + 1L  # 把 num 加 1L 存入 num
        res <- place_step(row, col, direction, n, m)  # 把 place_step(row, col, direction, 元素个数, 映射表) 存入 结果
        row <- res[[1]]  # 把 结果[[1]] 存入 row
        col <- res[[2]]  # 把 结果[[2]] 存入 col
        if (!is.null(res[[3]]))
            direction <- res[[3]]  # 若 取反 is.null(结果[[3]])) direction 小于 减 结果[[3]]
    }
    m  # 映射表
}
got3 <- fill_spiral(3L)  # 把 fill_spiral(3L) 存入 got3
want3 <- matrix(c(1, 8, 7, 2, 9, 6, 3, 4, 5), nrow = 3, byrow = TRUE)
stopifnot(identical(as.integer(got3), as.integer(want3)))  # 断言校验
got4 <- fill_spiral(4L)  # 把 fill_spiral(4L) 存入 got4
want4 <- matrix(c(1, 12, 11, 10, 2, 13, 16, 9, 3, 14, 15, 8, 4, 5, 6, 7), nrow = 4, byrow = TRUE)
stopifnot(identical(as.integer(got4), as.integer(want4)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
