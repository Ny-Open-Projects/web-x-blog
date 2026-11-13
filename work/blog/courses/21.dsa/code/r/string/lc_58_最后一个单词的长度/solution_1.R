# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130668538 LeetCode 58. 最后一个单词的长度 — R
# 版（方案1） 定义函数 length_of_last_word（参数：字符串）
length_of_last_word <- function(s) {
    t <- trimws(s)  # 把 trimws(字符串) 存入 另一字符串
    if (nchar(t) == 0)
        return(0L)  # 若 nchar(另一字符串) 等于 0) return(0L
    words <- strsplit(t, " ")[[1]]  # 把 strsplit(另一字符串, 「 」)[[1]] 存入 单词列表
    nchar(words[length(words)])  # nchar(单词列表[长度(单词列表)])
}
stopifnot(length_of_last_word("Hello World") == 5)  # 断言校验
stopifnot(length_of_last_word(" ") == 0)  # 断言校验
stopifnot(length_of_last_word("a") == 1)  # 断言校验
stopifnot(length_of_last_word(" fly me to the moon ") == 4)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
