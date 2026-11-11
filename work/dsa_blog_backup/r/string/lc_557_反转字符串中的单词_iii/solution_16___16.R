# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975 LeetCode 557. 反转字符串中的单词III
# — R 版（方案16） 定义函数 reverse_words（参数：字符串）
reverse_words <- function(s) {
    words <- strsplit(s, " ")[[1]]  # 把 strsplit(字符串, 「 」)[[1]] 存入 单词列表
    paste(vapply(words, function(w) paste(rev(strsplit(w, "")[[1]]), collapse = ""), ""), collapse = " ")
}
stopifnot(reverse_words("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc")  # 断言校验
stopifnot(reverse_words("God Ding") == "doG gniD")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
