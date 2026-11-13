# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133844403 LeetCode 55. 跳跃游戏 — R
# 版（方案1） 定义函数 can_jump（参数：数组）
can_jump <- function(nums) {
    max_reach <- 0L  # 把 0L 存入 max_reach
    for (i in seq_along(nums)) {
        # for (下标 i in seq_along(数组)) {
        if ((i - 1L) > max_reach)
            return(FALSE)  # 若 (下标 i 减 1L) 超过 max_reach) return(FALSE
        r <- (i - 1L) + nums[i]  # 把 (下标 i 减 1L) 加 数组[下标 i] 存入 右指针
        if (r > max_reach)
            max_reach <- r  # 若 右指针 超过 max_reach) max_reach 小于 减 右指针
    }
    TRUE  # TRUE
}
stopifnot(can_jump(c(2, 3, 1, 1, 4)))  # 断言校验
stopifnot(!can_jump(c(3, 2, 1, 0, 4)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
