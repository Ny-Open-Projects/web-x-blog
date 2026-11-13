# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113548046 图搜索之BFS详解 — R 版（方案1）
# 定义函数 bfs_order（参数：graph, 起点）
bfs_order <- function(graph, start) {
    n <- length(graph)  # 把 长度(graph) 存入 元素个数
    visited <- rep(FALSE, 100L)  # 预分配足够大
    order_ <- integer(0)  # 把 integer(0) 存入 order_
    queue <- start + 1L  # 把 起点 加 1L 存入 队列
    head <- 1L  # 把 1L 存入 头节点
    visited[start + 1L] <- TRUE  # 已访问集合[起点 加 1L] 小于 减 TRUE
    while (head <= length(queue)) {
        # 循环，直到不满足「头节点 不超过 长度(队列」
        c <- queue[head]  # 把 队列[头节点] 存入 字符
        head <- head + 1L  # 把 头节点 加 1L 存入 头节点
        order_ <- c(order_, c - 1L)  # 把 字符(order_, 字符 减 1L) 存入 order_
        nb <- if (c <= length(graph) && !is.null(graph[[c]]))
            graph[[c]] else integer(0)
        if (length(nb) > 0) {
            # 若 长度(nb) 超过 0 for (nx in nb) { 若 取反 已访问集合[nx]
            for (nx in nb) {
                if (!visited[nx]) {
                  visited[nx] <- TRUE  # 把 TRUE 存入 visited[nx]
                  queue <- c(queue, nx)  # 把 字符(队列, nx) 存入 队列
                }
            }
        }
    }
    order_  # order_
}
g <- list(c(2, 3), c(4, 5), c(6), NULL, NULL, NULL)  # 把 列表(字符(2, 3), 字符(4, 5), 字符(6), NULL, NULL, NULL) 存入 g
stopifnot(identical(as.integer(bfs_order(g, 0)), 0:5))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
