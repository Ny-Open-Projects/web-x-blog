# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135917076 LeetCode 567. 字符串的排列 — R
# 版（方案2） 定义函数 check_inclusion（参数：s1, s2）
check_inclusion <- function(s1, s2) {
    a <- strsplit(s1, "")[[1]]  # 把 strsplit(s1, 「」)[[1]] 存入 数组
    b <- strsplit(s2, "")[[1]]  # 把 strsplit(s2, 「」)[[1]] 存入 b
    m <- length(a)
    n <- length(b)  # 把 长度(数组); 元素个数 小于 减 长度(b) 存入 映射表
    if (m > n)
        return(FALSE)  # 若 映射表 超过 元素个数) return(FALSE
    ci <- function(str, from, to) {
        # 定义函数 ci（参数：str, from, to）
        cnt <- rep(0L, 26)  # 把 rep(0L, 26) 存入 计数
        for (ch in str[from:to]) cnt[utf8ToInt(ch) - 96] <- cnt[utf8ToInt(ch) - 96] + 1L
        cnt  # 计数
    }
    s1c <- ci(a, 1, m)  # 把 ci(数组, 1, 映射表) 存入 s1c
    s2c <- ci(b, 1, m)  # 把 ci(b, 1, 映射表) 存入 s2c
    if (identical(s1c, s2c))
        return(TRUE)  # 若 identical(s1c, s2c)) return(TRUE
    for (i in (m + 1):n) {
        # for (下标 i in (映射表 加 1):元素个数) {
        s2c <- ci(b, i - m + 1, i)  # 简化重算窗口（正确性优先）
        if (identical(s1c, s2c))
            return(TRUE)  # 若 identical(s1c, s2c)) return(TRUE
    }
    FALSE  # FALSE
}
stopifnot(check_inclusion("ab", "eidbaooo"))  # 断言校验
stopifnot(!check_inclusion("ab", "eidboaoo"))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
