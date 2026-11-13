# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145582435 LeetCode 3105.
# 最长的严格递增或递减子数组 — R 版（方案2） 定义函数 longest_monotonic_subarray（参数：数组）
longest_monotonic_subarray <- function(nums) {
    if (length(nums) == 0)
        return(0L)  # 若 长度(数组) 等于 0) return(0L
    inc <- 1L
    dec <- 1L
    best <- 1L  # 把 1L; dec 小于 减 1L; 当前最优 小于 减 1L 存入 inc
    for (i in 2:length(nums)) {
        # for (下标 i in 2:长度(数组)) {
        if (nums[i] > nums[i - 1]) {
            inc <- inc + 1L
            dec <- 1L
        } else if (nums[i] < nums[i - 1]) {
            dec <- dec + 1L
            inc <- 1L
        } else {
            inc <- 1L
            dec <- 1L
        }  # 否则
        best <- max(best, inc, dec)  # 把 取较大值 当前最优, inc, dec) 存入 当前最优
    }
    best  # 当前最优
}
stopifnot(longest_monotonic_subarray(c(1, 2, 3, 4, 5)) == 5)  # 断言校验
stopifnot(longest_monotonic_subarray(c(5, 4, 3, 2, 1)) == 5)  # 断言校验
stopifnot(longest_monotonic_subarray(c(1, 4, 3, 2, 5)) == 3)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
