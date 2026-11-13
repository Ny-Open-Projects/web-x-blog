# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134982348 LeetCode 977. 有序数组的平方 — R
# 版（方案2）
sorted_squares <- function(nums) sort(nums^2)  # 定义函数 sorted_squares（参数：数组）
stopifnot(identical(sorted_squares(c(-4, -1, 0, 3, 10)), c(0, 1, 9, 16, 100)))  # 断言校验
stopifnot(identical(sorted_squares(c(-7, -3, 2, 3, 11)), c(4, 9, 9, 49, 121)))  # 断言校验
stopifnot(identical(sorted_squares(c(1, 2, 3)), c(1, 4, 9)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
