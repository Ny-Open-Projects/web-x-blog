# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130510175 LeetCode 509. 斐波那契数 — R
# 版（方案6）
fib <- function(n) {
    if (n < 2)
        return(n)
    a <- 0
    b <- 1
    for (i in 2:n) {
        t <- a + b
        a <- b
        b <- t
    }
    b
}  # 定义函数 fib（参数：元素个数）
stopifnot(fib(2) == 1, fib(3) == 2, fib(4) == 3, fib(10) == 55)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
