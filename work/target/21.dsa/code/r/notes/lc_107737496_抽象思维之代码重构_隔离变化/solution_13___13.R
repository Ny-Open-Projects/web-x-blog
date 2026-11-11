# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496 LeetCode 107737496.
# 代码重构_隔离变化 — R 版（方案13：微型正则匹配 match/matchhere/matchstar） 定义函数 matchstar（参数：字符,
# re, text）
matchstar <- function(c, re, text) {
    i <- 0L  # 把 0L 存入 下标 i
    repeat {
        # repeat {
        if (matchhere(re, substr(text, i + 1L, nchar(text))))
            return(TRUE)
        if (i >= nchar(text))
            break  # 若 下标 i 不低于 nchar(text)) break
        if (substr(text, i + 1L, i + 1L) != c && c != ".")
            break
        i <- i + 1L  # 把 下标 i 加 1L 存入 下标 i
    }
    FALSE  # FALSE
}
matchhere <- function(re, text) {
    # 定义函数 matchhere（参数：re, text）
    if (nchar(re) == 0L)
        return(TRUE)  # 若 nchar(re) 等于 0L) return(TRUE
    if (nchar(re) >= 2L && substr(re, 2L, 2L) == "*") {
        # 若 nchar(re) 不低于 2L 且 substr(re, 2L, 2L) 等于 「 乘 」
        return(matchstar(substr(re, 1L, 1L), substr(re, 3L, nchar(re)), text))
    }
    if (substr(re, 1L, 1L) == "$" && nchar(re) == 1L)
        return(nchar(text) == 0L)
    if (nchar(text) > 0L && (substr(re, 1L, 1L) == "." || substr(re, 1L, 1L) == substr(text, 1L, 1L))) {
        return(matchhere(substr(re, 2L, nchar(re)), substr(text, 2L, nchar(text))))
    }
    FALSE  # FALSE
}
match_re <- function(re, text) {
    # 定义函数 match_re（参数：re, text） 若 nchar(re) 超过 0L 且 substr(re, 1L, 1L) 等于 「 按位异或 」
    if (nchar(re) > 0L && substr(re, 1L, 1L) == "^") {
        return(matchhere(substr(re, 2L, nchar(re)), text))  # 返回 matchhere(substr(re, 2L, nchar(re)), text
    }
    i <- 0L  # 把 0L 存入 下标 i
    repeat {
        # repeat {
        if (matchhere(re, substr(text, i + 1L, nchar(text))))
            return(TRUE)
        if (i >= nchar(text))
            break  # 若 下标 i 不低于 nchar(text)) break
        i <- i + 1L  # 把 下标 i 加 1L 存入 下标 i
    }
    FALSE  # FALSE
}
stopifnot(match_re("abc", "xxabcxx"))  # 断言校验
stopifnot(match_re("a.c", "axc"))  # 断言校验
stopifnot(match_re("a*", "aaaa"))  # 断言校验
stopifnot(!match_re("^a", "ba"))  # 断言校验
stopifnot(match_re("c$", "abc"))  # 断言校验
stopifnot(match_re("a.*c", "aXYZc"))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
