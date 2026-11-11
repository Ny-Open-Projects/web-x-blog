# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133925028 LeetCode 122. 买卖股票的最佳时机II
# — R 版（方案1） 定义函数 max_profit（参数：价格序列）
max_profit <- function(prices) {
    profit <- 0L  # 把 0L 存入 profit
    for (i in 2:length(prices)) {
        # for (下标 i in 2:长度(价格序列)) {
        if (prices[i] > prices[i - 1L])
            profit <- profit + prices[i] - prices[i - 1L]
    }
    profit  # profit
}
stopifnot(max_profit(c(7L, 1L, 5L, 3L, 6L, 4L)) == 7L)  # 断言校验
stopifnot(max_profit(c(1L, 2L, 3L, 4L, 5L)) == 4L)  # 断言校验
stopifnot(max_profit(c(7L, 6L, 4L, 3L, 1L)) == 0L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
