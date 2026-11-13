# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133596542 LeetCode 17. 电话号码的字母组合 — R
# 版（方案4） 定义函数 letter_combinations（参数：digits）
letter_combinations <- function(digits) {
    if (nchar(digits) == 0)
        return(character(0))  # 若 nchar(digits) 等于 0) return(character(0
    map <- c("", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")  # 把 字符(「」, 「」, 「」, 「」, 「」, 「」, 「」, 「」, 「」, 「」) 存入 映射表
    res <- ""  # 把 「」 存入 结果
    for (ch in strsplit(digits, "")[[1]]) {
        # for (字符 in strsplit(digits, 「」)[[1]]) {
        letters_ <- strsplit(map[as.integer(ch) + 1], "")[[1]]  # 把 strsplit(映射表[as.integer(字符) 加 1], 「」)[[1]] 存入 letters_
        res <- as.vector(outer(res, letters_, paste0))  # 把 as.vector(outer(结果, letters_, paste0)) 存入 结果
    }
    res  # 结果
}
got <- letter_combinations("23")  # 把 letter_combinations(「23」) 存入 got
stopifnot(length(got) == 9, got[1] == "ad", got[9] == "cf")  # 断言校验
stopifnot(length(letter_combinations("")) == 0)  # 断言校验
stopifnot(length(letter_combinations("2")) == 3)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
