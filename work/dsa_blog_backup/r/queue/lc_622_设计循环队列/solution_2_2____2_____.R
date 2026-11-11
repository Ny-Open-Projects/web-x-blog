# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130471048 LeetCode 622. 设计循环队列 — R 版
# 方案2：数组 + front/rear/size 循环队列 ⚠️ R 必须用 environment 引用语义模拟对象（list 是值语义） ⚠️ R 下标 1
# 基，取模规则相应换算：rear = rear %% cap + 1 定义函数 MyCircularQueue（参数：下标 k）
MyCircularQueue <- function(k) {
    env <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 env
    env$capacity <- k  # 把 下标 k 存入 env$capacity
    env$data <- rep(0L, k)  # 把 rep(0L, 下标 k) 存入 env$data
    env$front <- 1L  # 把 1L 存入 env$front
    env$rear <- 1L  # 把 1L 存入 env$rear
    env$size <- 0L  # 把 0L 存入 env$size
    env$enQueue <- function(value) {
        # 把 function(value) { 存入 env$enQueue
        if (env$isFull())
            return(FALSE)  # 若 env$isFull()) return(FALSE
        env$data[env$rear] <- value  # 把 value 存入 env$data[env$rear]
        env$rear <- env$rear%%env$capacity + 1L  # 把 env$rear 对…取模 对…取模 env$capacity 加 1L 存入 env$rear
        env$size <- env$size + 1L  # 把 env$大小 加 1L 存入 env$size
        TRUE  # TRUE
    }
    env$deQueue <- function() {
        # 把 function() { 存入 env$deQueue
        if (env$isEmpty())
            return(FALSE)  # 若 env$isEmpty()) return(FALSE
        env$front <- env$front%%env$capacity + 1L  # 把 env$front 对…取模 对…取模 env$capacity 加 1L 存入 env$front
        env$size <- env$size - 1L  # 把 env$大小 减 1L 存入 env$size
        TRUE  # TRUE
    }
    env$Front <- function() {
        # 把 function() { 存入 env$Front
        if (env$isEmpty())
            return(-1L)  # 若 env$isEmpty()) return( 减 1L
        env$data[env$front]  # env$data[env$front]
    }
    env$Rear <- function() {
        # 把 function() { 存入 env$Rear
        if (env$isEmpty())
            return(-1L)  # 若 env$isEmpty()) return( 减 1L
        # TS 0 基 (rear-1+cap)%cap 的 1 基等价
        idx <- (env$rear - 2L)%%env$capacity + 1L  # 把 (env$rear 减 2L) 对…取模 对…取模 env$capacity 加 1L 存入 idx
        env$data[idx]  # env$data[idx]
    }
    env$isEmpty <- function() env$size == 0L  # 把 function() env$大小 等于 0L 存入 env$isEmpty
    env$isFull <- function() env$size == env$capacity  # 把 function() env$大小 等于 env$capacity 存入 env$isFull
    env  # env
}
# 自测：与 TS 事实源内嵌用例一致
q <- MyCircularQueue(3L)  # 把 MyCircularQueue(3L) 存入 节点
got <- list(q$enQueue(1L), q$enQueue(2L), q$enQueue(3L), q$enQueue(4L), q$Rear(), q$isFull(), q$deQueue(), q$enQueue(4L),
    q$Rear())
want <- list(TRUE, TRUE, TRUE, FALSE, 3L, TRUE, TRUE, TRUE, 4L)
stopifnot(length(got) == length(want))  # 断言校验
for (i in seq_along(want)) {
    # for (下标 i in seq_along(want)) {
    stopifnot(identical(got[[i]], want[[i]]))  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
