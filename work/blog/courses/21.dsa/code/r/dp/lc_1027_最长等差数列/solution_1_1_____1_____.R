# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130687299 LeetCode 1027. 最长等差数列 — R
# 版（方案1） 定义函数 longest_arith_seq_length（参数：数组）
longest_arith_seq_length <- function(nums) {
    n <- length(nums)  # 把 长度(数组) 存入 元素个数
    dp <- vector("list", n)  # 把 vector(「列表」, 元素个数) 存入 DP 表
    for (i in seq_len(n)) dp[[i]] <- new.env(parent = emptyenv())
    best <- 1L  # 把 1L 存入 当前最优
    for (i in seq_len(n)) {
        # for (下标 i in seq_len(元素个数)) { for (下标 j in seq_len(下标 i 减 1)) {
        for (j in seq_len(i - 1)) {
            d <- nums[i] - nums[j]  # 把 数组[下标 i] 减 数组[下标 j] 存入 d
            cur <- if (!is.null(dp[[j]][[as.character(d)]]))
                dp[[j]][[as.character(d)]] + 1L else 2L
            dp[[i]][[as.character(d)]] <- cur  # 把 当前值 存入 dp[[i]][[as.character(d)]]
            if (cur > best)
                best <- cur  # 若 当前值 超过 当前最优) 当前最优 小于 减 当前值
        }
    }
    best  # 当前最优
}
stopifnot(longest_arith_seq_length(c(9, 4, 7, 2, 10)) == 3)  # 断言校验
stopifnot(longest_arith_seq_length(c(3, 6, 9, 12)) == 4)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
