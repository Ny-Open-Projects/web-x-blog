# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133816714 LeetCode 141. 环形链表 — R
# 版（方案11）
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
has_cycle <- function(head) {
    # 定义函数 has_cycle（参数：头节点）
    slow <- head
    fast <- head  # 把 头节点; 快指针 小于 减 头节点 存入 慢指针
    while (!is.null(fast) && !is.null(fast$nxt)) {
        # 循环，直到不满足「取反 is.null(快指针) 且 取反 is.null(快指针$nxt」
        slow <- slow$nxt  # 把 慢指针$nxt 存入 慢指针
        fast <- fast$nxt$nxt  # 把 快指针$nxt$nxt 存入 快指针
        if (!is.null(slow) && identical(slow, fast))
            return(TRUE)  # 若 取反 is.null(慢指针) 且 identical(慢指针, 快指针)) return(TRUE
    }
    FALSE  # FALSE
}
stopifnot(!has_cycle(build_list(c(3, 2, 0, -4))))  # 断言校验
h <- build_list(c(1))  # 把 build_list(字符(1)) 存入 h
h$nxt <- h  # 把 h 存入 h$nxt
stopifnot(has_cycle(h))  # 断言校验
stopifnot(!has_cycle(NULL))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
