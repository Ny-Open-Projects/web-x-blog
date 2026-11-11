# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135004189 LeetCode 3. 无重复字符的最长子串 —
# R 版（方案1） 定义函数 length_of_longest_substring（参数：字符串）
length_of_longest_substring <- function(s) {
    chars <- strsplit(s, "")[[1]]  # 把 strsplit(字符串, 「」)[[1]] 存入 chars
    st <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 st
    left <- 1L
    max_len <- 0L  # 把 1L; max_len 小于 减 0L 存入 左边界
    for (right in seq_along(chars)) {
        # for (右边界 in seq_along(chars)) {
        c <- chars[right]  # 把 chars[右边界] 存入 字符
        while (!is.null(st[[c]])) {
            # 循环，直到不满足「取反 is.null(st[[字符]]」
            rm(list = chars[left], envir = st)  # 把 chars[左边界], envir 赋值为 st) 写入 rm(list
            left <- left + 1L  # 把 左边界 加 1L 存入 左边界
        }
        st[[c]] <- TRUE  # 把 TRUE 存入 st[[c]]
        len <- right - left + 1L  # 把 右边界 减 左边界 加 1L 存入 长度
        if (len > max_len)
            max_len <- len  # 若 长度 超过 max_len) max_len 小于 减 长度
    }
    max_len  # max_len
}
stopifnot(length_of_longest_substring("abcabcbb") == 3L)  # 断言校验
stopifnot(length_of_longest_substring("bbbbb") == 1L)  # 断言校验
stopifnot(length_of_longest_substring("pwwkew") == 3L)  # 断言校验
stopifnot(length_of_longest_substring("") == 0L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
