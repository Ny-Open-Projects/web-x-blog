# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134032039 LeetCode 48. 旋转矩阵 — R 版
# 方案1：先沿主对角线转置，再逐行左右翻转 R 为传值拷贝语义，函数内原地修改不影响调用方（等价于 TS
# 的引用原地修改） 定义函数 rotate（参数：matrix_）
rotate <- function(matrix_) {
    n <- length(matrix_)  # 把 长度(matrix_) 存入 元素个数
    for (i in seq_len(n)) {
        # for (下标 i in seq_len(元素个数)) { 若 下标 i 加 1L 不超过 元素个数 for (下标 j in (下标 i 加
        # 1L):元素个数) {
        if (i + 1L <= n) {
            for (j in (i + 1L):n) {
                tmp <- matrix_[[i]][j]  # 把 matrix_[[下标 i]][下标 j] 存入 临时变量
                matrix_[[i]][j] <- matrix_[[j]][i]  # 把 matrix_[[下标 j]][下标 i] 存入 matrix_[[i]][j]
                matrix_[[j]][i] <- tmp  # 把 临时变量 存入 matrix_[[j]][i]
            }
        }
    }
    for (i in seq_len(n)) {
        # for (下标 i in seq_len(元素个数)) {
        matrix_[[i]] <- rev(matrix_[[i]])  # 等价于双指针左右翻转
    }
    matrix_  # matrix_
}
eq_matrix <- function(a, b) {
    # 定义函数 eq_matrix（参数：数组, b）
    if (length(a) != length(b))
        return(FALSE)  # 若 长度(数组) 不等于 长度(b)) return(FALSE
    for (i in seq_along(a)) {
        # for (下标 i in seq_along(数组)) {
        if (length(a[[i]]) != length(b[[i]]))
            return(FALSE)  # 若 长度(数组[[下标 i]]) 不等于 长度(b[[下标 i]])) return(FALSE
        if (!all(a[[i]] == b[[i]]))
            return(FALSE)  # 若 取反 all(数组[[下标 i]] 等于 b[[下标 i]])) return(FALSE
    }
    TRUE  # TRUE
}
# 自测：与 TS 事实源内嵌用例一致（LeetCode 官方示例）
cases <- list(list(list(c(1L, 2L, 3L), c(4L, 5L, 6L), c(7L, 8L, 9L)), list(c(7L, 4L, 1L), c(8L, 5L, 2L), c(9L,
    6L, 3L))  # 列表(字符(7L, 4L, 1L), 字符(8L, 5L, 2L), 字符(9L, 6L, 3L))
), list(list(c(5L, 1L, 9L,
    11L), c(2L, 4L, 8L, 10L), c(13L, 3L, 6L, 7L), c(15L, 14L, 12L, 16L)), list(c(15L, 13L, 2L, 5L), c(14L, 3L,
    4L, 1L), c(12L, 6L, 8L, 9L), c(16L, 7L, 10L, 11L))))
for (idx in seq_along(cases)) {
    # for (idx in seq_along(cases)) {
    got <- rotate(cases[[idx]][[1]])  # 把 rotate(cases[[idx]][[1]]) 存入 got
    stopifnot(eq_matrix(got, cases[[idx]][[2]]))  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
