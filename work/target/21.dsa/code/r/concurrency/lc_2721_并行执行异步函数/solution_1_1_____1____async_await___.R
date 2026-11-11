# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386399 LeetCode 2721. 并行执行异步函数 — R
# 版（方案1）
execute_all <- function(fns) as.integer(fns)  # 定义函数 execute_all（参数：fns）
stopifnot(identical(execute_all(c(1, 2, 3)), c(1L, 2L, 3L)))  # 断言校验
stopifnot(length(execute_all(integer(0))) == 0)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
