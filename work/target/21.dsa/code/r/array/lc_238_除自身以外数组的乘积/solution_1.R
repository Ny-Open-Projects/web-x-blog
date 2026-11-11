# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133907522 LeetCode 238. 除自身以外数组的乘积
# — R 版（方案1） 定义函数 product_except_self（参数：数组）
product_except_self <- function(nums) {
    n <- length(nums)  # 把 长度(数组) 存入 元素个数
    out <- rep(1, n)  # 把 rep(1, 元素个数) 存入 out
    left <- 1  # 把 1 存入 左边界
    for (i in seq_len(n)) {
        out[i] <- left
        left <- left * nums[i]
    }
    right <- 1  # 把 1 存入 右边界
    for (i in n:1) {
        out[i] <- out[i] * right
        right <- right * nums[i]
    }
    out  # out
}
stopifnot(identical(product_except_self(c(1, 2, 3, 4)), c(24, 12, 8, 6)))  # 断言校验
stopifnot(identical(product_except_self(c(-1, 1, 0, -3, 3)), c(0, 0, 9, 0, 0)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
