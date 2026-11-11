# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130506068 LeetCode 70. 爬楼梯 — R 版（方案2）
climb_stairs <- function(n) {
    if (n <= 2)
        return(n)
    a <- 1L
    b <- 2L
    for (i in 3:n) {
        t <- a + b
        a <- b
        b <- t
    }
    b
}  # 定义函数 climb_stairs（参数：元素个数）
stopifnot(climb_stairs(2) == 2, climb_stairs(3) == 3, climb_stairs(10) == 89)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
