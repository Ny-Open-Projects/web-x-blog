# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731 LeetCode 69. x 的平方根 — R 版（4 )
# 方案4：二分（返回 hi）） 用 double 运算（精确到 2^53），x 上限 2^31 内比较语义安全 定义函数
# my_sqrt（参数：x）
my_sqrt <- function(x) {
    x <- as.numeric(x)  # 把 as.numeric(x) 存入 x
    lo <- 1
    hi <- x  # 把 1; 右边界 小于 减 x 存入 左边界
    while (lo <= hi) {
        # 循环，直到不满足「左边界 不超过 右边界」
        m <- floor(lo + (hi - lo)/2)  # 把 floor(左边界 加 (右边界 减 左边界) 除以 2) 存入 映射表
        if (m * m == x)
            return(m)  # 若 映射表 乘 映射表 等于 x) return(映射表
 else if (m * m < x)
            lo <- m + 1 else hi <- m - 1  # 否则，若 映射表 乘 映射表 小于 x) 左边界 小于 减 映射表 加 1 else 右边界 小于 减 映射表 减 1
    }
    hi  # 右边界
}
cs <- matrix(c(4, 2, 8, 2, 16, 4, 2147395599, 46339), ncol = 2, byrow = TRUE)
for (i in seq_len(nrow(cs))) stopifnot(my_sqrt(cs[i, 1]) == cs[i, 2])  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
