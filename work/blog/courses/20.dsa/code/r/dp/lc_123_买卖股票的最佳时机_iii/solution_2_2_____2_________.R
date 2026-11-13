# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130588647 LeetCode 123. 买卖股票的最佳时机III
# — R 版（方案2） 定义函数 max_profit_iii（参数：价格序列）
max_profit_iii <- function(prices) {
    buy1 <- -Inf
    sell1 <- 0L
    buy2 <- -Inf
    sell2 <- 0L
    for (p in prices) {
        # for (节点 in 价格序列) {
        buy1 <- max(buy1, -p)  # 把 取较大值 buy1, 减 节点) 存入 buy1
        sell1 <- max(sell1, buy1 + p)  # 把 取较大值 sell1, buy1 加 节点) 存入 sell1
        buy2 <- max(buy2, sell1 - p)  # 把 取较大值 buy2, sell1 减 节点) 存入 buy2
        sell2 <- max(sell2, buy2 + p)  # 把 取较大值 sell2, buy2 加 节点) 存入 sell2
    }
    sell2  # sell2
}
stopifnot(max_profit_iii(c(1, 2, 3)) == 2)  # 断言校验
stopifnot(max_profit_iii(c(1, 2, 3, 4, 5)) == 4)  # 断言校验
stopifnot(max_profit_iii(c(7, 6, 4, 3, 1)) == 0)  # 断言校验
stopifnot(max_profit_iii(c(3, 3, 5, 0, 0, 3, 1, 4)) == 6)  # 断言校验
stopifnot(max_profit_iii(c(1)) == 0)  # 断言校验
stopifnot(max_profit_iii(c(1, 2)) == 1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
