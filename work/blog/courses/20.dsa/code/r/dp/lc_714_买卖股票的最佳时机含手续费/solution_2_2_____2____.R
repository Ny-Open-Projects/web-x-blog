# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130741193 LeetCode 714.
# 买卖股票的最佳时机含手续费 — R 版（方案2） 定义函数 max_profit_fee（参数：价格序列, fee）
max_profit_fee <- function(prices, fee) {
    hold <- -prices[1]
    sold <- 0L  # 把 减 价格序列[1]; sold 小于 减 0L 存入 hold
    for (p in prices[-1]) {
        # for (节点 in 价格序列[ 减 1]) {
        nh <- max(hold, sold - p)  # 把 取较大值 hold, sold 减 节点) 存入 nh
        ns <- max(sold, hold + p - fee)  # 把 取较大值 sold, hold 加 节点 减 fee) 存入 ns
        hold <- nh
        sold <- ns  # 把 nh; sold 小于 减 ns 存入 hold
    }
    sold  # sold
}
stopifnot(max_profit_fee(c(1, 3, 2, 8, 4, 9), 2) == 8)  # 断言校验
stopifnot(max_profit_fee(c(1), 1) == 0)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
