# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133468244 数据结构与算法之堆:
# 堆和实现最小堆类 — R 版（方案1）
min_heap_pop_all <- function(input) sort(as.integer(input))  # 定义函数 min_heap_pop_all（参数：input）
stopifnot(identical(min_heap_pop_all(c(3, 1, 6, 5, 2, 4)), 1:6))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
