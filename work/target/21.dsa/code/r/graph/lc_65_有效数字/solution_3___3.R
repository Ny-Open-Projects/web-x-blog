# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771 LeetCode 65. 有效数字 — R 版
# 方案3（线性扫描） 定义函数 is_number（参数：字符串）
is_number <- function(s) {
    t <- sub("\\s+$", "", sub("^\\s+", "", s, perl = TRUE), perl = TRUE)  # 等价于 trim()
    if (nchar(t) == 0)
        return(FALSE)  # 若 nchar(另一字符串) 等于 0) return(FALSE
    chars <- strsplit(t, "")[[1]]  # 把 strsplit(另一字符串, 「」)[[1]] 存入 chars
    has_dot <- FALSE  # 把 FALSE 存入 has_dot
    has_e <- FALSE  # 把 FALSE 存入 has_e
    has_digit <- FALSE  # 把 FALSE 存入 has_digit
    for (i in seq_along(chars)) {
        # for (下标 i in seq_along(chars)) {
        ch <- chars[i]  # 把 chars[下标 i] 存入 字符
        if (ch == ".") {
            # 若 字符 等于 「.」
            if (has_dot || has_e)
                return(FALSE)  # 若 has_dot 或 has_e) return(FALSE
            has_dot <- TRUE  # 把 TRUE 存入 has_dot
        } else if (ch == "e" || ch == "E") {
            # 否则，若 字符 等于 「e」 或 字符 等于 「e」
            if (has_e || !has_digit)
                return(FALSE)  # 若 has_e 或 取反 has_digit) return(FALSE
            has_e <- TRUE  # 把 TRUE 存入 has_e
            has_digit <- FALSE  # 把 FALSE 存入 has_digit
        } else if (ch == "+" || ch == "-") {
            # 否则，若 字符 等于 「 加 」 或 字符 等于 「 加 」
            if (i > 1 && chars[i - 1L] != "e" && chars[i - 1L] != "E")
                return(FALSE)
        } else if (grepl("^[0-9]$", ch)) {
            # 否则，若 grepl(「 按位异或 [0 减 9]$」, 字符
            has_digit <- TRUE  # 把 TRUE 存入 has_digit
        } else {
            # 否则
            return(FALSE)  # 返回 FALSE
        }
    }
    has_digit  # has_digit
}
stopifnot(is_number("abc") == FALSE)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
