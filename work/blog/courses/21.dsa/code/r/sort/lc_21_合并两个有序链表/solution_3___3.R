# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133594090 LeetCode 21. 合并两个有序链表 — R
# 版（方案3） 定义函数 build_list（参数：vals）
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
merge_two_lists <- function(list1, list2) {
    # 定义函数 merge_two_lists（参数：list1, list2）
    dummy <- new.env(parent = emptyenv())
    dummy$val <- 0L
    dummy$nxt <- NULL
    p <- dummy  # 把 哨兵节点 存入 节点
    p1 <- list1
    p2 <- list2  # 把 list1; p2 小于 减 list2 存入 p1
    while (!is.null(p1) && !is.null(p2)) {
        # 循环，直到不满足「取反 is.null(p1) 且 取反 is.null(p2」
        if (p1$val < p2$val) {
            p$nxt <- p1
            p1 <- p1$nxt
        } else {
            p$nxt <- p2
            p2 <- p2$nxt
        }
        p <- p$nxt  # 把 节点$nxt 存入 节点
    }
    p$nxt <- if (!is.null(p1))
        p1 else p2  # 把 if (取反 is.null(p1)) p1 else p2 存入 p$nxt
    dummy$nxt  # 哨兵节点$nxt
}
a <- list_to_vec(merge_two_lists(build_list(c(1L, 2L, 4L)), build_list(c(1L, 3L, 4L))))
stopifnot(identical(a, c(1L, 1L, 2L, 3L, 4L, 4L)))  # 断言校验
stopifnot(is.null(merge_two_lists(NULL, NULL)))  # 断言校验
c3 <- list_to_vec(merge_two_lists(NULL, build_list(0L)))  # 把 list_to_vec(merge_two_lists(NULL, build_list(0L))) 存入 c3
stopifnot(identical(c3, 0L))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
