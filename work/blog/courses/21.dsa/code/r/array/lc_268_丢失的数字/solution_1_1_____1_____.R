# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133968437 LeetCode 268. 丢失的数字 — R
# 版（方案1） 定义函数 missing_number（参数：数组）
missing_number <- function(nums) {
    n <- length(nums)  # 把 长度(数组) 存入 元素个数
    as.integer((n * (n + 1L))%/%2L - sum(nums))  # as.integer((元素个数 乘 (元素个数 加 1L)) 对…取模 除以 对…取模 2L 减 累计和(数组))
}
stopifnot(missing_number(c(3, 0, 1)) == 2)  # 断言校验
stopifnot(missing_number(c(0, 1)) == 2)  # 断言校验
stopifnot(missing_number(c(9, 6, 4, 2, 3, 5, 7, 0, 1)) == 8)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
