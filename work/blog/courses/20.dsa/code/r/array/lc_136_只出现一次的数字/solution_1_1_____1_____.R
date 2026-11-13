# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133468105 LeetCode 136. 只出现一次的数字 — R
# 版（方案1）
single_number <- function(nums) Reduce(bitwXor, nums, 0L)  # 定义函数 single_number（参数：数组）
stopifnot(single_number(c(2L, 2L, 1L)) == 1L)  # 断言校验
stopifnot(single_number(c(4L, 1L, 2L, 1L, 2L)) == 4L)  # 断言校验
stopifnot(single_number(c(1L)) == 1L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
