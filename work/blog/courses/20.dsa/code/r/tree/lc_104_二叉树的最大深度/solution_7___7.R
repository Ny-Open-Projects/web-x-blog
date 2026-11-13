# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631 LeetCode 104. 二叉树的最大深度 — R
# 版（方案7：分治递归 + 树遍历辅助（中序/自底向上层序/根叶路径/层均值）） harness：层序数组建树，NA
# 表示空节点；节点用 environment 引用语义
TreeNode <- function(val, left = NULL, right = NULL) {
    # 定义函数 TreeNode（参数：值, 左边界 赋值为 NULL, 右边界 赋值为 NULL）
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
# 辅助：中序遍历 定义函数 inorder（参数：根节点, out 赋值为 字符(）
inorder <- function(root, out = c()) {
    if (is.null(root))
        return(out)  # 若 is.null(根节点)) return(out
    out <- inorder(root$left, out)  # 把 inorder(根节点$左边界, out) 存入 out
    out <- c(out, root$val)  # 把 字符(out, 根节点$值) 存入 out
    inorder(root$right, out)  # inorder(根节点$右边界, out)
}
# 辅助：自底向上层序遍历 定义函数 level_order_bottom（参数：根节点）
level_order_bottom <- function(root) {
    res <- list()  # 把 列表() 存入 结果
    queue <- if (is.null(root))
        list() else list(root)  # 把 if (is.null(根节点)) 列表() else 列表(根节点) 存入 队列
    while (length(queue) > 0) {
        # 循环，直到不满足「长度(队列) 超过 0」
        vals <- c()  # 把 字符() 存入 vals
        nxt <- list()  # 把 列表() 存入 nxt
        for (node in queue) {
            # for (节点 in 队列) {
            vals <- c(vals, node$val)  # 把 字符(vals, 节点$值) 存入 vals
            if (!is.null(node$left))
                nxt[[length(nxt) + 1L]] <- node$left  # 若 取反 is.null(节点$左边界)) nxt[[长度(nxt) 加 1L]] 小于 减 节点$左边界
            if (!is.null(node$right))
                nxt[[length(nxt) + 1L]] <- node$right  # 若 取反 is.null(节点$右边界)) nxt[[长度(nxt) 加 1L]] 小于 减 节点$右边界
        }
        res <- c(list(vals), res)  # 把 字符(列表(vals), 结果) 存入 结果
        queue <- nxt  # 把 nxt 存入 队列
    }
    res  # 结果
}
# 辅助：所有根到叶路径 定义函数 binary_tree_paths（参数：根节点）
binary_tree_paths <- function(root) {
    out <- character(0)  # 把 character(0) 存入 out
    dfs <- function(n, path) {
        # 定义函数 dfs（参数：元素个数, 当前路径）
        if (is.null(n))
            return(invisible(NULL))  # 若 is.null(元素个数)) return(invisible(NULL
        path <- paste0(path, as.character(n$val))  # 把 paste0(当前路径, as.character(元素个数$值)) 存入 当前路径
        if (is.null(n$left) && is.null(n$right)) {
            # 若 is.null(元素个数$左边界) 且 is.null(元素个数$右边界
            out <<- c(out, path)  # out 小于 小于 减 字符(out, 当前路径)
            return(invisible(NULL))  # 返回 invisible(NULL
        }
        path <- paste0(path, "->")  # 把 paste0(当前路径, 「 减 超过 」) 存入 当前路径
        dfs(n$left, path)  # dfs(元素个数$左边界, 当前路径)
        dfs(n$right, path)  # dfs(元素个数$右边界, 当前路径)
    }
    dfs(root, "")  # dfs(根节点, 「」)
    out  # out
}
# 辅助：每层节点均值 定义函数 average_of_levels（参数：根节点）
average_of_levels <- function(root) {
    result <- c()  # 把 字符() 存入 结果
    queue <- if (is.null(root))
        list() else list(root)  # 把 if (is.null(根节点)) 列表() else 列表(根节点) 存入 队列
    while (length(queue) > 0) {
        # 循环，直到不满足「长度(队列) 超过 0」
        total <- 0  # 把 0 存入 总和
        nxt <- list()  # 把 列表() 存入 nxt
        for (node in queue) {
            # for (节点 in 队列) {
            total <- total + node$val  # 把 总和 加 节点$值 存入 总和
            if (!is.null(node$left))
                nxt[[length(nxt) + 1L]] <- node$left  # 若 取反 is.null(节点$左边界)) nxt[[长度(nxt) 加 1L]] 小于 减 节点$左边界
            if (!is.null(node$right))
                nxt[[length(nxt) + 1L]] <- node$right  # 若 取反 is.null(节点$右边界)) nxt[[长度(nxt) 加 1L]] 小于 减 节点$右边界
        }
        result <- c(result, total/length(queue))  # 把 字符(结果, 总和 除以 长度(队列)) 存入 结果
        queue <- nxt  # 把 nxt 存入 队列
    }
    result  # 结果
}
# 主解法：分治递归，深度 = 1 + max(左子树深度, 右子树深度) 定义函数 max_depth（参数：根节点）
max_depth <- function(root) {
    if (is.null(root))
        return(0L)  # 若 is.null(根节点)) return(0L
    l <- max_depth(root$left)  # 把 max_depth(根节点$左边界) 存入 左指针
    r <- max_depth(root$right)  # 把 max_depth(根节点$右边界) 存入 右指针
    1L + max(l, r)  # 1L 加 取较大值 左指针, 右指针)
}
# 自测：与 blog 方案用例一致
tests <- list(list(list(3L, 9L, 20L, NA, NA, 15L, 7L), 3L), list(list(1L, 2L, 3L, 4L, 5L), 3L)  # 列表(列表(1L, 2L, 3L, 4L, 5L), 3L)
)
for (idx in seq_along(tests)) {
    # for (idx in seq_along(tests)) {
    got <- max_depth(build_tree(tests[[idx]][[1]]))  # 把 max_depth(build_tree(tests[[idx]][[1]])) 存入 got
    want <- tests[[idx]][[2]]  # 把 tests[[idx]][[2]] 存入 want
    stopifnot(got == want)  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
