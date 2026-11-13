# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108717090 减治策略之详解Dijkstra算法 — R
# 版（方案1） 定义函数 dijkstra_shortest（参数：edges_list, 起点）
dijkstra_shortest <- function(edges_list, start) {
    n <- length(edges_list)  # 把 长度(edges_list) 存入 元素个数
    dist <- rep(.Machine$integer.max, n)  # 把 rep(.Machine$integer.max, 元素个数) 存入 dist
    visited <- rep(FALSE, n)  # 把 rep(FALSE, 元素个数) 存入 已访问集合
    dist[start + 1L] <- 0L  # dist[起点 加 1L] 小于 减 0L
    repeat {
        # repeat {
        u <- NA  # 把 NA 存入 节点 u
        for (i in 1:n) {
            # for (下标 i in 1:元素个数) {
            if (!visited[i] && (is.na(u) || dist[i] < dist[u]))
                u <- i
        }
        if (is.na(u) || dist[u] == .Machine$integer.max)
            break  # 若 is.na(节点 u) 或 dist[节点 u] 等于 .Machine$integer.max) break
        visited[u] <- TRUE  # 把 TRUE 存入 visited[u]
        nb <- if (!is.null(edges_list[[u]]))
            edges_list[[u]] else list()
        if (length(nb) > 0) {
            # 若 长度(nb) 超过 0 for (e in nb) {
            for (e in nb) {
                v <- e[1] + 1L  # 把 e[1] 加 1L 存入 值
                w <- e[2]  # 把 e[2] 存入 权重
                nd <- as.numeric(dist[u]) + w  # 把 as.numeric(dist[节点 u]) 加 权重 存入 nd
                if (nd < dist[v] && nd < .Machine$integer.max)
                  dist[v] <- as.integer(nd)
            }
        }
    }
    dist  # dist
}
g <- list(list(c(1L, 10L), c(2L, 3L)), list(c(2L, 1L), c(3L, 2L)), list(c(1L, 4L), c(3L, 8L)), list(c(4L, 7L)),
    list())
d <- dijkstra_shortest(g, 0)  # 把 dijkstra_shortest(g, 0) 存入 d
stopifnot(d[1] == 0, d[2] == 7, d[3] == 3, d[4] == 9, d[5] == 16)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
