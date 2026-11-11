# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138771574 LeetCode 93. 复原IP地址 — R
# 版（方案1） 定义函数 valid_seg（参数：字符串）
valid_seg <- function(s) {
    if (nchar(s) == 0 || nchar(s) > 3)
        return(FALSE)  # 若 nchar(字符串) 等于 0 或 nchar(字符串) 超过 3) return(FALSE
    if (nchar(s) > 1 && substr(s, 1, 1) == "0")
        return(FALSE)  # 若 nchar(字符串) 超过 1 且 substr(字符串, 1, 1) 等于 「0」) return(FALSE
    as.integer(s) <= 255  # 把 255 写入 as.integer(s) <
}
restore_ip_addresses <- function(s) {
    # 定义函数 restore_ip_addresses（参数：字符串）
    res <- character(0)  # 把 character(0) 存入 结果
    n <- nchar(s)  # 把 nchar(字符串) 存入 元素个数
    if (n < 4 || n > 12)
        return(res)  # 若 元素个数 小于 4 或 元素个数 超过 12) return(结果
    for (a in 1:3) for (b in 1:3) for (c in 1:3) {
        # for (数组 in 1:3) for (b in 1:3) for (字符 in 1:3) {
        d <- n - a - b - c  # 把 元素个数 减 数组 减 b 减 字符 存入 d
        if (d >= 1 && d <= 3) {
            # 若 d 不低于 1 且 d 不超过 3
            s1 <- substr(s, 1, a)  # 把 substr(字符串, 1, 数组) 存入 s1
            s2 <- substr(s, a + 1, a + b)  # 把 substr(字符串, 数组 加 1, 数组 加 b) 存入 s2
            s3 <- substr(s, a + b + 1, a + b + c)  # 把 substr(字符串, 数组 加 b 加 1, 数组 加 b 加 字符) 存入 s3
            s4 <- substr(s, a + b + c + 1, n)  # 把 substr(字符串, 数组 加 b 加 字符 加 1, 元素个数) 存入 s4
            if (valid_seg(s1) && valid_seg(s2) && valid_seg(s3) && valid_seg(s4)) {
                res <- c(res, paste(s1, s2, s3, s4, sep = "."))  # 把 字符(结果, paste(s1, s2, s3, s4, sep 赋值为 「.」)) 存入 结果
            }
        }
    }
    res  # 结果
}
got <- restore_ip_addresses("25525511135")  # 把 restore_ip_addresses(「25525511135」) 存入 got
stopifnot(identical(got, c("255.255.11.135", "255.255.111.35")))  # 断言校验
stopifnot(identical(restore_ip_addresses("0000"), "0.0.0.0"))  # 断言校验
stopifnot(length(restore_ip_addresses("abc")) == 0)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
