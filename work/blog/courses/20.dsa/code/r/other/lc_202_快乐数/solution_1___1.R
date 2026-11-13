# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135124945 LeetCode 202. 快乐数 — R
# 版（方案1） 定义函数 bit_square_sum（参数：元素个数）
bit_square_sum <- function(n) {
    s <- 0  # 把 0 存入 字符串
    while (n > 0) {
        # 循环，直到不满足「元素个数 超过 0」
        d <- n%%10  # 把 元素个数 对…取模 对…取模 10 存入 d
        s <- s + d * d  # 把 字符串 加 d 乘 d 存入 字符串
        n <- n%/%10  # 把 元素个数 对…取模 除以 对…取模 10 存入 元素个数
    }
    s  # 字符串
}
is_happy <- function(n) {
    # 定义函数 is_happy（参数：元素个数）
    seen <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 已见集合
    while (n != 1 && is.null(seen[[as.character(n)]])) {
        # 循环，直到不满足「元素个数 不等于 1 且 is.null(已见集合[[as.character(元素个数)]]」
        seen[[as.character(n)]] <- TRUE  # 把 TRUE 存入 seen[[as.character(n)]]
        n <- bit_square_sum(n)  # 把 bit_square_sum(元素个数) 存入 元素个数
    }
    n == 1  # 把 赋值为 1 存入 元素个数
}
stopifnot(bit_square_sum(1) == 1, bit_square_sum(19) == 82, bit_square_sum(82) == 68)  # 断言校验
stopifnot(is_happy(19), is_happy(1), !is_happy(2))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
