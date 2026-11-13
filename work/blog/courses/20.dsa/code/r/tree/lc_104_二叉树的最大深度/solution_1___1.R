# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631 LeetCode 104. 二叉树的最大深度 — R
# 版 注意：R 的 list 是值语义（copy-on-modify），树/链表节点必须用 environment 引用语义
TreeNode <- function(val, left = NULL, right = NULL) {
    # 定义函数 TreeNode（参数：值, 左边界 赋值为 NULL, 右边界 赋值为 NULL）
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$val <- val
    e$left <- left
    e$right <- right  # 把 值; e$左边界 小于 减 左边界; e$右边界 小于 减 右边界 存入 e$val
    class(e) <- "TreeNode"  # 把 「TreeNode」 存入 class(e)
    e
}
# 层序数组构建二叉树，NA 表示空节点 定义函数 build_tree（参数：vals）
build_tree <- function(vals) {
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
                node$left <- TreeNode(vals[[i]])  # environment 原地修改，生效！
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
# 主解法：DFS，叶子节点时刷新最大深度（与 blog 方案1一致） 定义函数 max_depth（参数：根节点）
max_depth <- function(root) {
    dep <- 0L  # 把 0L 存入 dep
    dfs <- function(n, l) {
        # 定义函数 dfs（参数：元素个数, 左指针）
        if (is.null(n))
            return(invisible(NULL))  # 若 is.null(元素个数)) return(invisible(NULL
        if (is.null(n$left) && is.null(n$right)) {
            # 若 is.null(元素个数$左边界) 且 is.null(元素个数$右边界
            dep <<- max(dep, l)  # dep 小于 小于 减 取较大值 dep, 左指针)
        }
        dfs(n$left, l + 1L)  # dfs(元素个数$左边界, 左指针 加 1L)
        dfs(n$right, l + 1L)  # dfs(元素个数$右边界, 左指针 加 1L)
    }
    dfs(root, 1L)  # dfs(根节点, 1L)
    dep  # dep
}
# 自测：与 LeetCode 官方用例一致
tests <- list(list(list(), 0L), list(list(1L), 1L), list(list(3L, 9L, 20L, NA, NA, 15L, 7L), 3L), list(list(1L,
    NA, 2L, NA, 3L), 3L)  # 列表(列表(1L, NA, 2L, NA, 3L), 3L)
)
for (idx in seq_along(tests)) {
    # for (idx in seq_along(tests)) {
    got <- max_depth(build_tree(tests[[idx]][[1]]))  # 把 max_depth(build_tree(tests[[idx]][[1]])) 存入 got
    want <- tests[[idx]][[2]]  # 把 tests[[idx]][[2]] 存入 want
    stopifnot(got == want)  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
