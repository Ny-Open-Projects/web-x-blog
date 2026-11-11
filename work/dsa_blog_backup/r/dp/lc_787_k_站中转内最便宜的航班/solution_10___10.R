# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133472893 LeetCode 787. K站中转内最便宜的航班
# — R 版（方案10） 定义函数 find_cheapest_price（参数：元素个数, flights, src, dst, 下标 k）
find_cheapest_price <- function(n, flights, src, dst, k) {
    INF <- .Machine$integer.max  # 把 Machine$integer.max 存入 INF
    dist <- rep(INF, n)  # 把 rep(INF, 元素个数) 存入 dist
    dist[src + 1] <- 0L  # dist[src 加 1] 小于 减 0L
    for (t in 0:k) {
        # for (另一字符串 in 0:下标 k) {
        nd <- dist  # 把 dist 存入 nd
        for (f in seq_len(nrow(flights))) {
            # for (f in seq_len(nrow(flights))) {
            u <- flights[f, 1] + 1  # 把 flights[f, 1] 加 1 存入 节点 u
            v <- flights[f, 2] + 1  # 把 flights[f, 2] 加 1 存入 值
            w <- flights[f, 3]  # 把 flights[f, 3] 存入 权重
            if (dist[u] != INF && as.numeric(dist[u]) + w < nd[v])
                nd[v] <- as.integer(dist[u] + w)
        }
        dist <- nd  # 把 nd 存入 dist
    }
    if (dist[dst + 1] == INF)
        -1L else dist[dst + 1]  # 若 dist[dst 加 1] 等于 INF) 减 1L else dist[dst 加 1]
}
f <- matrix(c(0, 1, 100, 1, 2, 100, 2, 0, 100, 1, 3, 600, 2, 3, 200), ncol = 3, byrow = TRUE)
stopifnot(find_cheapest_price(4, f, 0, 3, 1) == 700)  # 断言校验
stopifnot(find_cheapest_price(4, f, 0, 0, 1) == 0)  # 断言校验
stopifnot(find_cheapest_price(4, f, 0, 3, 2) == 400)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
