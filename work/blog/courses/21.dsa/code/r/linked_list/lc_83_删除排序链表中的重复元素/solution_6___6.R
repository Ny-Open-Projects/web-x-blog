# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133874590 LeetCode 83.
# 删除排序链表中的重复元素 — R 版（方案6）
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
delete_duplicates <- function(head) {
    # 定义函数 delete_duplicates（参数：头节点）
    if (is.null(head))
        return(NULL)  # 若 is.null(头节点)) return(NULL
    vals <- to_vec(head)  # 把 to_vec(头节点) 存入 vals
    vals <- vals[c(TRUE, vals[-1] != vals[-length(vals)])]  # 把 vals[字符(TRUE, vals[ 减 1] 不等于 vals[ 减 长度(vals)])] 存入 vals
    out <- NULL
    cur <- NULL  # 把 NULL; 当前值 小于 减 NULL 存入 out
    for (v in vals) {
        # for (值 in vals) {
        n <- ListNode(v)  # 把 ListNode(值) 存入 元素个数
        if (is.null(out)) {
            out <- n
            cur <- n
        } else {
            cur$nxt <- n
            cur <- n
        }
    }
    out  # out
}
stopifnot(identical(to_vec(delete_duplicates(build_list(c(1, 1, 2)))), c(1, 2)))  # 断言校验
stopifnot(identical(to_vec(delete_duplicates(build_list(c(1, 1, 2, 3, 3)))), c(1, 2, 3)))  # 断言校验
stopifnot(identical(to_vec(delete_duplicates(build_list(c(1, 1, 1)))), 1))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
