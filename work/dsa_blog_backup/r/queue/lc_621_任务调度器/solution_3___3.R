# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987 LeetCode 621. 任务调度器 — R 版
# 方案3（贪心模拟，每轮取剩余次数最多的 n+1 个，最后一轮只计实际执行数） 定义函数
# least_interval（参数：tasks, 元素个数）
least_interval <- function(tasks, n) {
    freq <- integer(26L)  # 把 integer(26L) 存入 频次表
    base <- utf8ToInt("A")  # 把 utf8ToInt(「A」) 存入 base
    for (t in tasks) {
        # for (另一字符串 in tasks) {
        idx <- utf8ToInt(t) - base + 1L  # 把 utf8ToInt(另一字符串) 减 base 加 1L 存入 idx
        freq[idx] <- freq[idx] + 1L  # 把 频次表[idx] 加 1L 存入 freq[idx]
    }
    cnt <- as.integer(freq[freq > 0L])  # 把 as.integer(频次表[频次表 超过 0L]) 存入 计数
    time <- 0L  # 把 0L 存入 time
    while (length(cnt) > 0L) {
        # 循环，直到不满足「长度(计数) 超过 0L」
        cnt <- sort(cnt, decreasing = TRUE)  # 把 sort(计数, decreasing 赋值为 TRUE) 存入 计数
        used <- 0L  # 把 0L 存入 已用标记
        take <- min(n + 1L, length(cnt))  # 把 取较小值 元素个数 加 1L, 长度(计数)) 存入 take
        for (i in seq_len(take)) {
            # for (下标 i in seq_len(take)) { 若 计数[下标 i] 超过 0L
            if (cnt[i] > 0L) {
                cnt[i] <- cnt[i] - 1L  # 把 计数[下标 i] 减 1L 存入 cnt[i]
                used <- used + 1L  # 把 已用标记 加 1L 存入 已用标记
            }
        }
        cnt <- cnt[cnt > 0L]  # 把 计数[计数 超过 0L] 存入 计数
        time <- time + if (length(cnt) > 0L)
            n + 1L else used  # 把 time 加 if (长度(计数) 超过 0L) 元素个数 加 1L else 已用标记 存入 time
    }
    time  # time
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
