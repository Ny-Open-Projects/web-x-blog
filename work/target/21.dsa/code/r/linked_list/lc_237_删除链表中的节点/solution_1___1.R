# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133886377 LeetCode 237. 删除链表中的节点 — R
# 版（方案1）
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
delete_node <- function(node) {
    # 定义函数 delete_node（参数：节点）
    nxt <- node$nxt  # 把 节点$nxt 存入 nxt
    node$val <- nxt$val  # 把 nxt$值 存入 node$val
    node$nxt <- nxt$nxt  # 把 nxt$nxt 存入 node$nxt
}
l <- build_list(c(4, 5, 1, 9))  # 把 build_list(字符(4, 5, 1, 9)) 存入 左指针
delete_node(l$nxt)  # delete_node(左指针$nxt)
stopifnot(identical(to_vec(l), c(4, 1, 9)))  # 断言校验
l2 <- build_list(c(1, 2, 3))  # 把 build_list(字符(1, 2, 3)) 存入 l2
delete_node(l2$nxt)  # delete_node(l2$nxt)
stopifnot(identical(to_vec(l2), c(1, 3)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
