# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133785568 LeetCode 206. 反转链表 — R
# 版（方案5）
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
reverse_list <- function(head) {
    # 定义函数 reverse_list（参数：头节点）
    prev <- NULL
    cur <- head  # 把 NULL; 当前值 小于 减 头节点 存入 前一个
    while (!is.null(cur)) {
        # 循环，直到不满足「取反 is.null(当前值」
        nxt <- cur$nxt  # 把 当前值$nxt 存入 nxt
        cur$nxt <- prev  # 把 前一个 存入 cur$nxt
        prev <- cur  # 把 当前值 存入 前一个
        cur <- nxt  # 把 nxt 存入 当前值
    }
    prev  # 前一个
}
stopifnot(identical(to_vec(reverse_list(build_list(1:5))), 5:1))  # 断言校验
stopifnot(length(to_vec(reverse_list(build_list(integer(0))))) == 0)  # 断言校验
stopifnot(identical(to_vec(reverse_list(build_list(1L))), 1L))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
