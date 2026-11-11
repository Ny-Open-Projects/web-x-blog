# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108013114 LeetCode 108013114.
# 贪心策略之BST&BBST_hashtable+dictionary+map — R 版（贪心策略之 BST/BBST/哈希表：Kruskal 最小生成树（并查集
# + 排序））
kruskal_mst <- function(edges) {
    # 定义函数 kruskal_mst（参数：边集） edges: 3 列矩阵 [u, v, w]
    if (nrow(edges) == 0)
        return(0L)  # 若 nrow(边集) 等于 0) return(0L
    ord <- order(edges[, 3])  # 把 order(边集[, 3]) 存入 ord
    parent <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 parent
    find <- function(x) {
        # 定义函数 find（参数：x）
        if (is.null(parent[[as.character(x)]]))
            parent[[as.character(x)]] <- x
        while (parent[[as.character(x)]] != x) {
            # 循环，直到不满足「parent[[as.character(x)]] 不等于 x」
            parent[[as.character(x)]] <- parent[[as.character(parent[[as.character(x)]])]]
            x <- parent[[as.character(x)]]  # 把 parent[[as.character(x)]] 存入 x
        }
        x
    }
    total <- 0L  # 把 0L 存入 总和
    for (i in ord) {
        # for (下标 i in ord) {
        u <- edges[i, 1]
        v <- edges[i, 2]
        w <- edges[i, 3]
        ru <- find(u)
        rv <- find(v)  # 把 find(节点 u); rv 小于 减 find(值) 存入 ru
        if (ru != rv) {
            # 若 ru 不等于 rv
            parent[[as.character(ru)]] <- rv  # 把 rv 存入 parent[[as.character(ru)]]
            total <- total + w  # 把 总和 加 权重 存入 总和
        }
    }
    total  # 总和
}
cases <- list(list(matrix(c(0, 1, 10, 0, 2, 6, 0, 3, 5, 1, 3, 15, 2, 3, 4), ncol = 3, byrow = TRUE), 19L), list(matrix(c(0,
    1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4), ncol = 3, byrow = TRUE), 10L), list(matrix(c(0, 1, 2, 1, 2, 3), ncol = 3,
    byrow = TRUE), 5L), list(matrix(integer(0), ncol = 3), 0L)  # 把 3), 0L) 写入 list(matrix(integer(0), ncol
)
for (idx in seq_along(cases)) {
    # for (idx in seq_along(cases)) {
    got <- kruskal_mst(cases[[idx]][[1]])  # 把 kruskal_mst(cases[[idx]][[1]]) 存入 got
    stopifnot(got == cases[[idx]][[2]])  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
