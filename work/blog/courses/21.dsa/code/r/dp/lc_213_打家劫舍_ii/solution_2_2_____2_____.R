# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130716392 LeetCode 213. 打家劫舍II — R
# 版（方案2）
rob_line <- function(nums) {
    a <- 0L
    b <- 0L
    for (v in nums) {
        t <- max(b, a + v)
        a <- b
        b <- t
    }
    b
}  # 定义函数 rob_line（参数：数组）
rob_ii <- function(nums) {
    # 定义函数 rob_ii（参数：数组）
    if (length(nums) == 1)
        return(nums)  # 若 长度(数组) 等于 1) return(数组
    max(rob_line(nums[-1]), rob_line(nums[-length(nums)]))  # 取较大值 rob_line(数组[ 减 1]), rob_line(数组[ 减 长度(数组)]))
}
stopifnot(rob_ii(c(2, 3, 2)) == 3)  # 断言校验
stopifnot(rob_ii(c(1, 2, 3, 1)) == 4)  # 断言校验
stopifnot(rob_ii(c(1)) == 1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
