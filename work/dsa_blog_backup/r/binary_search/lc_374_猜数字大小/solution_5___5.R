# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145238093 LeetCode 374. 猜数字大小 — R
# 版（方案5：迭代二分）
pick_v <- 6L  # 把 6L 存入 pick_v
guess <- function(num) if (num == pick_v) 0L else if (num < pick_v) 1L else -1L  # 定义函数 guess（参数：num）
guess_number <- function(n) {
    # 定义函数 guess_number（参数：元素个数）
    low <- 1L
    high <- n  # 把 1L; high 小于 减 元素个数 存入 low
    while (low <= high) {
        # 循环，直到不满足「low 不超过 high」
        mid <- low + (high - low)%/%2L  # 把 low 加 (high 减 low) 对…取模 除以 对…取模 2L 存入 中点
        res <- guess(mid)  # 把 guess(中点) 存入 结果
        if (res == 0L)
            return(mid)  # 若 结果 等于 0L) return(中点
        if (res == 1L)
            low <- mid + 1L else high <- mid - 1L  # 若 结果 等于 1L) low 小于 减 中点 加 1L else high 小于 减 中点 减 1L
    }
    -1L  # 减 1L
}
cs <- matrix(c(10L, 6L, 1L, 1L, 5L, 3L, 2L, 2L), ncol = 2L, byrow = TRUE)
for (i in seq_len(nrow(cs))) {
    # for (下标 i in seq_len(nrow(cs))) {
    pick_v <<- cs[i, 2L]  # pick_v 小于 小于 减 cs[下标 i, 2L]
    stopifnot(guess_number(cs[i, 1L]) == cs[i, 2L])  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
