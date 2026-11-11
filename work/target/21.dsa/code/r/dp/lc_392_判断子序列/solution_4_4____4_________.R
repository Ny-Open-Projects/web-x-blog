# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130753613 LeetCode 392. 判断子序列 — R
# 版（方案4） 定义函数 is_subsequence（参数：字符串, 另一字符串）
is_subsequence <- function(s, t) {
    si <- 1L  # 把 1L 存入 si
    chars_t <- strsplit(t, "")[[1]]  # 把 strsplit(另一字符串, 「」)[[1]] 存入 chars_t
    chars_s <- strsplit(s, "")[[1]]  # 把 strsplit(字符串, 「」)[[1]] 存入 chars_s
    for (ch in chars_t) {
        # for (字符 in chars_t) {
        if (si <= length(chars_s) && chars_s[si] == ch)
            si <- si + 1L  # 若 si 不超过 长度(chars_s) 且 chars_s[si] 等于 字符) si 小于 减 si 加 1L
    }
    si > length(chars_s)  # si 超过 长度(chars_s)
}
stopifnot(is_subsequence("abc", "ahbgdc"))  # 断言校验
stopifnot(!is_subsequence("axc", "ahbgdc"))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
