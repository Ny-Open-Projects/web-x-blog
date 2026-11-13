# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134859971 LeetCode 2050. 并行课程III — R
# 版（方案2） 定义函数 minimum_time_courses（参数：元素个数, relations, time）
minimum_time_courses <- function(n, relations, time) {
    next_ <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 next_
    indeg <- rep(0L, n + 1)  # 把 rep(0L, 元素个数 加 1) 存入 indeg
    for (r in seq_len(nrow(relations))) {
        # for (右指针 in seq_len(nrow(relations))) {
        u <- relations[r, 1]
        v <- relations[r, 2]  # 把 relations[右指针, 1]; 值 小于 减 relations[右指针, 2] 存入 节点 u
        key <- as.character(u)  # 把 as.character(节点 u) 存入 key
        lst <- if (!is.null(next_[[key]]))
            next_[[key]] else integer(0)
        next_[[key]] <- c(lst, v)  # 把 字符(lst, 值) 存入 next_[[key]]
        indeg[v + 1] <- indeg[v + 1] + 1L  # indeg[值 加 1] 小于 减 indeg[值 加 1] 加 1L
    }
    finish <- rep(0L, n + 1)  # 把 rep(0L, 元素个数 加 1) 存入 finish
    queue <- integer(0)  # 把 integer(0) 存入 队列
    for (c in 1:n) if (indeg[c + 1] == 0L)
        queue <- c(queue, c)
    total <- 0L  # 把 0L 存入 总和
    while (length(queue) > 0) {
        # 循环，直到不满足「长度(队列) 超过 0」
        nq <- integer(0)  # 把 integer(0) 存入 nq
        for (c in queue) {
            # for (字符 in 队列) {
            finish[c + 1] <- finish[c + 1] + time[c]  # finish[字符 加 1] 小于 减 finish[字符 加 1] 加 time[字符]
            if (finish[c + 1] > total)
                total <- finish[c + 1]  # 若 finish[字符 加 1] 超过 总和) 总和 小于 减 finish[字符 加 1]
            key <- as.character(c)  # 把 as.character(字符) 存入 key
            for (nx in (if (!is.null(next_[[key]]))
                next_[[key]] else integer(0))) {
                if (finish[nx + 1] < finish[c + 1])
                  finish[nx + 1] <- finish[c + 1]
                indeg[nx + 1] <- indeg[nx + 1] - 1L  # indeg[nx 加 1] 小于 减 indeg[nx 加 1] 减 1L
                if (indeg[nx + 1] == 0L)
                  nq <- c(nq, nx)  # 若 indeg[nx 加 1] 等于 0L) nq 小于 减 字符(nq, nx
            }
        }
        queue <- nq  # 把 nq 存入 队列
    }
    total  # 总和
}
r1 <- matrix(c(1, 3, 2, 3), ncol = 2, byrow = TRUE)  # 把 矩阵(字符(1,3, 2,3), ncol 赋值为 2, byrow 赋值为 TRUE) 存入 r1
stopifnot(minimum_time_courses(3, r1, c(3, 2, 5)) == 8)  # 断言校验
r2 <- matrix(c(1, 2, 2, 3, 3, 4, 4, 5), ncol = 2, byrow = TRUE)
stopifnot(minimum_time_courses(5, r2, c(1, 2, 3, 4, 5)) == 15)  # 断言校验
stopifnot(minimum_time_courses(1, matrix(integer(0), ncol = 2), c(5)) == 5)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
