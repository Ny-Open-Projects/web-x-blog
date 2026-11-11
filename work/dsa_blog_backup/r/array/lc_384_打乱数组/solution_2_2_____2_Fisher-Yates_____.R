# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134350547 LeetCode 384. 打乱数组 — R
# 版（方案2） 定义函数 ShuffleArray（参数：vals）
ShuffleArray <- function(vals) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$orig <- vals
    e$cur <- vals  # 把 vals; e$当前值 小于 减 vals 存入 e$orig
    e$reset <- function() {
        e$cur <<- e$orig
        e$cur
    }  # 把 function() { e$当前值 小于 小于 减 e$orig; e$当前值 } 存入 e$reset
    e$shuffle <- function() {
        # 把 function() { 存入 e$shuffle
        n <- length(e$cur)  # 把 长度(e$当前值) 存入 元素个数
        for (i in n:2) {
            # for (下标 i in 元素个数:2) {
            j <- sample(i, 1L)  # 把 sample(下标 i, 1L) 存入 下标 j
            t <- e$cur[i]
            e$cur[i] <- e$cur[j]
            e$cur[j] <- t
        }
        e$cur  # e$当前值
    }
    e
}
set.seed(42)  # set.seed(42)
sa <- ShuffleArray(c(1L, 2L, 3L))  # 把 ShuffleArray(字符(1L, 2L, 3L)) 存入 sa
sh <- sa$shuffle()  # 把 sa$shuffle() 存入 sh
stopifnot(identical(sort(sh), c(1L, 2L, 3L)))  # 断言校验
r <- sa$reset()  # 把 sa$reset() 存入 右指针
stopifnot(identical(r, c(1L, 2L, 3L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
