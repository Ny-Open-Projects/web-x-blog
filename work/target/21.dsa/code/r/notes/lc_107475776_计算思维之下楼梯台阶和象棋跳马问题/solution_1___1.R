# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776 计算思维之下楼梯台阶和象棋跳马问题
# — R 版（方案1） 定义函数 climb_stairs_variants（参数：元素个数）
climb_stairs_variants <- function(n) {
    if (n <= 1)
        return(1)  # 若 元素个数 不超过 1) return(1
    a <- 1
    b <- 1  # 把 1; b 小于 减 1 存入 数组
    for (i in 2:n) {
        t <- a + b
        a <- b
        b <- t
    }
    b
}
stopifnot(climb_stairs_variants(10) == 89, climb_stairs_variants(1) == 1, climb_stairs_variants(2) == 2)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
