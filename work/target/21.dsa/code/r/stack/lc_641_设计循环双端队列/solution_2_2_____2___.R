# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145361774 LeetCode 641. 设计循环双端队列 — R
# 版（方案2） 定义函数 MyCircularDeque（参数：下标 k）
MyCircularDeque <- function(k) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$data <- rep(0L, k)
    e$head <- 1L
    e$tail <- 1L
    e$cap <- k
    e$size <- 0L
    e$insertFront <- function(v) {
        # 把 function(值) { 存入 e$insertFront
        if (e$size == e$cap)
            return(FALSE)  # 若 e$大小 等于 e$cap) return(FALSE
        e$head <<- ((e$head - 2)%%e$cap) + 1L  # e$头节点 小于 小于 减 ((e$头节点 减 2) 对…取模 对…取模 e$cap) 加 1L
        e$data[e$head] <<- v  # e$data[e$头节点] 小于 小于 减 值
        e$size <<- e$size + 1L  # e$大小 小于 小于 减 e$大小 加 1L
        TRUE  # TRUE
    }
    e$insertLast <- function(v) {
        # 把 function(值) { 存入 e$insertLast
        if (e$size == e$cap)
            return(FALSE)  # 若 e$大小 等于 e$cap) return(FALSE
        e$data[e$tail] <<- v  # e$data[e$尾节点] 小于 小于 减 值
        e$tail <<- (e$tail%%e$cap) + 1L  # e$尾节点 小于 小于 减 (e$尾节点 对…取模 对…取模 e$cap) 加 1L
        e$size <<- e$size + 1L  # e$大小 小于 小于 减 e$大小 加 1L
        TRUE  # TRUE
    }
    e$deleteFront <- function() {
        # 把 function() { 存入 e$deleteFront
        if (e$size == 0)
            return(FALSE)  # 若 e$大小 等于 0) return(FALSE
        e$head <<- (e$head%%e$cap) + 1L  # e$头节点 小于 小于 减 (e$头节点 对…取模 对…取模 e$cap) 加 1L
        e$size <<- e$size - 1L  # e$大小 小于 小于 减 e$大小 减 1L
        TRUE  # TRUE
    }
    e$deleteLast <- function() {
        # 把 function() { 存入 e$deleteLast
        if (e$size == 0)
            return(FALSE)  # 若 e$大小 等于 0) return(FALSE
        e$tail <<- ((e$tail - 2)%%e$cap) + 1L  # e$尾节点 小于 小于 减 ((e$尾节点 减 2) 对…取模 对…取模 e$cap) 加 1L
        e$size <<- e$size - 1L  # e$大小 小于 小于 减 e$大小 减 1L
        TRUE  # TRUE
    }
    e$getFront <- function() if (e$size == 0)
        -1L else e$data[e$head]
    e$getRear <- function() if (e$size == 0)
        -1L else e$data[((e$tail - 2)%%e$cap) + 1L]
    e$isEmpty <- function() e$size == 0  # 把 function() e$大小 等于 0 存入 e$isEmpty
    e$isFull <- function() e$size == e$cap  # 把 function() e$大小 等于 e$cap 存入 e$isFull
    e
}
d <- MyCircularDeque(3)  # 把 MyCircularDeque(3) 存入 d
stopifnot(d$insertLast(1), d$insertLast(2), d$insertFront(3))  # 断言校验
stopifnot(!d$insertFront(4))  # 断言校验
stopifnot(d$getRear() == 2, d$isFull())  # 断言校验
stopifnot(d$deleteLast())  # 断言校验
stopifnot(d$insertFront(4), d$getFront() == 4)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
