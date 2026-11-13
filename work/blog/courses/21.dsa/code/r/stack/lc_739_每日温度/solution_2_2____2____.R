# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233913 LeetCode 739. 每日温度 — R
# 版（方案2） 定义函数 daily_temperatures（参数：temps）
daily_temperatures <- function(temps) {
    n <- length(temps)  # 把 长度(temps) 存入 元素个数
    res <- rep(0L, n)  # 把 rep(0L, 元素个数) 存入 结果
    st <- integer(0)  # 把 integer(0) 存入 st
    for (i in seq_len(n)) {
        # for (下标 i in seq_len(元素个数)) { 循环，直到不满足「长度(st) 超过 0 且 temps[st[长度(st)]] 小于
        # temps[下标 i]」
        while (length(st) > 0 && temps[st[length(st)]] < temps[i]) {
            res[st[length(st)]] <- i - st[length(st)]  # 把 下标 i 减 st[长度(st)] 存入 res[st[length(st)]]
            st <- st[-length(st)]  # 把 st[ 减 长度(st)] 存入 st
        }
        st <- c(st, i)  # 把 字符(st, 下标 i) 存入 st
    }
    res  # 结果
}
stopifnot(identical(daily_temperatures(c(73, 74, 75, 71, 69, 72, 76, 73)), c(1L, 1L, 4L, 2L, 1L, 1L, 0L, 0L)))  # 断言校验
stopifnot(identical(daily_temperatures(c(30, 40, 50, 60)), c(1L, 1L, 1L, 0L)))  # 断言校验
stopifnot(identical(daily_temperatures(c(30, 60, 90)), c(1L, 1L, 0L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
