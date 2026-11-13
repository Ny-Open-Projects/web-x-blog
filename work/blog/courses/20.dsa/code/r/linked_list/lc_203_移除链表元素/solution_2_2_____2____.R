# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133813394 LeetCode 203. 移除链表元素 — R
# 版（方案2）
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
remove_elements <- function(head, val) {
    # 定义函数 remove_elements（参数：头节点, 值）
    dummy <- ListNode(0, head)  # 把 ListNode(0, 头节点) 存入 哨兵节点
    cur <- dummy  # 把 哨兵节点 存入 当前值
    while (!is.null(cur$nxt)) {
        # 循环，直到不满足「取反 is.null(当前值$nxt」 若 当前值$nxt$值 等于 值
        if (cur$nxt$val == val) {
            cur$nxt <- cur$nxt$nxt  # 把 当前值$nxt$nxt 存入 cur$nxt
        } else {
            # 否则
            cur <- cur$nxt  # 把 当前值$nxt 存入 当前值
        }
    }
    dummy$nxt  # 哨兵节点$nxt
}
stopifnot(identical(to_vec(remove_elements(build_list(1:6), 6)), 1:5))  # 断言校验
stopifnot(is.null(remove_elements(build_list(rep(7, 4)), 7)))  # 断言校验
stopifnot(identical(to_vec(remove_elements(build_list(c(1, 2, 2, 1)), 2)), c(1, 1)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
