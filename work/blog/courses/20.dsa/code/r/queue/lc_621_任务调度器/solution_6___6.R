# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987 LeetCode 621. 任务调度器 — R 版
# 方案6（公式法另一写法：Counter 值列表 + count(freq)） 定义函数 least_interval（参数：tasks, 元素个数）
least_interval <- function(tasks, n) {
    cnt <- table(tasks)  # 把 table(tasks) 存入 计数
    lst <- as.integer(cnt)  # 把 as.integer(计数) 存入 lst
    freq <- if (length(lst) > 0L)
        max(lst) else 0L  # 把 if (长度(lst) 超过 0L) 取较大值 lst) else 0L 存入 频次表
    same <- sum(lst == freq)  # 把 累计和(lst 等于 频次表) 存入 same
    max((freq - 1L) * (n + 1L) + same, length(tasks))  # 取较大值 (频次表 减 1L) 乘 (元素个数 加 1L) 加 same, 长度(tasks))
}
# 自测：与 TS 事实源内嵌用例一致
cases <- list(list(tasks = c("A", "A", "A", "B", "B", "B"), n = 2L, want = 8L), list(tasks = c("A", "A", "A", "A"),
    n = 2L, want = 10L), list(tasks = c("A", "B", "C", "D"), n = 0L, want = 4L))
for (i in seq_along(cases)) {
    # for (下标 i in seq_along(cases)) {
    got <- least_interval(cases[[i]]$tasks, cases[[i]]$n)
    stopifnot(got == cases[[i]]$want)  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
