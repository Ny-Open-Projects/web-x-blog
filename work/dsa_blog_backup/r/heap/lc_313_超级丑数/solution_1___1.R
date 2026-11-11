# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133547933 LeetCode 313. 超级丑数 — R
# 版（方案1） 定义函数 nth_super_ugly_number（参数：元素个数, primes）
nth_super_ugly_number <- function(n, primes) {
    ugly <- rep(1, n)  # 把 rep(1, 元素个数) 存入 ugly
    idx <- rep(1L, length(primes))  # 把 rep(1L, 长度(primes)) 存入 idx
    val <- primes  # 把 primes 存入 值
    if (n >= 2)
        for (i in 2:n) {
            # 若 元素个数 不低于 2) for (下标 i in 2:元素个数
            next_v <- min(val)  # 把 取较小值 值) 存入 next_v
            ugly[i] <- next_v  # 把 next_v 存入 ugly[i]
            for (k in seq_along(primes)) {
                # for (下标 k in seq_along(primes)) { 若 值[下标 k] 等于 next_v
                if (val[k] == next_v) {
                  idx[k] <- idx[k] + 1L  # 把 idx[下标 k] 加 1L 存入 idx[k]
                  val[k] <- ugly[idx[k]] * primes[k]  # 把 ugly[idx[下标 k]] 乘 primes[下标 k] 存入 val[k]
                }
            }
        }
    ugly[n]  # ugly[元素个数]
}
stopifnot(nth_super_ugly_number(12, c(2, 7, 13, 19)) == 32)  # 断言校验
stopifnot(nth_super_ugly_number(1, c(2, 7, 13, 19)) == 1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
