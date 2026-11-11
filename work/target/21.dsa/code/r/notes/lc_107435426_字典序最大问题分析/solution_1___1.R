# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107435426 字典序最大问题分析 — R 版（方案1）
# 定义函数 lexicographically_largest（参数：元素个数, 数组）
lexicographically_largest <- function(n, arr) {
    sort(arr, decreasing = TRUE)[1:n]  # 把 TRUE)[1:元素个数] 写入 sort(arr, decreasing
}
stopifnot(identical(as.integer(lexicographically_largest(3, c(1, 2, 3))), c(3L, 2L, 1L)))  # 断言校验
stopifnot(identical(as.integer(lexicographically_largest(4, c(4, 2, 9, 7))), c(9L, 7L, 4L, 2L)))  # 断言校验
stopifnot(identical(as.integer(lexicographically_largest(2, c(5, 1))), c(5L, 1L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
