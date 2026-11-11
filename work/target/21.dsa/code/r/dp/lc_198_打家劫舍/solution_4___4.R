# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130644389 LeetCode 198. 打家劫舍 — R
# 版（方案4）
rob_houses <- function(nums) {
    a <- 0L
    b <- 0L
    for (v in nums) {
        t <- max(b, a + v)
        a <- b
        b <- t
    }
    b
}  # 定义函数 rob_houses（参数：数组）
stopifnot(rob_houses(c(1, 2, 3, 1)) == 4)  # 断言校验
stopifnot(rob_houses(c(2, 7, 9, 3, 1)) == 12)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
