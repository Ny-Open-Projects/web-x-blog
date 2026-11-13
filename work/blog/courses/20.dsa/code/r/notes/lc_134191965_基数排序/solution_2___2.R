# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134191965 数据结构与算法之排序: 基数排序 — R
# 版（方案2） 定义函数 radix_sort（参数：数组）
radix_sort <- function(nums) {
    if (length(nums) == 0)
        return(nums)  # 若 长度(数组) 等于 0) return(数组
    mn <- min(nums)
    mx <- max(nums)  # 把 取较小值 数组); mx 小于 减 取较大值 数组) 存入 mn
    offset <- if (mn < 0)
        -mn else 0  # 把 if (mn 小于 0) 减 mn else 0 存入 offset
    adj <- as.numeric(nums) + offset  # 把 as.numeric(数组) 加 offset 存入 邻接表
    max_adj <- max(adj)  # 把 取较大值 邻接表) 存入 max_adj
    radix <- 1  # 把 1 存入 radix
    tmp <- numeric(length(adj))  # 把 numeric(长度(邻接表)) 存入 临时变量
    while (max_adj >= radix) {
        # 循环，直到不满足「max_adj 不低于 radix」
        bucket <- rep(0, 10)  # 把 rep(0, 10) 存入 bucket
        for (v in adj) {
            # for (值 in 邻接表) {
            d <- floor(v/radix)%%10  # 把 floor(值 除以 radix) 对…取模 对…取模 10 存入 d
            bucket[d + 1] <- bucket[d + 1] + 1  # bucket[d 加 1] 小于 减 bucket[d 加 1] 加 1
        }
        for (i in 2:10) bucket[i] <- bucket[i] + bucket[i - 1]
        for (i in length(adj):1) {
            # for (下标 i in 长度(邻接表):1) {
            d <- floor(adj[i]/radix)%%10  # 把 floor(邻接表[下标 i] 除以 radix) 对…取模 对…取模 10 存入 d
            tmp[bucket[d + 1]] <- adj[i]  # 临时变量[bucket[d 加 1]] 小于 减 邻接表[下标 i]
            bucket[d + 1] <- bucket[d + 1] - 1  # bucket[d 加 1] 小于 减 bucket[d 加 1] 减 1
        }
        for (i in seq_along(adj)) adj[i] <- tmp[i]  # for (下标 i in seq_along(邻接表)) 邻接表[下标 i] 小于 减 临时变量[下标 i]
        radix <- radix * 10  # 把 radix 乘 10 存入 radix
    }
    as.integer(adj - offset)  # as.integer(邻接表 减 offset)
}
stopifnot(identical(radix_sort(c(5, 4, 3, 2, 1)), 1:5))  # 断言校验
stopifnot(identical(radix_sort(c(3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)), c(1L, 1L, 2L, 3L, 3L, 4L, 5L, 5L, 5L, 6L, 9L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
