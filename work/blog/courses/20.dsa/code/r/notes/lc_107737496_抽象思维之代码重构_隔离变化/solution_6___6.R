# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496 LeetCode 107737496.
# 代码重构_隔离变化 — R 版（方案6：Matrix 公开 buf 直接访问） 定义函数 Matrix（参数：右指针, 字符）
Matrix <- function(r, c) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$row <- r  # 把 右指针 存入 e$row
    e$col <- c  # 把 字符 存入 e$col
    e$buf <- matrix(0L, nrow = r, ncol = c)  # 把 矩阵(0L, nrow 赋值为 右指针, ncol 赋值为 字符) 存入 e$buf
    class(e) <- "Matrix"  # 把 「Matrix」 存入 class(e)
    e
}
matrix_call <- function(m, r, c) m$buf[r + 1L, c + 1L]  # 定义函数 matrix_call（参数：映射表, 右指针, 字符）
m <- Matrix(4L, 5L)  # 把 Matrix(4L, 5L) 存入 映射表
for (i in 0:3) {
    # for (下标 i in 0:3) {
    for (j in 0:4) m$buf[i + 1L, j + 1L] <- i * j  # 直接访问 buf
}
stopifnot(matrix_call(m, 2L, 3L) == 6L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
