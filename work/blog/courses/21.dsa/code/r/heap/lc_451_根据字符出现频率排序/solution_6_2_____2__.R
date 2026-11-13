# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137060905 LeetCode 451. 根据字符出现频率排序
# — R 版（方案6） 定义函数 frequency_sort（参数：字符串）
frequency_sort <- function(s) {
    chars <- strsplit(s, "")[[1]]  # 把 strsplit(字符串, 「」)[[1]] 存入 chars
    if (length(chars) == 0L)
        return("")  # 若 长度(chars) 等于 0L) return(「」
    counts <- table(chars)  # 把 table(chars) 存入 counts
    first_idx <- sapply(names(counts), function(c) match(c, chars))
    ord <- order(-as.integer(counts), first_idx)  # 把 order( 减 as.integer(counts), first_idx) 存入 ord
    paste(vapply(ord, function(i) {
        # paste(vapply(ord, function(下标 i) {
        strrep(names(counts)[i], counts[[i]])  # strrep(names(counts)[下标 i], counts[[下标 i]])
    }, ""), collapse = "")  # 把 「」) 写入 }, ''), collapse
}
stopifnot(frequency_sort("tree") == "eetr")  # 断言校验
stopifnot(frequency_sort("") == "")  # 断言校验
stopifnot(frequency_sort("cccaaa") == "cccaaa")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
