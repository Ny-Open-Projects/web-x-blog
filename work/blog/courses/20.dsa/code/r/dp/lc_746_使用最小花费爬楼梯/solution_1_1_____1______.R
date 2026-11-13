# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130521152 LeetCode 746. 使用最小花费爬楼梯 —
# R 版（方案1） 定义函数 min_cost_climbing_stairs（参数：cost）
min_cost_climbing_stairs <- function(cost) {
    a <- 0
    b <- 0  # 把 0; b 小于 减 0 存入 数组
    for (i in 3:(length(cost) + 1)) {
        # for (下标 i in 3:(长度(cost) 加 1)) {
        t <- min(a + cost[i - 2], b + cost[i - 1])  # 把 取较小值 数组 加 cost[下标 i 减 2], b 加 cost[下标 i 减 1]) 存入 另一字符串
        a <- b
        b <- t  # 把 b; b 小于 减 另一字符串 存入 数组
    }
    b
}
stopifnot(min_cost_climbing_stairs(c(10, 15, 20)) == 15)  # 断言校验
stopifnot(min_cost_climbing_stairs(c(1, 100, 1, 1, 1, 100, 1, 1, 100, 1)) == 6)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
