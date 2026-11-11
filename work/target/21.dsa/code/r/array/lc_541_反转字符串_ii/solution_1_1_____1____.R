# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134588341 LeetCode 541. 反转字符串II — R
# 版（方案1） 定义函数 reverse_str（参数：字符串, 下标 k）
reverse_str <- function(s, k) {
    chars <- strsplit(s, "")[[1]]  # 把 strsplit(字符串, 「」)[[1]] 存入 chars
    n <- length(chars)  # 把 长度(chars) 存入 元素个数
    out <- chars  # 把 chars 存入 out
    i <- 1  # 把 1 存入 下标 i
    while (i <= n) {
        # 循环，直到不满足「下标 i 不超过 元素个数」
        e <- min(i + k - 1, n)  # 把 取较小值 下标 i 加 下标 k 减 1, 元素个数) 存入 e
        out[i:e] <- rev(chars[i:e])  # 把 rev(chars[下标 i:e]) 存入 out[i:e]
        i <- i + 2 * k  # 把 下标 i 加 2 乘 下标 k 存入 下标 i
    }
    paste(out, collapse = "")  # 把 「」) 写入 paste(out, collapse
}
stopifnot(reverse_str("abcdefg", 2) == "bacdfeg")  # 断言校验
stopifnot(reverse_str("abcd", 2) == "bacd")  # 断言校验
stopifnot(reverse_str("abc", 1) == "abc")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
