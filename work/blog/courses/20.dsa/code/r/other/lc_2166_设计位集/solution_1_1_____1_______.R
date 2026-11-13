# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145556343 LeetCode 2166. 设计位集 — R
# 版（方案1） 定义函数 Bitset（参数：大小）
Bitset <- function(size) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$n <- size  # 把 大小 存入 e$n
    e$words <- rep(0, (size + 31)%/%32)  # 把 rep(0, (大小 加 31) 对…取模 除以 对…取模 32) 存入 e$words
    e$ones <- 0L  # 把 0L 存入 e$ones
    e$reverse <- 0L  # 把 0L 存入 e$reverse
    e$get <- function(idx) {
        # 把 function(idx) { 存入 e$get
        w <- e$words[(idx%/%32) + 1]  # 把 e$单词列表[(idx 对…取模 除以 对…取模 32) 加 1] 存入 权重
        bitwXor(bitwAnd(bitwShiftR(w, idx%%32), 1L), e$reverse)
    }
    e$fix <- function(idx) {
        # 把 function(idx) { 存入 e$fix 若 e$get(idx) 等于 0
        if (e$get(idx) == 0) {
            wi <- (idx%/%32) + 1  # 把 (idx 对…取模 除以 对…取模 32) 加 1 存入 wi
            e$words[wi] <- bitwOr(e$words[wi], bitwShiftL(1, idx%%32))
            e$ones <- e$ones + 1L  # 把 e$ones 加 1L 存入 e$ones
        }
    }
    e$unfix <- function(idx) {
        # 把 function(idx) { 存入 e$unfix 若 e$get(idx) 等于 1
        if (e$get(idx) == 1) {
            wi <- (idx%/%32) + 1  # 把 (idx 对…取模 除以 对…取模 32) 加 1 存入 wi
            e$words[wi] <- bitwAnd(e$words[wi], bitwNot(bitwShiftL(1, idx%%32)))
            e$ones <- e$ones - 1L  # 把 e$ones 减 1L 存入 e$ones
        }
    }
    e$flip <- function() {
        # 把 function() { 存入 e$flip
        e$reverse <- bitwXor(e$reverse, 1L)  # 把 bitwXor(e$reverse, 1L) 存入 e$reverse
        e$ones <- e$n - e$ones  # 把 e$元素个数 减 e$ones 存入 e$ones
    }
    e$all <- function() e$ones == e$n  # 把 function() e$ones 等于 e$元素个数 存入 e$all
    e$one <- function() e$ones > 0  # 把 function() e$ones 超过 0 存入 e$one
    e$count <- function() e$ones  # 把 function() e$ones 存入 e$count
    e$tostring <- function() {
        # 把 function() { 存入 e$tostring
        paste(vapply(seq_len(e$n) - 1L, function(i) as.character(e$get(i)), ""), collapse = "")
    }
    e
}
bs <- Bitset(5)  # 把 Bitset(5) 存入 bs
bs$fix(0)
bs$fix(3)  # bs$fix(0); bs$fix(3)
stopifnot(bs$tostring() == "10010", bs$count() == 2)  # 断言校验
bs$flip()  # bs$flip()
stopifnot(bs$tostring() == "01101", bs$count() == 3)  # 断言校验
bs$unfix(0)  # bs$unfix(0)
stopifnot(bs$tostring() == "01101")  # 断言校验
stopifnot(bs$all() == FALSE, bs$one() == TRUE)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
