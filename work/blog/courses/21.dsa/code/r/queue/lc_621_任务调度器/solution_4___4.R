# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987 LeetCode 621. 任务调度器 — R 版
# 方案4（26 位频率桶公式法） 定义函数 least_interval（参数：tasks, 元素个数）
least_interval <- function(tasks, n) {
    freq <- integer(26L)  # 把 integer(26L) 存入 频次表
    base <- utf8ToInt("A")  # 把 utf8ToInt(「A」) 存入 base
    for (t in tasks) {
        # for (另一字符串 in tasks) {
        idx <- utf8ToInt(t) - base + 1L  # 把 utf8ToInt(另一字符串) 减 base 加 1L 存入 idx
        freq[idx] <- freq[idx] + 1L  # 把 频次表[idx] 加 1L 存入 freq[idx]
    }
    max_freq <- max(freq)  # 把 取较大值 频次表) 存入 max_freq
    same <- sum(freq == max_freq)  # 把 累计和(频次表 等于 max_freq) 存入 same
    max((max_freq - 1L) * (n + 1L) + same, length(tasks))  # 取较大值 (max_freq 减 1L) 乘 (元素个数 加 1L) 加 same, 长度(tasks))
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
