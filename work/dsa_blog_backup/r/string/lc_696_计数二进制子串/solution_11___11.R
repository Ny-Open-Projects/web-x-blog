# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135756434 LeetCode 696. 计数二进制子串 — R
# 版（方案11） 定义函数 count_binary_substrings（参数：字符串）
count_binary_substrings <- function(s) {
    chars <- strsplit(s, "")[[1]]  # 把 strsplit(字符串, 「」)[[1]] 存入 chars
    groups <- integer(0)  # 把 integer(0) 存入 groups
    i <- 1
    n <- length(chars)  # 把 1; 元素个数 小于 减 长度(chars) 存入 下标 i
    while (i <= n) {
        # 循环，直到不满足「下标 i 不超过 元素个数」
        ch <- chars[i]  # 把 chars[下标 i] 存入 字符
        cnt <- 0  # 把 0 存入 计数
        while (i <= n && chars[i] == ch) {
            cnt <- cnt + 1
            i <- i + 1
        }
        groups <- c(groups, cnt)  # 把 字符(groups, 计数) 存入 groups
    }
    ans <- 0  # 把 0 存入 答案
    for (k in 2:length(groups)) {
        # for (下标 k in 2:长度(groups)) {
        ans <- ans + min(groups[k - 1], groups[k])  # 把 答案 加 取较小值 groups[下标 k 减 1], groups[下标 k]) 存入 答案
    }
    ans  # 答案
}
stopifnot(count_binary_substrings("00110011") == 6)  # 断言校验
stopifnot(count_binary_substrings("10101") == 4)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
