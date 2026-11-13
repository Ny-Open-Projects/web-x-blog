# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135424151 LeetCode 292. Nim游戏 — R
# 版（方案1）
can_win_nim <- function(n) n%%4 != 0  # 定义函数 can_win_nim（参数：元素个数）
stopifnot(!can_win_nim(4), can_win_nim(1), can_win_nim(2), !can_win_nim(8))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
