# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138290964 LeetCode 482. 密钥格式化 — R
# 版（方案2） 定义函数 license_key_formatting（参数：字符串, 下标 k）
license_key_formatting <- function(s, k) {
    cleaned <- toupper(gsub("-", "", s))  # 把 toupper(gsub(「 减 」, 「 减 」, 字符串)) 存入 cleaned
    chars <- strsplit(cleaned, "")[[1]]  # 把 strsplit(cleaned, 「」)[[1]] 存入 chars
    n <- length(chars)  # 把 长度(chars) 存入 元素个数
    if (n == 0)
        return("")  # 若 元素个数 等于 0) return(「」
    first <- n%%k  # 把 元素个数 对…取模 对…取模 下标 k 存入 first
    out <- character(0)  # 把 character(0) 存入 out
    idx <- 1  # 把 1 存入 idx
    if (first > 0) {
        # 若 first 超过 0
        out <- c(out, chars[idx:(idx + first - 1)])  # 把 字符(out, chars[idx:(idx 加 first 减 1)]) 存入 out
        idx <- idx + first  # 把 idx 加 first 存入 idx
        if (idx <= n)
            out <- c(out, "-")  # 若 idx 不超过 元素个数) out 小于 减 字符(out, 「 减 」
    }
    while (idx <= n) {
        # 循环，直到不满足「idx 不超过 元素个数」
        out <- c(out, chars[idx:(idx + k - 1)])  # 把 字符(out, chars[idx:(idx 加 下标 k 减 1)]) 存入 out
        idx <- idx + k  # 把 idx 加 下标 k 存入 idx
        if (idx <= n)
            out <- c(out, "-")  # 若 idx 不超过 元素个数) out 小于 减 字符(out, 「 减 」
    }
    paste(out, collapse = "")  # 把 「」) 写入 paste(out, collapse
}
stopifnot(license_key_formatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W")  # 断言校验
stopifnot(license_key_formatting("2-5g-3-J", 2) == "2-5G-3J")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
