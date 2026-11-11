# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130736023 LeetCode 415. 字符串相加 — R
# 版（方案2） 定义函数 add_strings（参数：num1, num2）
add_strings <- function(num1, num2) {
    ca <- strsplit(num1, "")[[1]]
    cb <- strsplit(num2, "")[[1]]
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
        out <- c(out, as.character(total%%10))  # 把 字符(out, as.character(总和 对…取模 对…取模 10)) 存入 out
        carry <- total%/%10  # 把 总和 对…取模 除以 对…取模 10 存入 carry
    }
    if (length(out) == 0)
        out <- "0"  # 若 长度(out) 等于 0) out 小于 减 「0」
    paste(rev(out), collapse = "")  # 把 「」) 写入 paste(rev(out), collapse
}
stopifnot(add_strings("11", "123") == "134")  # 断言校验
stopifnot(add_strings("456", "77") == "533")  # 断言校验
stopifnot(add_strings("0", "0") == "0")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
