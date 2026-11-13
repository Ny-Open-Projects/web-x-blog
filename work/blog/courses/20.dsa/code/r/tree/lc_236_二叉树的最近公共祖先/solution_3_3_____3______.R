# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136528287 LeetCode 236. 二叉树的最近公共祖先
# — R 版（方案3） 树节点：R 必须 environment 引用语义（list 是值语义） 定义函数 TreeNode（参数：值, 左边界
# 赋值为 NULL, 右边界 赋值为 NULL）
TreeNode <- function(val, left = NULL, right = NULL) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$val <- val
    e$left <- left
    e$right <- right  # 把 值; e$左边界 小于 减 左边界; e$右边界 小于 减 右边界 存入 e$val
    class(e) <- "TreeNode"  # 把 「TreeNode」 存入 class(e)
    e
}
build_tree <- function(vals) {
    # 定义函数 build_tree（参数：vals）
    if (length(vals) == 0 || is.na(vals[[1]]))
        return(NULL)  # 若 长度(vals) 等于 0 或 is.na(vals[[1]])) return(NULL
    root <- TreeNode(vals[[1]])  # 把 TreeNode(vals[[1]]) 存入 根节点
    queue <- list(root)  # 把 列表(根节点) 存入 队列
    head <- 1L  # 把 1L 存入 头节点
    i <- 2L  # 把 2L 存入 下标 i
    while (head <= length(queue) && i <= length(vals)) {
        # 循环，直到不满足「头节点 不超过 长度(队列) 且 下标 i 不超过 长度(vals」
        node <- queue[[head]]  # 把 队列[[头节点]] 存入 节点
        head <- head + 1L  # 把 头节点 加 1L 存入 头节点
        if (i <= length(vals)) {
            # 若 下标 i 不超过 长度(vals 若 取反 is.na(vals[[下标 i]]
            if (!is.na(vals[[i]])) {
                node$left <- TreeNode(vals[[i]])  # 把 TreeNode(vals[[下标 i]]) 存入 node$left
                queue[[length(queue) + 1L]] <- node$left  # 队列[[长度(队列) 加 1L]] 小于 减 节点$左边界
            }
            i <- i + 1L  # 把 下标 i 加 1L 存入 下标 i
        }
        if (i <= length(vals)) {
            # 若 下标 i 不超过 长度(vals 若 取反 is.na(vals[[下标 i]]
            if (!is.na(vals[[i]])) {
                node$right <- TreeNode(vals[[i]])  # 把 TreeNode(vals[[下标 i]]) 存入 node$right
                queue[[length(queue) + 1L]] <- node$right  # 队列[[长度(队列) 加 1L]] 小于 减 节点$右边界
            }
            i <- i + 1L  # 把 下标 i 加 1L 存入 下标 i
        }
    }
    root  # 根节点
}
# 层序转列表（用于断言输出） 定义函数 tree_to_levels（参数：根节点）
tree_to_levels <- function(root) {
    if (is.null(root))
        return(list())  # 若 is.null(根节点)) return(列表(
    res <- list()  # 把 列表() 存入 结果
    level <- list(root)  # 把 列表(根节点) 存入 level
    while (length(level) > 0) {
        # 循环，直到不满足「长度(level) 超过 0」
        vals <- list()
        nxt <- list()  # 把 列表(); nxt 小于 减 列表() 存入 vals
        for (nd in level) {
            # for (nd in level) {
            vals[[length(vals) + 1L]] <- nd$val  # vals[[长度(vals) 加 1L]] 小于 减 nd$值
            if (!is.null(nd$left))
                nxt[[length(nxt) + 1L]] <- nd$left  # 若 取反 is.null(nd$左边界)) nxt[[长度(nxt) 加 1L]] 小于 减 nd$左边界
            if (!is.null(nd$right))
                nxt[[length(nxt) + 1L]] <- nd$right  # 若 取反 is.null(nd$右边界)) nxt[[长度(nxt) 加 1L]] 小于 减 nd$右边界
        }
        res[[length(res) + 1L]] <- unlist(vals)  # 结果[[长度(结果) 加 1L]] 小于 减 unlist(vals)
        level <- nxt  # 把 nxt 存入 level
    }
    res  # 结果
}
lca_fn <- function(n, p, q, found) {
    # 定义函数 lca_fn（参数：元素个数, 节点, 节点, found）
    if (is.null(n))
        return(-1L)  # 若 is.null(元素个数)) return( 减 1L
    if (n$val == p || n$val == q) {
        # 若 元素个数$值 等于 节点 或 元素个数$值 等于 节点
        found$cnt <- found$cnt + 1L  # 把 found$计数 加 1L 存入 found$cnt
        return(n$val)  # 返回 元素个数$值
    }
    before <- found$cnt  # 把 found$计数 存入 before
    l <- lca_fn(n$left, p, q, found)  # 把 lca_fn(元素个数$左边界, 节点, 节点, found) 存入 左指针
    r <- lca_fn(n$right, p, q, found)  # 把 lca_fn(元素个数$右边界, 节点, 节点, found) 存入 右指针
    if (l != -1L && r != -1L)
        return(n$val)  # 若 左指针 不等于 减 1L 且 右指针 不等于 减 1L) return(元素个数$值
    if (found$cnt > before)
        return(if (l != -1L) l else r)  # 若 found$计数 超过 before) return(if (左指针 不等于 减 1L) 左指针 else 右指针
    -1L  # 减 1L
}
lowest_common_ancestor <- function(root, p, q) {
    # 定义函数 lowest_common_ancestor（参数：根节点, 节点, 节点）
    found <- new.env(parent = emptyenv())
    found$cnt <- 0L  # 把 new.env(parent 赋值为 emptyenv()); found$计数 小于 减 0L 存入 found
    lca_fn(root, p, q, found)  # lca_fn(根节点, 节点, 节点, found)
}
t <- build_tree(list(3L, 5L, 1L, 6L, 2L, 0L, 8L, NA, NA, 7L, 4L))
stopifnot(lowest_common_ancestor(t, 5L, 1L) == 3L)  # 断言校验
stopifnot(lowest_common_ancestor(t, 5L, 4L) == 5L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
