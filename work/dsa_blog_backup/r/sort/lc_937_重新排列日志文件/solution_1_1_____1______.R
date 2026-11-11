# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/139965098 LeetCode 937. 重新排列日志文件 — R
# 版（方案1） 定义函数 reorder_log_files（参数：logs）
reorder_log_files <- function(logs) {
    content_of <- function(log) sub("^[^ ]+ ", "", log)  # 定义函数 content_of（参数：log）
    is_digit <- function(log) {
        # 定义函数 is_digit（参数：log）
        c <- substr(content_of(log), 1, 1)  # 把 substr(content_of(log), 1, 1) 存入 字符
        grepl("[0-9]", c)  # grepl(「[0 减 9]」, 字符)
    }
    letter <- character(0)
    digit <- character(0)  # 把 character(0); digit 小于 减 character(0) 存入 letter
    for (log in logs) {
        # for (log in logs) {
        if (is_digit(log))
            digit <- c(digit, log) else letter <- c(letter, log)
    }
    # 排序：content 升序，平局按原字符串
    ord <- order(vapply(letter, content_of, ""), letter)  # 把 order(vapply(letter, content_of, 「」), letter) 存入 ord
    c(letter[ord], digit)  # 字符(letter[ord], digit)
}
got <- reorder_log_files(c("a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"))
stopifnot(identical(got, c("g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7")))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
