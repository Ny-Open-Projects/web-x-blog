# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135256754 LeetCode 76. 最小覆盖子串 — R
# 版（方案2） 定义函数 min_window（参数：字符串, 另一字符串）
min_window <- function(s, t) {
    if (nchar(s) == 0L || nchar(t) == 0L)
        return("")  # 若 nchar(字符串) 等于 0L 或 nchar(另一字符串) 等于 0L) return(「」
    sc <- strsplit(s, "")[[1]]  # 把 strsplit(字符串, 「」)[[1]] 存入 sc
    tc <- strsplit(t, "")[[1]]  # 把 strsplit(另一字符串, 「」)[[1]] 存入 tc
    target <- table(tc)  # 把 table(tc) 存入 目标值
    required <- length(target)  # 引入依赖
    left <- 1L
    formed <- 0L  # 把 1L; formed 小于 减 0L 存入 左边界
    window <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 window
    min_len <- .Machine$integer.max
    min_left <- 1L  # 把 Machine$integer.max; min_left 小于 减 1L 存入 min_len
    for (right in seq_along(sc)) {
        # for (右边界 in seq_along(sc)) {
        c <- sc[right]  # 把 sc[右边界] 存入 字符
        key <- as.character(c)  # 把 as.character(字符) 存入 key
        if (is.null(window[[key]]))
            window[[key]] <- 0L  # 若 is.null(window[[key]])) window[[key]] 小于 减 0L
        window[[key]] <- window[[key]] + 1L  # 把 window[[key]] 加 1L 存入 window[[key]]
        if (!is.na(target[key]) && window[[key]] == target[[key]])
            formed <- formed + 1L
        while (formed == required) {
            # 循环，直到不满足「formed 等于 required」
            if (right - left + 1L < min_len) {
                min_len <- right - left + 1L
                min_left <- left
            }
            lk <- as.character(sc[left])  # 把 as.character(sc[左边界]) 存入 lk
            window[[lk]] <- window[[lk]] - 1L  # 把 window[[lk]] 减 1L 存入 window[[lk]]
            if (!is.na(target[lk]) && window[[lk]] < target[[lk]])
                formed <- formed - 1L
            left <- left + 1L  # 把 左边界 加 1L 存入 左边界
        }
    }
    if (min_len == .Machine$integer.max)
        return("")  # 若 min_len 等于 .Machine$integer.max) return(「」
    paste(sc[min_left:(min_left + min_len - 1L)], collapse = "")
}
stopifnot(min_window("ADOBECODEBANC", "ABC") == "BANC")  # 断言校验
stopifnot(min_window("a", "a") == "a")  # 断言校验
stopifnot(min_window("a", "aa") == "")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
