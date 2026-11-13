# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135637716 LeetCode 114. 二叉树展开为链表 — R
# 版（方案4） 树节点：R 必须 environment 引用语义（list 是值语义） 定义函数 TreeNode（参数：值, 左边界 赋值为
# NULL, 右边界 赋值为 NULL）
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
flatten <- function(root) {
    # 定义函数 flatten（参数：根节点）
    prev <- NULL  # 把 NULL 存入 前一个
    dfs <- function(node) {
        # 定义函数 dfs（参数：节点）
        if (is.null(node))
            return(invisible(NULL))  # 若 is.null(节点)) return(invisible(NULL
        dfs(node$right)  # dfs(节点$右边界)
        dfs(node$left)  # dfs(节点$左边界)
        node$right <- prev  # node 是 environment，<- 字段赋值即原地生效
        node$left <- NULL  # 把 NULL 存入 node$left
        prev <<- node  # 前一个 小于 小于 减 节点
    }
    dfs(root)  # dfs(根节点)
    root  # 根节点
}
chain <- function(root) {
    # 定义函数 chain（参数：根节点）
    out <- integer(0)  # 把 integer(0) 存入 out
    while (!is.null(root)) {
        # 循环，直到不满足「取反 is.null(根节点」
        stopifnot(is.null(root$left))  # 断言校验
        out[[length(out) + 1L]] <- root$val  # out[[长度(out) 加 1L]] 小于 减 根节点$值
        root <- root$right  # 把 根节点$右边界 存入 根节点
    }
    out  # out
}
stopifnot(identical(chain(flatten(build_tree(list(1L, 2L, 5L, 3L, 4L, NA, 6L)))), 1:6))  # 断言校验
stopifnot(identical(chain(flatten(build_tree(list(7L)))), 7L))  # 断言校验
stopifnot(is.null(flatten(NULL)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
