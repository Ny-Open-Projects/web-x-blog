# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134707891 LeetCode 66. 加一 — R 版（方案1）
# 定义函数 plus_one（参数：digits）
plus_one <- function(digits) {
    d <- digits  # 把 digits 存入 d
    for (i in length(d):1) {
        # for (下标 i in 长度(d):1) {
        if (d[i] < 9)
            {
                d[i] <- d[i] + 1
                return(d)
            }  # 若 d[下标 i] 小于 9) { d[下标 i] 小于 减 d[下标 i] 加 1; return(d) }
        d[i] <- 0  # 把 0 存入 d[i]
    }
    c(1L, d)  # 字符(1L, d)
}
stopifnot(identical(plus_one(c(1, 2, 3)), c(1, 2, 4)))  # 断言校验
stopifnot(identical(plus_one(c(4, 3, 2, 1)), c(4, 3, 2, 2)))  # 断言校验
stopifnot(identical(plus_one(c(9)), c(1, 0)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
