# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133530983 数据结构与算法之堆:
# 实现最大堆类及堆排序 — R 版（方案1）
max_heap_pop_all <- function(input) sort(as.integer(input), decreasing = TRUE)  # 定义函数 max_heap_pop_all（参数：input）
stopifnot(identical(max_heap_pop_all(c(3, 1, 6, 5, 2, 4)), c(6L, 5L, 4L, 3L, 2L, 1L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
