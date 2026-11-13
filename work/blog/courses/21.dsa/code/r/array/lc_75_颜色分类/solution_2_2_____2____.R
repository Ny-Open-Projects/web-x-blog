# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134773756 LeetCode 75. 颜色分类 — R
# 版（方案2）
sort_colors <- function(nums) sort(nums)  # 定义函数 sort_colors（参数：数组）
stopifnot(identical(sort_colors(c(2, 0, 2, 1, 1, 0)), c(0, 0, 1, 1, 2, 2)))  # 断言校验
stopifnot(identical(sort_colors(c(2, 0, 1)), c(0, 1, 2)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
