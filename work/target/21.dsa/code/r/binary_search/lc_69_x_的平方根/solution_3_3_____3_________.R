# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731 LeetCode 69. x 的平方根 — R 版（3 )
# 方案3：牛顿迭代） 用 double 运算（精确到 2^53），x 上限 2^31 内比较语义安全 定义函数 my_sqrt（参数：x）
my_sqrt <- function(x) {
    x <- as.numeric(x)  # 把 as.numeric(x) 存入 x
    if (x < 2)
        return(x)  # 若 x 小于 2) return(x
    r <- x  # 把 x 存入 右指针
    while (r * r > x) r <- floor((r + x/r)/2)
    r  # 右指针
}
cs <- matrix(c(4, 2, 8, 2, 16, 4, 2147395599, 46339), ncol = 2, byrow = TRUE)
for (i in seq_len(nrow(cs))) stopifnot(my_sqrt(cs[i, 1]) == cs[i, 2])  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
