# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134283831 LeetCode 23. 合并K个升序链表 — R
# 版（方案6） 定义函数 build_list（参数：vals）
build_list <- function(vals) {
    if (length(vals) == 0)
        return(NULL)  # 若 长度(vals) 等于 0) return(NULL
    head <- NULL
    cur <- NULL  # 把 NULL; 当前值 小于 减 NULL 存入 头节点
    for (v in vals) {
        # for (值 in vals) {
        n <- new.env(parent = emptyenv())
        n$val <- v
        n$nxt <- NULL
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
list_to_vec <- function(head) {
    # 定义函数 list_to_vec（参数：头节点）
    out <- integer(0)  # 把 integer(0) 存入 out
    while (!is.null(head)) {
        out[[length(out) + 1L]] <- head$val
        head <- head$nxt
    }
    out  # out
}
merge_k_lists <- function(lists) {
    # 定义函数 merge_k_lists（参数：lists）
    ptrs <- lists  # 把 lists 存入 ptrs
    dummy <- new.env(parent = emptyenv())
    dummy$val <- 0L
    dummy$nxt <- NULL
    tail <- dummy  # 把 哨兵节点 存入 尾节点
    repeat {
        # repeat {
        best_i <- 0L  # 把 0L 存入 best_i
        for (i in seq_along(ptrs)) {
            # for (下标 i in seq_along(ptrs)) {
            if (!is.null(ptrs[[i]]) && (best_i == 0L || ptrs[[i]]$val < ptrs[[best_i]]$val))
                best_i <- i
        }
        if (best_i == 0L)
            break  # 若 best_i 等于 0L) break
        tail$nxt <- ptrs[[best_i]]  # 把 ptrs[[best_i]] 存入 tail$nxt
        ptrs[[best_i]] <- ptrs[[best_i]]$nxt  # 把 ptrs[[best_i]]$nxt 存入 ptrs[[best_i]]
        tail <- tail$nxt  # 把 尾节点$nxt 存入 尾节点
    }
    dummy$nxt  # 哨兵节点$nxt
}
got <- list_to_vec(merge_k_lists(list(build_list(c(1L, 4L, 5L)), build_list(c(1L, 3L, 4L)), build_list(c(2L, 6L)))))
stopifnot(identical(got, c(1L, 1L, 2L, 3L, 4L, 4L, 5L, 6L)))  # 断言校验
stopifnot(is.null(merge_k_lists(list())))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
