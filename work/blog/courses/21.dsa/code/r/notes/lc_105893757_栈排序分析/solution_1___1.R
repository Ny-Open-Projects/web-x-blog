# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757 栈排序分析 — R 版（方案1）
stack_sort <- function(input) as.integer(rev(input))  # 定义函数 stack_sort（参数：input）
stopifnot(identical(stack_sort(c(3, 1, 5, 2, 4)), c(4L, 2L, 5L, 1L, 3L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
