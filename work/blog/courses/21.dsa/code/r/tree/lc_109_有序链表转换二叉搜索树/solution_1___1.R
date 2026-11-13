# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135270549 LeetCode 109.
# 有序链表转换二叉搜索树 — R 版（方案1） 树节点：R 必须 environment 引用语义（list 是值语义） 定义函数
# TreeNode（参数：值, 左边界 赋值为 NULL, 右边界 赋值为 NULL）
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
ListNode <- function(val, nxt = NULL) {
    e <- new.env(parent = emptyenv())
    e$val <- val
    e$nxt <- nxt
    class(e) <- "ListNode"
    e
}  # 定义函数 ListNode（参数：值, nxt 赋值为 NULL）
build_list <- function(vals) {
    # 定义函数 build_list（参数：vals）
    head <- NULL
    cur <- NULL  # 把 NULL; 当前值 小于 减 NULL 存入 头节点
    for (v in vals) {
        # for (值 in vals) {
        n <- ListNode(v)  # 把 ListNode(值) 存入 元素个数
        if (is.null(head)) {
            head <- n
            cur <- n
        } else {
            cur$nxt <- n
            cur <- n
        }
    }
    head  # 头节点
}
sorted_list_to_bst <- function(head) {
    # 定义函数 sorted_list_to_bst（参数：头节点）
    nodes <- integer(0)
    cur <- head  # 把 integer(0); 当前值 小于 减 头节点 存入 nodes
    while (!is.null(cur)) {
        nodes[[length(nodes) + 1L]] <- cur$val
        cur <- cur$nxt
    }
    if (length(nodes) == 0L)
        return(NULL)  # 若 长度(nodes) 等于 0L) return(NULL
    build <- function(left, right) {
        # 定义函数 build（参数：左边界, 右边界）
        if (left > right)
            return(NULL)  # 若 左边界 超过 右边界) return(NULL
        mid <- left + (right - left)%/%2L  # 把 左边界 加 (右边界 减 左边界) 对…取模 除以 对…取模 2L 存入 中点
        root <- TreeNode(nodes[mid])  # 把 TreeNode(nodes[中点]) 存入 根节点
        root$left <- build(left, mid - 1L)  # 把 build(左边界, 中点 减 1L) 存入 root$left
        root$right <- build(mid + 1L, right)  # 把 build(中点 加 1L, 右边界) 存入 root$right
        root  # 根节点
    }
    build(1L, length(nodes))  # build(1L, 长度(nodes))
}
inorder_fn <- function(n) {
    # 定义函数 inorder_fn（参数：元素个数）
    if (is.null(n))
        return(integer(0))  # 若 is.null(元素个数)) return(integer(0
    c(inorder_fn(n$left), n$val, inorder_fn(n$right))  # 字符(inorder_fn(元素个数$左边界), 元素个数$值, inorder_fn(元素个数$右边界))
}
stopifnot(is.null(sorted_list_to_bst(NULL)))  # 断言校验
t <- sorted_list_to_bst(build_list(c(1L, 2L, 3L)))  # 把 sorted_list_to_bst(build_list(字符(1L, 2L, 3L))) 存入 另一字符串
out <- inorder_fn(t)  # 把 inorder_fn(另一字符串) 存入 out
stopifnot(identical(out, c(1L, 2L, 3L)))  # 断言校验
stopifnot(t$val == 2L, t$left$val == 1L, t$right$val == 3L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
