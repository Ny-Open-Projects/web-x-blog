# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987 LeetCode 621. 任务调度器 — R 版
# 方案5（公式法：出现最多的任务 freq 个，有 same 个并列最多， 最少时间 = (freq-1)*(n+1) +
# same，且不能少于任务总数） 定义函数 least_interval（参数：tasks, 元素个数）
least_interval <- function(tasks, n) {
    cnt <- table(tasks)  # 把 table(tasks) 存入 计数
    freq <- if (length(cnt) > 0L)
        max(cnt) else 0L  # 把 if (长度(计数) 超过 0L) 取较大值 计数) else 0L 存入 频次表
    same <- sum(cnt == freq)  # 把 累计和(计数 等于 频次表) 存入 same
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
