# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134283831 LeetCode 23. 合并K个升序链表 — R
# 版（方案7） 定义函数 build_list（参数：vals）
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
merge_two <- function(a, b) {
    # 定义函数 merge_two（参数：数组, b）
    dummy <- new.env(parent = emptyenv())
    dummy$val <- 0L
    dummy$nxt <- NULL
    cur <- dummy  # 把 哨兵节点 存入 当前值
    while (!is.null(a) && !is.null(b)) {
        # 循环，直到不满足「取反 is.null(数组) 且 取反 is.null(b」
        if (a$val <= b$val) {
            cur$nxt <- a
            a <- a$nxt
        } else {
            cur$nxt <- b
            b <- b$nxt
        }
        cur <- cur$nxt  # 把 当前值$nxt 存入 当前值
    }
    cur$nxt <- if (!is.null(a))
        a else b  # 把 if (取反 is.null(数组)) 数组 else b 存入 cur$nxt
    dummy$nxt  # 哨兵节点$nxt
}
merge_k_lists <- function(lists) {
    # 定义函数 merge_k_lists（参数：lists）
    acc <- NULL  # 把 NULL 存入 累加器
    for (l in lists) acc <- merge_two(acc, l)  # for (左指针 in lists) 累加器 小于 减 merge_two(累加器, 左指针)
    acc  # 累加器
}
got <- list_to_vec(merge_k_lists(list(build_list(c(1L, 4L, 5L)), build_list(c(1L, 3L, 4L)), build_list(c(2L, 6L)))))
stopifnot(identical(got, c(1L, 1L, 2L, 3L, 4L, 4L, 5L, 6L)))  # 断言校验
stopifnot(is.null(merge_k_lists(list())))  # 断言校验
stopifnot(is.null(merge_k_lists(list(build_list(integer(0))))))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
