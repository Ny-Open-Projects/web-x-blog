# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130778527 LeetCode 125. 验证回文串 — R
# 版（方案3） 定义函数 is_palindrome（参数：字符串）
is_palindrome <- function(s) {
    f <- tolower(gsub("[^[:alnum:]]", "", s))
    chars <- strsplit(f, "")[[1]]  # 把 strsplit(f, 「」)[[1]] 存入 chars
    identical(chars, rev(chars))  # identical(chars, rev(chars))
}
stopifnot(is_palindrome("A man, a plan, a canal: Panama"))  # 断言校验
stopifnot(!is_palindrome("race a car"))  # 断言校验
stopifnot(is_palindrome(" "))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
