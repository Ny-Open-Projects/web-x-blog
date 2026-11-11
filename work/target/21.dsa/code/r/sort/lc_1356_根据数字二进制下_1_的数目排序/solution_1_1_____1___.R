# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138671078 LeetCode 1356.
# 根据数字二进制下1的数目排序 — R 版（方案1） 定义函数 count_bits（参数：元素个数）
count_bits <- function(n) {
    c <- 0L  # 把 0L 存入 字符
    while (n > 0) {
        c <- c + bitwAnd(n, 1)
        n <- bitwShiftR(n, 1)
    }
    c  # 字符
}
sort_by_bits <- function(nums) {
    # 定义函数 sort_by_bits（参数：数组）
    b <- vapply(nums, count_bits, 0L)  # 把 vapply(数组, count_bits, 0L) 存入 b
    nums[order(b, nums)]  # 数组[order(b, 数组)]
}
stopifnot(identical(sort_by_bits(0:8), c(0L, 1L, 2L, 4L, 8L, 3L, 5L, 6L, 7L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
