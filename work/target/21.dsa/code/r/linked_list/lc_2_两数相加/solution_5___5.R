# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133598918 LeetCode 2. 两数相加 — R
# 版（方案5） 定义函数 add_two_numbers（参数：数组, b）
add_two_numbers <- function(a, b) {
    i <- 1L
    j <- 1L
    carry <- 0L  # 把 1L; 下标 j 小于 减 1L; carry 小于 减 0L 存入 下标 i
    out <- integer(0)  # 把 integer(0) 存入 out
    while (i <= length(a) || j <= length(b) || carry > 0) {
        # 循环，直到不满足「下标 i 不超过 长度(数组) 或 下标 j 不超过 长度(b) 或 carry 超过 0」
        total <- carry  # 把 carry 存入 总和
        if (i <= length(a)) {
            total <- total + a[i]
            i <- i + 1L
        }
        if (j <= length(b)) {
            total <- total + b[j]
            j <- j + 1L
        }
        out <- c(out, total%%10)  # 把 字符(out, 总和 对…取模 对…取模 10) 存入 out
        carry <- total%/%10  # 把 总和 对…取模 除以 对…取模 10 存入 carry
    }
    if (length(out) == 0)
        out <- 0L  # 若 长度(out) 等于 0) out 小于 减 0L
    out  # out
}
stopifnot(identical(add_two_numbers(c(2, 4, 3), c(5, 6, 4)), c(7, 0, 8)))  # 断言校验
stopifnot(identical(add_two_numbers(0, 0), 0))  # 断言校验
stopifnot(identical(add_two_numbers(c(9, 9, 9, 9, 9, 9, 9), c(9, 9, 9, 9)), c(8, 9, 9, 9, 0, 0, 0, 1)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
