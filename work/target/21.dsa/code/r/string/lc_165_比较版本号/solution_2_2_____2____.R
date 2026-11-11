# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135004886 LeetCode 165. 比较版本号 — R
# 版（方案2） 定义函数 compare_version（参数：v1, v2）
compare_version <- function(v1, v2) {
    p1 <- as.numeric(strsplit(v1, "\\.")[[1]])  # 把 as.numeric(strsplit(v1, 「\.」)[[1]]) 存入 p1
    p2 <- as.numeric(strsplit(v2, "\\.")[[1]])  # 把 as.numeric(strsplit(v2, 「\.」)[[1]]) 存入 p2
    n <- max(length(p1), length(p2))  # 把 取较大值 长度(p1), 长度(p2)) 存入 元素个数
    for (i in seq_len(n)) {
        # for (下标 i in seq_len(元素个数)) {
        a <- if (i <= length(p1))
            p1[i] else 0  # 把 if (下标 i 不超过 长度(p1)) p1[下标 i] else 0 存入 数组
        b <- if (i <= length(p2))
            p2[i] else 0  # 把 if (下标 i 不超过 长度(p2)) p2[下标 i] else 0 存入 b
        if (a < b)
            return(-1)  # 若 数组 小于 b) return( 减 1
        if (a > b)
            return(1)  # 若 数组 超过 b) return(1
    }
    0
}
stopifnot(compare_version("1.01", "1.001") == 0)  # 断言校验
stopifnot(compare_version("1.0", "1.0.0") == 0)  # 断言校验
stopifnot(compare_version("0.1", "1.1") == -1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
