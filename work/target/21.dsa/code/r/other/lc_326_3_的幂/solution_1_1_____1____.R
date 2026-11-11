# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135359346 LeetCode 326. 3的幂 — R 版（方案1）
# 定义函数 is_power_of_three（参数：元素个数）
is_power_of_three <- function(n) {
    while (n != 0 && n%%3 == 0) n <- n%/%3
    n == 1  # 把 赋值为 1 存入 元素个数
}
stopifnot(is_power_of_three(27), !is_power_of_three(0), is_power_of_three(9), !is_power_of_three(-1), is_power_of_three(1))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
