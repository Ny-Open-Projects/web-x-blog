# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771 LeetCode 65. 有效数字 — R 版
# 方案4（确定有限状态自动机 DFA，字符原样作为转移键） 定义函数 is_number（参数：字符串）
is_number <- function(s) {
    graph <- list(`0` = list(blank = 0L, sign = 1L, . = 2L, digit = 6L), `1` = list(digit = 6L, . = 2L), `2` = list(digit = 3L),
        `3` = list(digit = 3L, e = 4L), `4` = list(digit = 5L, sign = 7L), `5` = list(digit = 5L), `6` = list(digit = 6L,
            . = 3L, e = 4L), `7` = list(digit = 5L))
    t <- sub("\\s+$", "", sub("^\\s+", "", s, perl = TRUE), perl = TRUE)  # 等价于 trim()
    state <- 0L  # 把 0L 存入 state
    for (ch in strsplit(t, "")[[1]]) {
        # for (字符 in strsplit(另一字符串, 「」)[[1]]) { 若 grepl(「 按位异或 [0 减 9]$」, 字符
        if (grepl("^[0-9]$", ch)) {
            c <- "digit"  # 把 「digit」 存入 字符
        } else if (ch == " ") {
            # 否则，若 字符 等于 「 」
            c <- "blank"  # 把 「blank」 存入 字符
        } else if (ch == "+" || ch == "-") {
            # 否则，若 字符 等于 「 加 」 或 字符 等于 「 加 」
            c <- "sign"  # 把 「sign」 存入 字符
        } else {
            # 否则
            c <- ch  # 原样字符（'e' 直接作键；与 Python 参考一致）
        }
        row <- graph[[as.character(state)]]  # 把 graph[[as.character(state)]] 存入 row
        if (is.null(row) || is.null(row[[c]]))
            return(FALSE)  # 若 is.null(row) 或 is.null(row[[字符]])) return(FALSE
        state <- row[[c]]  # 把 row[[字符]] 存入 state
    }
    state == 3L || state == 5L || state == 6L  # 把 赋值为 3L 或 state 等于 5L 或 state 等于 6L 存入 state
}
stopifnot(is_number("0") == TRUE)  # 断言校验
stopifnot(is_number("abc") == FALSE)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
