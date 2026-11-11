# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133807379 LeetCode 209. 长度最小的子数组 — R
# 版（方案3） 定义函数 min_sub_array_len（参数：目标值, 数组）
min_sub_array_len <- function(target, nums) {
    l <- 1L
    sum_ <- 0
    best <- .Machine$integer.max  # 把 1L; sum_ 小于 减 0; 当前最优 小于 减 .Machine$integer.max 存入 左指针
    for (r in seq_along(nums)) {
        # for (右指针 in seq_along(数组)) {
        sum_ <- sum_ + nums[r]  # 把 sum_ 加 数组[右指针] 存入 sum_
        while (sum_ >= target) {
            # 循环，直到不满足「sum_ 不低于 目标值」
            if (r - l + 1L < best)
                best <- r - l + 1L  # 若 右指针 减 左指针 加 1L 小于 当前最优) 当前最优 小于 减 右指针 减 左指针 加 1L
            sum_ <- sum_ - nums[l]  # 把 sum_ 减 数组[左指针] 存入 sum_
            l <- l + 1L  # 把 左指针 加 1L 存入 左指针
        }
    }
    if (best == .Machine$integer.max)
        0L else best  # 若 当前最优 等于 .Machine$integer.max) 0L else 当前最优
}
stopifnot(min_sub_array_len(7, c(2, 3, 1, 2, 4, 3)) == 2)  # 断言校验
stopifnot(min_sub_array_len(4, c(1, 4, 4)) == 1)  # 断言校验
stopifnot(min_sub_array_len(11, c(1, 1, 1, 1, 1, 1, 1, 1)) == 0)  # 断言校验
stopifnot(min_sub_array_len(1, c(1, 2, 3)) == 1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
