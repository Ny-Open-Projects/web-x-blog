# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133746567 LeetCode 19.
# 删除链表的倒数第N个结点 — R 版（方案3）
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
to_vec <- function(h) {
    out <- integer(0)
    while (!is.null(h)) {
        out <- c(out, h$val)
        h <- h$nxt
    }
    out
}  # 定义函数 to_vec（参数：h）
remove_nth_from_end <- function(head, n) {
    # 定义函数 remove_nth_from_end（参数：头节点, 元素个数）
    vals <- to_vec(head)  # 把 to_vec(头节点) 存入 vals
    idx <- length(vals) - n + 1  # 把 长度(vals) 减 元素个数 加 1 存入 idx
    if (idx >= 1)
        vals <- vals[-idx]  # 若 idx 不低于 1) vals 小于 减 vals[ 减 idx]
    out <- NULL
    cur <- NULL  # 把 NULL; 当前值 小于 减 NULL 存入 out
    for (v in vals) {
        # for (值 in vals) {
        nd <- ListNode(v)  # 把 ListNode(值) 存入 nd
        if (is.null(out)) {
            out <- nd
            cur <- nd
        } else {
            cur$nxt <- nd
            cur <- nd
        }
    }
    out  # out
}
stopifnot(identical(to_vec(remove_nth_from_end(build_list(1:5), 2)), c(1L, 2L, 3L, 5L)))  # 断言校验
stopifnot(length(to_vec(remove_nth_from_end(build_list(1L), 1L))) == 0)  # 断言校验
stopifnot(identical(to_vec(remove_nth_from_end(build_list(c(1L, 2L)), 2L)), 2L))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
