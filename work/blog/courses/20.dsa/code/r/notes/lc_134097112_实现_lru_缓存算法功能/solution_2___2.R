# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134097112 实现LRU缓存算法功能 — R 版（方案2）
# 定义函数 NoteLruNote（参数：cap）
NoteLruNote <- function(cap) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$cap <- cap
    e$keys <- integer(0)
    e$vals <- list()  # 把 cap; e$keys 小于 减 integer(0); e$vals 小于 减 列表() 存入 e$cap
    e$get <- function(k) {
        # 把 function(下标 k) { 存入 e$get
        w <- match(k, e$keys)  # 把 match(下标 k, e$keys) 存入 权重
        if (is.na(w))
            return(-1L)  # 若 is.na(权重)) return( 减 1L
        e$keys <- c(e$keys[-w], e$keys[w])  # 把 字符(e$keys[ 减 权重], e$keys[权重]) 存入 e$keys
        e$vals[[as.character(k)]]  # e$vals[[as.character(下标 k)]]
    }
    e$put <- function(k, v) {
        # 把 function(下标 k, 值) { 存入 e$put
        w <- match(k, e$keys)  # 把 match(下标 k, e$keys) 存入 权重
        if (!is.na(w)) {
            # 若 取反 is.na(权重
            e$keys <- e$keys[-w]  # 把 e$keys[ 减 权重] 存入 e$keys
        } else if (length(e$keys) == e$cap) {
            # 否则，若 长度(e$keys) 等于 e$cap
            old <- e$keys[1]  # 把 e$keys[1] 存入 old
            e$keys <- e$keys[-1]  # 把 e$keys[ 减 1] 存入 e$keys
            e$vals[[as.character(old)]] <- NULL  # 把 NULL 存入 e$vals[[as.character(old)]]
        }
        e$keys <- c(e$keys, k)  # 把 字符(e$keys, 下标 k) 存入 e$keys
        e$vals[[as.character(k)]] <- v  # 把 值 存入 e$vals[[as.character(k)]]
    }
    e
}
c1 <- NoteLruNote(2)  # 把 NoteLruNote(2) 存入 c1
c1$put(1, 1)
c1$put(2, 2)  # c1$put(1, 1); c1$put(2, 2)
stopifnot(c1$get(1) == 1)  # 断言校验
c1$put(3, 3)  # c1$put(3, 3)
stopifnot(c1$get(2) == -1)  # 断言校验
c1$put(4, 4)  # c1$put(4, 4)
stopifnot(c1$get(1) == -1, c1$get(3) == 3, c1$get(4) == 4)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
