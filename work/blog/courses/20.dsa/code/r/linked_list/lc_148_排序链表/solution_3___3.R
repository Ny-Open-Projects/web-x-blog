# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133904873 LeetCode 148. 排序链表 — R
# 版（方案3）
sort_list <- function(vals) as.integer(sort(vals))  # 定义函数 sort_list（参数：vals）
stopifnot(identical(sort_list(c(4, 2, 1, 3)), 1:4))  # 断言校验
stopifnot(identical(sort_list(c(-1, 5, 3, 4, 0)), c(-1L, 0L, 3L, 4L, 5L)))  # 断言校验
stopifnot(length(sort_list(integer(0))) == 0)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
