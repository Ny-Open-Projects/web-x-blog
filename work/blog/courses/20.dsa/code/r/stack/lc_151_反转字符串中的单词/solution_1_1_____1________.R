# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130846022 LeetCode 151. 反转字符串中的单词 —
# R 版（方案1） 定义函数 reverse_words（参数：字符串）
reverse_words <- function(s) {
    words <- strsplit(trimws(s), "\\s+")[[1]]  # 把 strsplit(trimws(字符串), 「\字符串 加 」)[[1]] 存入 单词列表
    paste(rev(words), collapse = " ")  # 把 「 」) 写入 paste(rev(words), collapse
}
stopifnot(reverse_words("the sky is blue") == "blue is sky the")  # 断言校验
stopifnot(reverse_words("  hello world  ") == "world hello")  # 断言校验
stopifnot(reverse_words("a good   example") == "example good a")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
