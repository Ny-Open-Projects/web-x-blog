# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137295891 LeetCode 460. LFU缓存 — R
# 版（方案1） 定义函数 LfuSim（参数：cap）
LfuSim <- function(cap) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$cap <- cap
    e$vals <- list()
    e$freq <- list()
    e$stamp <- list()
    e$clock_ <- 0L
    e$get <- function(k) {
        # 把 function(下标 k) { 存入 e$get
        e$clock_ <<- e$clock_ + 1L  # e$clock_ 小于 小于 减 e$clock_ 加 1L
        key <- as.character(k)  # 把 as.character(下标 k) 存入 key
        if (!is.null(e$vals[[key]])) {
            # 若 取反 is.null(e$vals[[key]]
            e$freq[[key]] <<- e$freq[[key]] + 1L  # e$频次表[[key]] 小于 小于 减 e$频次表[[key]] 加 1L
            e$stamp[[key]] <<- e$clock_  # e$stamp[[key]] 小于 小于 减 e$clock_
            e$vals[[key]]  # e$vals[[key]]
        } else -1L  # 否则
    }
    e$put <- function(k, v) {
        # 把 function(下标 k, 值) { 存入 e$put
        e$clock_ <<- e$clock_ + 1L  # e$clock_ 小于 小于 减 e$clock_ 加 1L
        key <- as.character(k)  # 把 as.character(下标 k) 存入 key
        if (!is.null(e$vals[[key]])) {
            # 若 取反 is.null(e$vals[[key]]
            e$vals[[key]] <<- v  # e$vals[[key]] 小于 小于 减 值
            e$freq[[key]] <<- e$freq[[key]] + 1L  # e$频次表[[key]] 小于 小于 减 e$频次表[[key]] 加 1L
            e$stamp[[key]] <<- e$clock_  # e$stamp[[key]] 小于 小于 减 e$clock_
            return(invisible(NULL))  # 返回 invisible(NULL
        }
        if (e$cap == 0)
            return(invisible(NULL))  # 若 e$cap 等于 0) return(invisible(NULL
        if (length(e$vals) == e$cap) {
            # 若 长度(e$vals) 等于 e$cap
            ek <- NULL
            ef <- .Machine$integer.max
            es <- .Machine$integer.max
            for (key2 in names(e$vals)) {
                # for (key2 in names(e$vals)) {
                if (e$freq[[key2]] < ef || (e$freq[[key2]] == ef && e$stamp[[key2]] < es)) {
                  ef <- e$freq[[key2]]
                  es <- e$stamp[[key2]]
                  ek <- key2  # 把 e$频次表[[key2]]; es 小于 减 e$stamp[[key2]]; ek 小于 减 key2 存入 ef
                }
            }
            e$vals[[ek]] <<- NULL
            e$freq[[ek]] <<- NULL
            e$stamp[[ek]] <<- NULL
        }
        e$vals[[key]] <<- v
        e$freq[[key]] <<- 1L
        e$stamp[[key]] <<- e$clock_
    }
    e
}
lfu <- LfuSim(2)  # 把 LfuSim(2) 存入 lfu
lfu$put(1, 1)
lfu$put(2, 2)  # lfu$put(1, 1); lfu$put(2, 2)
stopifnot(lfu$get(1) == 1)  # 断言校验
lfu$put(3, 3)  # lfu$put(3, 3)
stopifnot(lfu$get(2) == -1, lfu$get(3) == 3)  # 断言校验
lfu$put(4, 4)  # lfu$put(4, 4)
stopifnot(lfu$get(1) == -1, lfu$get(3) == 3, lfu$get(4) == 4)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
