# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133651611 LeetCode 133651611.
# 图及其深度和广度优先遍历实现 — R 版（方案6） 邻接表用 environment 引用语义 定义函数 Graph（参数：无）
Graph <- function() {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$adj <- list()  # 把 列表() 存入 e$adj
    class(e) <- "Graph"  # 把 「Graph」 存入 class(e)
    e
}
add_edge <- function(g, from, to) {
    # 定义函数 add_edge（参数：g, from, to）
    if (is.null(g$adj[[as.character(from)]]))
        g$adj[[as.character(from)]] <- c()
    if (is.null(g$adj[[as.character(to)]]))
        g$adj[[as.character(to)]] <- c()
    g$adj[[as.character(from)]] <- c(g$adj[[as.character(from)]], from * 0 + to)
    g$adj[[as.character(to)]] <- c(g$adj[[as.character(to)]], to * 0 + from)
    invisible(NULL)  # invisible(NULL)
}
dfs <- function(g, start) {
    # 定义函数 dfs（参数：g, 起点）
    visited <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 已访问集合
    result <- c()  # 把 字符() 存入 结果
    helper <- function(node) {
        # 定义函数 helper（参数：节点）
        if (!is.null(visited[[as.character(node)]]))
            return(invisible(NULL))
        visited[[as.character(node)]] <- TRUE  # 把 TRUE 存入 visited[[as.character(node)]]
        result <<- c(result, node)  # 结果 小于 小于 减 字符(结果, 节点)
        for (nb in g$adj[[as.character(node)]] %||% c()) helper(nb)
    }
    helper(start)  # helper(起点)
    as.integer(result)  # as.integer(结果)
}
`%||%` <- function(a, b) if (is.null(a)) b else a
bfs <- function(g, start) {
    # 定义函数 bfs（参数：g, 起点）
    visited <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 已访问集合
    visited[[as.character(start)]] <- TRUE  # 把 TRUE 存入 visited[[as.character(start)]]
    result <- c()  # 把 字符() 存入 结果
    queue <- c(start)  # 把 字符(起点) 存入 队列
    head <- 1L  # 把 1L 存入 头节点
    while (head <= length(queue)) {
        # 循环，直到不满足「头节点 不超过 长度(队列」
        node <- queue[head]  # 把 队列[头节点] 存入 节点
        head <- head + 1L  # 把 头节点 加 1L 存入 头节点
        result <- c(result, node)  # 把 字符(结果, 节点) 存入 结果
        nbs <- g$adj[[as.character(node)]] %||% c()  # 把 g$邻接表[[as.character(节点)]] 对…取模 或 对…取模 字符() 存入 nbs
        for (nb in nbs) {
            # for (nb in nbs) { 若 is.null(已访问集合[[as.character(nb)]]
            if (is.null(visited[[as.character(nb)]])) {
                visited[[as.character(nb)]] <- TRUE  # 把 TRUE 存入 visited[[as.character(nb)]]
                queue <- c(queue, nb)  # 把 字符(队列, nb) 存入 队列
            }
        }
    }
    as.integer(result)  # as.integer(结果)
}
eq <- function(a, b) identical(as.integer(a), as.integer(b))  # 定义函数 eq（参数：数组, b）
# case 1: 方形图 0-1-3-2-0
g1 <- Graph()  # 把 Graph() 存入 g1
add_edge(g1, 0L, 1L)  # add_edge(g1, 0L, 1L)
add_edge(g1, 0L, 2L)  # add_edge(g1, 0L, 2L)
add_edge(g1, 1L, 3L)  # add_edge(g1, 1L, 3L)
add_edge(g1, 2L, 3L)  # add_edge(g1, 2L, 3L)
stopifnot(eq(dfs(g1, 0L), c(0L, 1L, 3L, 2L)))  # 断言校验
stopifnot(eq(bfs(g1, 0L), c(0L, 1L, 2L, 3L)))  # 断言校验
# case 2: 从另一节点出发
stopifnot(eq(dfs(g1, 2L), c(2L, 0L, 1L, 3L)))  # 断言校验
stopifnot(eq(bfs(g1, 2L), c(2L, 0L, 3L, 1L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
