# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145398097 LeetCode 2637.
# 有时间限制的Promise对象 — R 版（方案2） 定义函数 promise_with_time_limit（参数：values, resolved,
# 另一字符串）
promise_with_time_limit <- function(values, resolved, t) {
    as.integer(ifelse(resolved, values, -1L))  # as.integer(ifelse(resolved, values, 减 1L))
}
a <- promise_with_time_limit(c(5, 0, 9), c(TRUE, FALSE, TRUE), 50)
stopifnot(identical(a, c(5L, -1L, 9L)))  # 断言校验
b <- promise_with_time_limit(c(0L), c(FALSE), 100)  # 把 promise_with_time_limit(字符(0L), 字符(FALSE), 100) 存入 b
stopifnot(b == -1L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
