# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136838836 LeetCode 791. 自定义字符串排序 — R
# 版（方案1） 定义函数 custom_sort_string（参数：order, 字符串）
custom_sort_string <- function(order, s) {
    count <- table(strsplit(s, "")[[1]])  # 把 table(strsplit(字符串, 「」)[[1]]) 存入 计数
    out <- character(0)  # 把 character(0) 存入 out
    for (c in strsplit(order, "")[[1]]) {
        # for (字符 in strsplit(order, 「」)[[1]]) { 若 取反 is.na(计数[字符]) 且 计数[[字符]] 超过 0
        if (!is.na(count[c]) && count[[c]] > 0) {
            out <- c(out, rep(c, count[[c]]))  # 把 字符(out, rep(字符, 计数[[字符]])) 存入 out
            count[[c]] <- 0  # 把 0 存入 count[[c]]
        }
    }
    rest <- character(0)  # 把 character(0) 存入 rest
    for (c in names(count)) {
        # for (字符 in names(计数)) {
        if (count[[c]] > 0)
            rest <- c(rest, rep(c, count[[c]]))  # 若 计数[[字符]] 超过 0) rest 小于 减 字符(rest, rep(字符, 计数[[字符]]
    }
    paste(c(out, rest), collapse = "")  # 把 「」) 写入 paste(c(out, rest), collapse
}
stopifnot(custom_sort_string("cba", "abcd") == "cbad")  # 断言校验
stopifnot(custom_sort_string("bcafg", "abcd") == "bcad")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
