# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133874671 LeetCode 142. 环形链表II — R
# 版（方案2）
ListNode <- function(val, nxt = NULL) {
    e <- new.env(parent = emptyenv())
    e$val <- val
    e$nxt <- nxt
    class(e) <- "ListNode"
    e
}  # 定义函数 ListNode（参数：值, nxt 赋值为 NULL）
build_with_cycle <- function(vals, pos) {
    # 定义函数 build_with_cycle（参数：vals, pos）
    head <- NULL
    cur <- NULL
    tail_at <- NULL  # 把 NULL; 当前值 小于 减 NULL; tail_at 小于 减 NULL 存入 头节点
    for (i in seq_along(vals)) {
        # for (下标 i in seq_along(vals)) {
        n <- ListNode(vals[i])  # 把 ListNode(vals[下标 i]) 存入 元素个数
        if (is.null(head)) {
            head <- n
            cur <- n
        } else {
            cur$nxt <- n
            cur <- n
        }
        if (i == pos)
            tail_at <- n  # 若 下标 i 等于 pos) tail_at 小于 减 元素个数
    }
    if (!is.null(tail_at))
        cur$nxt <- tail_at  # 若 取反 is.null(tail_at)) 当前值$nxt 小于 减 tail_at
    head  # 头节点
}
detect_cycle <- function(head) {
    # 定义函数 detect_cycle（参数：头节点）
    slow <- head
    fast <- head  # 把 头节点; 快指针 小于 减 头节点 存入 慢指针
    while (!is.null(fast) && !is.null(fast$nxt)) {
        # 循环，直到不满足「取反 is.null(快指针) 且 取反 is.null(快指针$nxt」
        slow <- slow$nxt  # 把 慢指针$nxt 存入 慢指针
        fast <- fast$nxt$nxt  # 把 快指针$nxt$nxt 存入 快指针
        if (!is.null(slow) && identical(slow, fast)) {
            # 若 取反 is.null(慢指针) 且 identical(慢指针, 快指针
            p1 <- head
            p2 <- slow  # 把 头节点; p2 小于 减 慢指针 存入 p1
            while (!identical(p1, p2)) {
                p1 <- p1$nxt
                p2 <- p2$nxt
            }
            return(p1)  # 返回 p1
        }
    }
    NULL  # NULL
}
h <- build_with_cycle(c(3, 2, 0, -4), 2)  # 把 build_with_cycle(字符(3, 2, 0, 减 4), 2) 存入 h
stopifnot(!is.null(detect_cycle(h)), detect_cycle(h)$val == 2)  # 断言校验
stopifnot(is.null(detect_cycle(ListNode(1))))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
