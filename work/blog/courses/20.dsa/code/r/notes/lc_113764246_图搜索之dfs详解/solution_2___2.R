# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113764246 图搜索之DFS详解 — R 版（方案2）
# 定义函数 dfs_order_graph（参数：graph, 起点）
dfs_order_graph <- function(graph, start) {
    visited <- rep(FALSE, 100L)  # 把 rep(FALSE, 100L) 存入 已访问集合
    order_ <- integer(0)  # 把 integer(0) 存入 order_
    go <- function(c) {
        # 定义函数 go（参数：字符）
        visited[c + 1L] <<- TRUE  # 已访问集合[字符 加 1L] 小于 小于 减 TRUE
        order_ <<- c(order_, c)  # order_ 小于 小于 减 字符(order_, 字符)
        nb <- if (c + 1L <= length(graph) && !is.null(graph[[c + 1L]]))
            graph[[c + 1L]] else integer(0)
        if (length(nb) > 0) {
            # 若 长度(nb) 超过 0 for (nx in nb) {
            for (nx in nb) {
                if (!visited[nx + 1L])
                  go(nx)  # 若 取反 已访问集合[nx 加 1L]) go(nx
            }
        }
    }
    go(start)  # go(起点)
    order_  # order_
}
g <- list(c(1, 2), c(3, 4), c(5), NULL, NULL, NULL)  # 把 列表(字符(1, 2), 字符(3, 4), 字符(5), NULL, NULL, NULL) 存入 g
stopifnot(identical(as.integer(dfs_order_graph(g, 0)), c(0L, 1L, 3L, 4L, 2L, 5L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
