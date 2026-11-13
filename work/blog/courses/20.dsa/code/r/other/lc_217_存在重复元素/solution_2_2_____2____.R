# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135038527 LeetCode 217. 存在重复元素 — R
# 版（方案2）
contains_duplicate <- function(nums) length(unique(nums)) != length(nums)  # 定义函数 contains_duplicate（参数：数组）
stopifnot(contains_duplicate(c(1, 2, 3, 1)))  # 断言校验
stopifnot(!contains_duplicate(c(1, 2, 3, 4)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
