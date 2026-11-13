# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145295630 LeetCode 1047.
# 删除字符串中的所有相邻重复项 — R 版（方案1） 定义函数 remove_duplicates_str（参数：字符串）
remove_duplicates_str <- function(s) {
    chars <- strsplit(s, "")[[1]]  # 把 strsplit(字符串, 「」)[[1]] 存入 chars
    st <- character(0)  # 把 character(0) 存入 st
    for (c in chars) {
        # for (字符 in chars) {
        if (length(st) > 0 && st[length(st)] == c)
            st <- st[-length(st)]  # 若 长度(st) 超过 0 且 st[长度(st)] 等于 字符) st 小于 减 st[ 减 长度(st)]
 else st <- c(st, c)  # 否则
    }
    paste(st, collapse = "")  # 把 「」) 写入 paste(st, collapse
}
stopifnot(remove_duplicates_str("abbaca") == "ca")  # 断言校验
stopifnot(remove_duplicates_str("azxxzy") == "ay")  # 断言校验
stopifnot(remove_duplicates_str("") == "")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
