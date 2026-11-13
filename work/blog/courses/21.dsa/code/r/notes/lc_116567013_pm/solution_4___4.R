# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013 LeetCode 116567013. PM — R
# 版（方案4：buildNext 单测） 定义函数 build_next（参数：节点）
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
eq_arr <- function(a, b) identical(as.integer(a), as.integer(b))  # 定义函数 eq_arr（参数：数组, b）
stopifnot(eq_arr(build_next("ababaca"), c(-1, 0, 0, 1, 2, 3, 0)))  # 断言校验
stopifnot(eq_arr(build_next("aaaa"), c(-1, 0, 1, 2)))  # 断言校验
stopifnot(eq_arr(build_next("abcabc"), c(-1, 0, 0, 0, 1, 2)))  # 断言校验
stopifnot(eq_arr(build_next("abcd"), c(-1, 0, 0, 0)))  # 断言校验
stopifnot(eq_arr(build_next("a"), c(-1)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
