# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136236962 LeetCode 1685.
# 有序数组中差绝对值之和 — R 版（方案3） 定义函数 get_sum_absolute_differences（参数：数组）
get_sum_absolute_differences <- function(nums) {
    n <- length(nums)  # 把 长度(数组) 存入 元素个数
    total <- sum(nums)  # 把 累计和(数组) 存入 总和
    prefix <- 0  # 把 0 存入 prefix
    out <- integer(n)  # 把 integer(元素个数) 存入 out
    for (i in seq_len(n)) {
        # for (下标 i in seq_len(元素个数)) {
        v <- nums[i]  # 把 数组[下标 i] 存入 值
        left <- v * (i - 1) - prefix  # 把 值 乘 (下标 i 减 1) 减 prefix 存入 左边界
        right <- (total - prefix - v) - v * (n - i)  # 把 (总和 减 prefix 减 值) 减 值 乘 (元素个数 减 下标 i) 存入 右边界
        out[i] <- left + right  # 把 左边界 加 右边界 存入 out[i]
        prefix <- prefix + v  # 把 prefix 加 值 存入 prefix
    }
    out  # out
}
stopifnot(identical(as.integer(get_sum_absolute_differences(c(2, 3, 5))), c(4L, 3L, 5L)))  # 断言校验
stopifnot(identical(as.integer(get_sum_absolute_differences(c(1, 4, 6, 8, 10))), c(24L, 15L, 13L, 15L, 21L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
