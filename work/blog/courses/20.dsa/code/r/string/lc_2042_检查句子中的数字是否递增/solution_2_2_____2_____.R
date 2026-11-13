# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138481618 LeetCode 2042.
# 检查句子中的数字是否递增 — R 版（方案2） 定义函数 are_numbers_ascending（参数：字符串）
are_numbers_ascending <- function(s) {
    prev <- -1  # 把 减 1 存入 前一个
    for (tok in strsplit(trimws(s), " ")[[1]]) {
        # for (tok in strsplit(trimws(字符串), 「 」)[[1]]) { 若 nchar(tok) 超过 0 且 grepl(「 按位异或 [0 减
        # 9]」, tok
        if (nchar(tok) > 0 && grepl("^[0-9]", tok)) {
            num <- as.numeric(tok)  # 把 as.numeric(tok) 存入 num
            if (num <= prev)
                return(FALSE)  # 若 num 不超过 前一个) return(FALSE
            prev <- num  # 把 num 存入 前一个
        }
    }
    TRUE  # TRUE
}
stopifnot(are_numbers_ascending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))  # 断言校验
stopifnot(!are_numbers_ascending("hello world 5 x 5"))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
