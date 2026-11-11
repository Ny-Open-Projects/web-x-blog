# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134055742 LeetCode 283. 移动零 — R
# 版（方案1） 定义函数 move_zeroes（参数：数组）
move_zeroes <- function(nums) {
    nz <- nums[nums != 0]  # 把 数组[数组 不等于 0] 存入 nz
    c(nz, rep(0, length(nums) - length(nz)))  # 字符(nz, rep(0, 长度(数组) 减 长度(nz)))
}
stopifnot(identical(move_zeroes(c(0, 1, 0, 3, 12)), c(1, 3, 12, 0, 0)))  # 断言校验
stopifnot(identical(move_zeroes(c(0)), c(0)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
