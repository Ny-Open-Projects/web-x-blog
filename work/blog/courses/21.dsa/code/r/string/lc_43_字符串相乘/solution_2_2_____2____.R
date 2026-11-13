# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130701795 LeetCode 43. 字符串相乘 — R
# 版（方案2） 定义函数 multiply_str（参数：num1, num2）
multiply_str <- function(num1, num2) {
    if (num1 == "0" || num2 == "0")
        return("0")  # 若 num1 等于 「0」 或 num2 等于 「0」) return(「0」
    ca <- strsplit(num1, "")[[1]]
    cb <- strsplit(num2, "")[[1]]
    m <- length(ca)
    n <- length(cb)  # 把 长度(ca); 元素个数 小于 减 长度(cb) 存入 映射表
    result <- rep(0L, m + n)  # 把 rep(0L, 映射表 加 元素个数) 存入 结果
    for (i in m:1) {
        # for (下标 i in 映射表:1) { for (下标 j in 元素个数:1) {
        for (j in n:1) {
            mul <- (as.integer(ca[i])) * (as.integer(cb[j]))  # 把 (as.integer(ca[下标 i])) 乘 (as.integer(cb[下标 j])) 存入 mul
            p1 <- i + j - 1
            p2 <- i + j  # 把 下标 i 加 下标 j 减 1; p2 小于 减 下标 i 加 下标 j 存入 p1
            total <- mul + result[p2]  # 把 mul 加 结果[p2] 存入 总和
            result[p2] <- total%%10  # 把 总和 对…取模 对…取模 10 存入 result[p2]
            result[p1] <- result[p1] + total%/%10  # 把 结果[p1] 加 总和 对…取模 除以 对…取模 10 存入 result[p1]
        }
    }
    digits <- result[result != 0 | cumsum(result != 0) > 0 | seq_along(result) == length(result)]
    # 简化：拼接后去前导零
    s <- paste(result, collapse = "")  # 把 paste(结果, collapse 赋值为 「」) 存入 字符串
    s <- sub("^0+", "", s)  # 把 sub(「 按位异或 0 加 」, 「 按位异或 0 加 」, 字符串) 存入 字符串
    if (nchar(s) == 0)
        "0" else s  # 若 nchar(字符串) 等于 0) 「0」 else 字符串
}
stopifnot(multiply_str("2", "3") == "6")  # 断言校验
stopifnot(multiply_str("123", "456") == "56088")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
