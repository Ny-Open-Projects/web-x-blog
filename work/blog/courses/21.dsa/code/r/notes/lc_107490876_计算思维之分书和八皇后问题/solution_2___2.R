# 来源：https://blog.csdn.net/tyro_java/article/details/107490876 LeetCode 107490876. 分书和八皇后问题 — R
# 版（方案2：分书，函数式不可变副本）
LIKE <- matrix(c(0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1  # 0, 1, 0, 0, 1
),
    nrow = 5, byrow = TRUE)  # 把 5, byrow 赋值为 TRUE) 写入 ), nrow
allocate_books_func <- function() {
    # 定义函数 allocate_books_func（参数：无）
    results <- list()  # 把 列表() 存入 results
    try_assign <- function(reader, assigned) {
        # 定义函数 try_assign（参数：reader, assigned） 若 reader 等于 5L
        if (reader == 5L) {
            results <<- c(results, list(assigned))  # results 小于 小于 减 字符(results, 列表(assigned))
            return(invisible(NULL))  # 返回 invisible(NULL
        }
        for (book in 0:4) {
            # for (book in 0:4) {
            if (LIKE[reader + 1L, book + 1L] == 1 && assigned[book + 1L] == -1L) {
                nxt <- assigned  # 把 assigned 存入 nxt
                nxt[book + 1L] <- reader  # nxt[book 加 1L] 小于 减 reader
                try_assign(reader + 1L, nxt)  # try_assign(reader 加 1L, nxt)
            }
        }
    }
    try_assign(0L, rep(-1L, 5))  # try_assign(0L, rep( 减 1L, 5))
    results  # results
}
want <- list(c(1L, 2L, 0L, 3L, 4L), c(1L, 4L, 0L, 3L, 2L))  # 把 列表(字符(1L, 2L, 0L, 3L, 4L), 字符(1L, 4L, 0L, 3L, 2L)) 存入 want
res <- allocate_books_func()  # 把 allocate_books_func() 存入 结果
stopifnot(length(res) == 2L)  # 断言校验
for (i in 1:2) {
    # for (下标 i in 1:2) {
    stopifnot(identical(as.integer(res[[i]]), as.integer(want[[i]])))  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
