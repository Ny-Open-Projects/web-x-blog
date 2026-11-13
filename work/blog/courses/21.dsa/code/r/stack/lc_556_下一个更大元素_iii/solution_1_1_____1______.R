# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397820 LeetCode 556. 下一个更大元素 III —
# R 版（方案1） 定义函数 next_greater_element_iii（参数：元素个数）
next_greater_element_iii <- function(n) {
    d <- as.integer(rev(as.integer(strsplit(as.character(n), "")[[1]])))
    d <- rev(d)  # 正序
    m <- length(d)  # 把 长度(d) 存入 映射表
    i <- m - 1  # 把 映射表 减 1 存入 下标 i
    while (i >= 1 && d[i] >= d[i + 1]) i <- i - 1
    if (i == 0)
        return(-1L)  # 若 下标 i 等于 0) return( 减 1L
    j <- m  # 把 映射表 存入 下标 j
    while (d[j] <= d[i]) j <- j - 1  # 循环，直到不满足「d[下标 j] 不超过 d[下标 i]) 下标 j 小于 减 下标 j 减 1」
    t <- d[i]
    d[i] <- d[j]
    d[j] <- t  # 把 d[下标 i]; d[下标 i] 小于 减 d[下标 j]; d[下标 j] 小于 减 另一字符串 存入 另一字符串
    if (i + 1 < m)
        d[(i + 1):m] <- rev(d[(i + 1):m])
    res <- as.numeric(paste(d, collapse = ""))  # 把 as.numeric(paste(d, collapse 赋值为 「」)) 存入 结果
    if (res > 2147483647)
        return(-1L)  # 若 结果 超过 2147483647) return( 减 1L
    as.integer(res)  # as.integer(结果)
}
stopifnot(next_greater_element_iii(12) == 21)  # 断言校验
stopifnot(next_greater_element_iii(21) == -1)  # 断言校验
stopifnot(next_greater_element_iii(1) == -1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
