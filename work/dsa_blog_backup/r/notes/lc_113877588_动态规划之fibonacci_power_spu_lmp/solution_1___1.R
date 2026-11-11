# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113877588 动态规划之Fibonacci — R 版（方案1）
# 定义函数 fib_memo（参数：元素个数）
fib_memo <- function(n) {
    memo <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 记忆化表
    go <- function(k) {
        # 定义函数 go（参数：下标 k）
        if (k <= 1)
            return(k)  # 若 下标 k 不超过 1) return(下标 k
        key <- as.character(k)  # 把 as.character(下标 k) 存入 key
        if (!is.null(memo[[key]]))
            return(memo[[key]])  # 若 取反 is.null(记忆化表[[key]])) return(记忆化表[[key]]
        memo[[key]] <<- go(k - 1L) + go(k - 2L)  # 记忆化表[[key]] 小于 小于 减 go(下标 k 减 1L) 加 go(下标 k 减 2L)
        memo[[key]]  # 记忆化表[[key]]
    }
    go(n)  # go(元素个数)
}
stopifnot(fib_memo(10) == 55, fib_memo(20) == 6765, fib_memo(0) == 0)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
