# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386298 LeetCode 117.
# 填充每个节点的下一个右侧节点指针 II — R 版（方案2） 树节点：R 必须 environment 引用语义（list 是值语义）
# 定义函数 TreeNode（参数：值, 左边界 赋值为 NULL, 右边界 赋值为 NULL）
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
NNode <- function(v) {
    e <- new.env(parent = emptyenv())
    e$val <- v
    e$left <- NULL
    e$right <- NULL
    e$nxt <- NULL
    class(e) <- "NNode"
    e
}  # 定义函数 NNode（参数：值）
build_ntree <- function(vals) {
    # 定义函数 build_ntree（参数：vals）
    if (length(vals) == 0L)
        return(NULL)  # 若 长度(vals) 等于 0L) return(NULL
    root <- NNode(vals[1L])  # 把 NNode(vals[1L]) 存入 根节点
    q <- list(root)
    head <- 1L
    i <- 2L  # 把 列表(根节点); 头节点 小于 减 1L; 下标 i 小于 减 2L 存入 节点
    while (head <= length(q) && i <= length(vals)) {
        # 循环，直到不满足「头节点 不超过 长度(节点) 且 下标 i 不超过 长度(vals」
        node <- q[[head]]
        head <- head + 1L  # 把 节点[[头节点]]; 头节点 小于 减 头节点 加 1L 存入 节点
        if (i <= length(vals)) {
            node$left <- NNode(vals[i])
            q[[length(q) + 1L]] <- node$left
            i <- i + 1L
        }
        if (i <= length(vals)) {
            node$right <- NNode(vals[i])
            q[[length(q) + 1L]] <- node$right
            i <- i + 1L
        }
    }
    root  # 根节点
}
connect <- function(root) {
    # 定义函数 connect（参数：根节点）
    if (is.null(root))
        return(NULL)  # 若 is.null(根节点)) return(NULL
    cur <- root  # 把 根节点 存入 当前值
    while (!is.null(cur)) {
        # 循环，直到不满足「取反 is.null(当前值」
        dummy <- NNode(0L)  # 把 NNode(0L) 存入 哨兵节点
        prev <- dummy  # 把 哨兵节点 存入 前一个
        node <- cur  # 把 当前值 存入 节点
        while (!is.null(node)) {
            # 循环，直到不满足「取反 is.null(节点」
            if (!is.null(node$left)) {
                prev$nxt <- node$left
                prev <- prev$nxt
            }
            if (!is.null(node$right)) {
                prev$nxt <- node$right
                prev <- prev$nxt
            }
            node <- node$nxt  # 把 节点$nxt 存入 节点
        }
        cur <- dummy$nxt  # 把 哨兵节点$nxt 存入 当前值
    }
    root  # 根节点
}
stopifnot(is.null(connect(NULL)))  # 断言校验
root <- connect(build_ntree(1:7))  # 把 connect(build_ntree(1:7)) 存入 根节点
levels <- list()  # 把 列表() 存入 levels
cur <- root  # 把 根节点 存入 当前值
while (!is.null(cur) && length(levels) < 5L) {
    # 循环，直到不满足「取反 is.null(当前值) 且 长度(levels) 小于 5L」
    vals <- integer(0)  # 把 integer(0) 存入 vals
    node <- cur  # 把 当前值 存入 节点
    while (!is.null(node)) {
        vals[[length(vals) + 1L]] <- node$val
        node <- node$nxt
    }
    levels[[length(levels) + 1L]] <- vals  # levels[[长度(levels) 加 1L]] 小于 减 vals
    cur <- if (!is.null(cur$left))
        cur$left else cur$right  # 把 if (取反 is.null(当前值$左边界)) 当前值$左边界 else 当前值$右边界 存入 当前值
}
stopifnot(identical(levels, list(1L, 2:3, 4:7)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
