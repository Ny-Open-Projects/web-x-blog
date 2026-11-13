# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987 LeetCode 621. 任务调度器 — R 版
# 方案1（Counter 公式法）；table() 即 Counter 等价物 定义函数 least_interval（参数：tasks, 元素个数）
least_interval <- function(tasks, n) {
    count <- table(tasks)  # 把 table(tasks) 存入 计数
    max_count <- if (length(count) > 0L)
        max(count) else 0L  # 把 if (长度(计数) 超过 0L) 取较大值 计数) else 0L 存入 max_count
    max_count_tasks <- sum(count == max_count)  # 把 累计和(计数 等于 max_count) 存入 max_count_tasks
    max(length(tasks), (max_count - 1L) * (n + 1L) + max_count_tasks)
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
