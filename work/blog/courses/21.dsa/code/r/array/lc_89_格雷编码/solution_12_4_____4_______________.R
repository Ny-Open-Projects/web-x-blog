# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134866839 LeetCode 89. 格雷编码 — R
# 版（方案12） 定义函数 gray_code（参数：元素个数）
gray_code <- function(n) {
    m <- 2^n  # 把 2 按位异或 元素个数 存入 映射表
    sapply(0:(m - 1), function(i) bitwXor(i, bitwShiftR(i, 1)))
}
stopifnot(identical(as.integer(gray_code(2)), c(0L, 1L, 3L, 2L)))  # 断言校验
stopifnot(identical(as.integer(gray_code(1)), c(0L, 1L)))  # 断言校验
stopifnot(length(gray_code(3)) == 8)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
