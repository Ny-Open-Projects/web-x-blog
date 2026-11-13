# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135129920 LeetCode 8. 字符串转换整数 (atoi) —
# R 版（方案2） 定义函数 my_atoi（参数：字符串）
my_atoi <- function(s) {
    i <- 1
    n <- nchar(s)  # 把 1; 元素个数 小于 减 nchar(字符串) 存入 下标 i
    chars <- strsplit(s, "")[[1]]  # 把 strsplit(字符串, 「」)[[1]] 存入 chars
    while (i <= n && chars[i] == " ") i <- i + 1L
    sign <- 1  # 把 1 存入 sign
    if (i <= n && (chars[i] == "+" || chars[i] == "-")) {
        if (chars[i] == "-")
            sign <- -1  # 若 chars[下标 i] 等于 「 减 」) sign 小于 减 减 1
        i <- i + 1L  # 把 下标 i 加 1L 存入 下标 i
    }
    ans <- 0  # 把 0 存入 答案
    while (i <= n && grepl("[0-9]", chars[i])) {
        # 循环，直到不满足「下标 i 不超过 元素个数 且 grepl(「[0 减 9]」, chars[下标 i]」
        ans <- ans * 10 + as.integer(chars[i])  # 把 答案 乘 10 加 as.integer(chars[下标 i]) 存入 答案
        if (ans > 2147483648)
            ans <- 2147483648  # 若 答案 超过 2147483648) 答案 小于 减 2147483648
        i <- i + 1L  # 把 下标 i 加 1L 存入 下标 i
    }
    ans <- ans * sign  # 把 答案 乘 sign 存入 答案
    if (ans >= 2147483648)
        return(2147483647L)  # 若 答案 不低于 2147483648) return(2147483647L
    if (ans <= -2147483648)
        return(-2147483648)  # 若 答案 不超过 减 2147483648) return( 减 2147483648L
    as.integer(ans)  # as.integer(答案)
}
stopifnot(my_atoi("42") == 42)  # 断言校验
stopifnot(my_atoi(" -42") == -42)  # 断言校验
stopifnot(my_atoi("4193 with words") == 4193)  # 断言校验
stopifnot(my_atoi("-91283472332") == -2147483648)  # 断言校验
stopifnot(my_atoi("words and 987") == 0)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
