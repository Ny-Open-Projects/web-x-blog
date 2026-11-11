# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135154838 LeetCode 242. 有效的字母异位词 — R
# 版（方案2） 定义函数 is_anagram（参数：字符串, 另一字符串）
is_anagram <- function(s, t) {
    if (nchar(s) != nchar(t))
        return(FALSE)  # 若 nchar(字符串) 不等于 nchar(另一字符串)) return(FALSE
    identical(sort(strsplit(s, "")[[1]]), sort(strsplit(t, "")[[1]]))
}
stopifnot(is_anagram("anagram", "nagaram"))  # 断言校验
stopifnot(!is_anagram("rat", "car"))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
