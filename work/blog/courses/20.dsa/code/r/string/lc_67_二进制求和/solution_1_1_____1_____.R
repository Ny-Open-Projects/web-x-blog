# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130724108 LeetCode 67. 二进制求和 — R
# 版（方案1） 定义函数 add_binary（参数：数组, b）
add_binary <- function(a, b) {
    ca <- strsplit(a, "")[[1]]
    cb <- strsplit(b, "")[[1]]  # 把 strsplit(数组, 「」)[[1]]; cb 小于 减 strsplit(b, 「」)[[1]] 存入 ca
    i <- length(ca)
    j <- length(cb)
    carry <- 0  # 把 长度(ca); 下标 j 小于 减 长度(cb); carry 小于 减 0 存入 下标 i
    out <- character(0)  # 把 character(0) 存入 out
    while (i >= 1 || j >= 1 || carry > 0) {
        # 循环，直到不满足「下标 i 不低于 1 或 下标 j 不低于 1 或 carry 超过 0」
        total <- carry  # 把 carry 存入 总和
        if (i >= 1) {
            total <- total + as.integer(ca[i])
            i <- i - 1
        }
        if (j >= 1) {
            total <- total + as.integer(cb[j])
            j <- j - 1
        }
        out <- c(out, as.character(total%%2))  # 把 字符(out, as.character(总和 对…取模 对…取模 2)) 存入 out
        carry <- total%/%2  # 把 总和 对…取模 除以 对…取模 2 存入 carry
    }
    if (length(out) == 0)
        out <- "0"  # 若 长度(out) 等于 0) out 小于 减 「0」
    paste(rev(out), collapse = "")  # 把 「」) 写入 paste(rev(out), collapse
}
stopifnot(add_binary("11", "1") == "100")  # 断言校验
stopifnot(add_binary("1010", "1011") == "10101")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
