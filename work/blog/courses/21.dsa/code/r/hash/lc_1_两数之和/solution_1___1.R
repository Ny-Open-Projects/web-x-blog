# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130663853 LeetCode 1. 两数之和 — R
# 版（方案1：暴力双循环） 定义函数 two_sum（参数：数组, 目标值）
two_sum <- function(nums, target) {
    n <- length(nums)  # 把 长度(数组) 存入 元素个数
    for (i in seq_len(n)) {
        # for (下标 i in seq_len(元素个数)) { for (下标 j in (下标 i 加 1L):元素个数) {
        for (j in (i + 1L):n) {
            if (nums[i] + nums[j] == target)
                return(c(i - 1L, j - 1L))  # 若 数组[下标 i] 加 数组[下标 j] 等于 目标值) return(字符(下标 i 减 1L, 下标 j 减 1L
        }
    }
    integer(0)  # integer(0)
}
stopifnot(identical(two_sum(c(2, 7, 11, 15), 9), c(0L, 1L)))  # 断言校验
stopifnot(identical(two_sum(c(3, 2, 4), 6), c(1L, 2L)))  # 断言校验
stopifnot(identical(two_sum(c(3, 3), 6), c(0L, 1L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
