# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013 LeetCode 116567013. PM — R
# 版（方案3：KMP，next 表失配大步跳跃） 定义函数 build_next（参数：节点）
build_next <- function(p) {
    m <- nchar(p)  # 把 nchar(节点) 存入 映射表
    N <- rep(-1L, m)  # 把 rep( 减 1L, 映射表) 存入 N
    J <- 0L
    T <- -1L  # 0 基逻辑游标（存储按 1 基下标）
    pc <- function(k) substr(p, k, k)  # 定义函数 pc（参数：下标 k）
    while (J < m - 1L) {
        # 循环，直到不满足「J 小于 映射表 减 1L」 若 T 小于 0L 或 pc(J 加 1L) 等于 pc(T 加 1L
        if (T < 0L || pc(J + 1L) == pc(T + 1L)) {
            J <- J + 1L
            T <- T + 1L  # 把 J 加 1L; T 小于 减 T 加 1L 存入 J
            N[J + 1L] <- T  # N[J 加 1L] 小于 减 T
        } else {
            # 否则
            T <- N[T + 1L]  # 把 N[T 加 1L] 存入 T
        }
    }
    as.integer(N)  # as.integer(N)
}
kmp_match <- function(p, t) {
    # 定义函数 kmp_match（参数：节点, 另一字符串）
    N <- build_next(p)  # 把 build_next(节点) 存入 N
    n <- nchar(t)
    m <- nchar(p)  # 把 nchar(另一字符串); 映射表 小于 减 nchar(节点) 存入 元素个数
    i <- 1L
    j <- 1L  # 把 1L; 下标 j 小于 减 1L 存入 下标 i
    at <- function(s, k) substr(s, k, k)  # 定义函数 at（参数：字符串, 下标 k）
    while (j <= m && i <= n) {
        # 循环，直到不满足「下标 j 不超过 映射表 且 下标 i 不超过 元素个数」 若 下标 j 小于 1L 或
        # at(另一字符串, 下标 i) 等于 at(节点, 下标 j
        if (j < 1L || at(t, i) == at(p, j)) {
            i <- i + 1L
            j <- j + 1L  # 把 下标 i 加 1L; 下标 j 小于 减 下标 j 加 1L 存入 下标 i
        } else {
            # 否则
            j <- N[j] + 1L  # 0 基转 1 基
        }
    }
    if (j > m)
        return(as.integer(i - j))  # 若 下标 j 超过 映射表) return(as.integer(下标 i 减 下标 j
    -1L  # 减 1L
}
eq_arr <- function(a, b) identical(as.integer(a), as.integer(b))  # 定义函数 eq_arr（参数：数组, b）
T <- "now is the time for all good people to come"  # 把 「now is the time for all good people to come」 存入 T
cases <- list(list("people", T, 29L), list("all", T, 20L), list("no", T, 0L), list("xyz", T, -1L), list("a", "",
    -1L)  # 列表(「xyz」, T, 减 1L), 列表(「xyz」, 「xyz」, 减 1L)
)
for (idx in seq_along(cases)) {
    # for (idx in seq_along(cases)) {
    stopifnot(kmp_match(cases[[idx]][[1]], cases[[idx]][[2]]) == cases[[idx]][[3]])  # 断言校验
}
stopifnot(kmp_match("aaaa", "aaaaa") == 0L)  # 断言校验
stopifnot(kmp_match("aaab", "aaabaaa") == 0L)  # 断言校验
stopifnot(eq_arr(build_next("ababaca"), c(-1, 0, 0, 1, 2, 3, 0)))  # 断言校验
stopifnot(eq_arr(build_next("aaaa"), c(-1, 0, 1, 2)))  # 断言校验
stopifnot(eq_arr(build_next("abcd"), c(-1, 0, 0, 0)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
