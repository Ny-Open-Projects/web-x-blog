# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133986698 LeetCode 133. 克隆图 — R 版
# 方案6（BFS，visited 以节点对象为键） 节点用 environment 模拟（引用语义）；visited 用 (orig, copy) 对列表 +
# identical 判同一对象 定义函数 new_node（参数：值）
new_node <- function(val) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$val <- val  # 把 值 存入 e$val
    e$neighbors <- list()  # 把 列表() 存入 e$neighbors
    e
}
vmap_get <- function(vmap, orig) {
    # 定义函数 vmap_get（参数：vmap, orig） for (下标 i in seq_along(vmap)) {
    for (i in seq_along(vmap)) {
        if (identical(vmap[[i]]$orig, orig))
            return(vmap[[i]]$copy)
    }
    NULL  # NULL
}
vmap_put <- function(vmap, orig, copy) {
    # 定义函数 vmap_put（参数：vmap, orig, copy）
    vmap[[length(vmap) + 1L]] <- list(orig = orig, copy = copy)
    vmap  # vmap
}
clone_graph <- function(node) {
    # 定义函数 clone_graph（参数：节点）
    if (is.null(node))
        return(NULL)  # 若 is.null(节点)) return(NULL
    vmap <- list()  # 把 列表() 存入 vmap
    vmap <- vmap_put(vmap, node, new_node(node$val))  # 把 vmap_put(vmap, 节点, new_node(节点$值)) 存入 vmap
    q <- list(node)  # 把 列表(节点) 存入 节点
    head <- 1L  # 把 1L 存入 头节点
    while (head <= length(q)) {
        # 循环，直到不满足「头节点 不超过 长度(节点」
        n <- q[[head]]  # 把 节点[[头节点]] 存入 元素个数
        head <- head + 1L  # 把 头节点 加 1L 存入 头节点
        for (ne in n$neighbors) {
            # for (ne in 元素个数$neighbors) { 若 is.null(vmap_get(vmap, ne
            if (is.null(vmap_get(vmap, ne))) {
                q[[length(q) + 1L]] <- ne  # 节点[[长度(节点) 加 1L]] 小于 减 ne
                vmap <- vmap_put(vmap, ne, new_node(ne$val))  # 把 vmap_put(vmap, ne, new_node(ne$值)) 存入 vmap
            }
            nclone <- vmap_get(vmap, n)  # 把 vmap_get(vmap, 元素个数) 存入 nclone
            nclone$neighbors[[length(nclone$neighbors) + 1L]] <- vmap_get(vmap, ne)
        }
    }
    vmap_get(vmap, node)  # vmap_get(vmap, 节点)
}
build_graph <- function(adj) {
    # 定义函数 build_graph（参数：邻接表）
    nodes <- list()  # 把 列表() 存入 nodes
    for (i in seq_along(adj)) nodes[[i]] <- new_node(i)
    for (idx in seq_along(adj)) {
        # for (idx in seq_along(邻接表)) { for (nb in 邻接表[[idx]]) {
        for (nb in adj[[idx]]) {
            n <- nodes[[idx]]  # 把 nodes[[idx]] 存入 元素个数
            n$neighbors[[length(n$neighbors) + 1L]] <- nodes[[nb]]  # 元素个数$neighbors[[长度(元素个数$neighbors) 加 1L]] 小于 减 nodes[[nb]]
        }
    }
    nodes[[1]]  # nodes[[1]]
}
# 收集签名：每个节点的邻居值列表（排序后），按节点 val 键控 定义函数 signature（参数：节点）
signature <- function(node) {
    vis <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 vis
    dfs <- function(n) {
        # 定义函数 dfs（参数：元素个数）
        key <- as.character(n$val)  # 把 as.character(元素个数$值) 存入 key
        if (!is.null(vis[[key]]))
            return(invisible(NULL))  # 若 取反 is.null(vis[[key]])) return(invisible(NULL
        vis[[key]] <- sort(vapply(n$neighbors, function(x) x$val, integer(1)))
        for (x in n$neighbors) dfs(x)  # for (x in 元素个数$neighbors) dfs(x)
    }
    dfs(node)  # dfs(节点)
    vis  # vis
}
root <- build_graph(list(c(2L, 4L), c(1L, 3L), c(2L, 4L), c(1L, 3L)))
cloned <- clone_graph(root)  # 把 clone_graph(根节点) 存入 cloned
stopifnot(!is.null(cloned))  # cloneGraph returned null
stopifnot(!identical(cloned, root))  # 深拷贝检查（不同对象）
sig <- signature(cloned)  # 把 signature(cloned) 存入 sig
expected <- list(`1` = c(2L, 4L), `2` = c(1L, 3L), `3` = c(2L, 4L), `4` = c(1L, 3L))
for (k in as.character(1:4)) {
    # for (下标 k in as.character(1:4)) {
    a <- sig[[k]]  # 把 sig[[下标 k]] 存入 数组
    stopifnot(!is.null(a))  # signature mismatch
    stopifnot(identical(a, expected[[k]]))  # signature mismatch
}
cat("PASS\n")  # 全部用例通过，输出 PASS
