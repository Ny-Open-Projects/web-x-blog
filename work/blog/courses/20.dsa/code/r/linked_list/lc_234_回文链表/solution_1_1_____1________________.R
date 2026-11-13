# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133812752 LeetCode 234. 回文链表 — R
# 版（方案1） 定义函数 is_palindrome_list（参数：vals）
is_palindrome_list <- function(vals) {
    if (length(vals) == 0)
        return(TRUE)  # 若 长度(vals) 等于 0) return(TRUE
    identical(vals, rev(vals))  # identical(vals, rev(vals))
}
stopifnot(is_palindrome_list(integer(0)))  # 断言校验
stopifnot(is_palindrome_list(c(1, 2, 2, 1)))  # 断言校验
stopifnot(!is_palindrome_list(c(1, 2)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
