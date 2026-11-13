# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130515763 LeetCode 121. 买卖股票的最佳时机 —
# R 版（方案6） 定义函数 max_profit_stock（参数：价格序列）
max_profit_stock <- function(prices) {
    min_p <- .Machine$integer.max
    best <- 0L  # 把 Machine$integer.max; 当前最优 小于 减 0L 存入 min_p
    for (p in prices) {
        # for (节点 in 价格序列) {
        if (p < min_p)
            min_p <- p  # 若 节点 小于 min_p) min_p 小于 减 节点
        if (p - min_p > best)
            best <- p - min_p  # 若 节点 减 min_p 超过 当前最优) 当前最优 小于 减 节点 减 min_p
    }
    best  # 当前最优
}
stopifnot(max_profit_stock(c(7, 1, 5, 3, 6, 4)) == 5)  # 断言校验
stopifnot(max_profit_stock(c(7, 6, 4, 3, 1)) == 0)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
