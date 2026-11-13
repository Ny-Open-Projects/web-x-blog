# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134893847 LeetCode 905. 按奇偶排序数组 — R
# 版（方案2） 定义函数 sort_array_by_parity（参数：数组）
sort_array_by_parity <- function(nums) {
    even <- nums[nums%%2 == 0]  # 把 数组[数组 对…取模 对…取模 2 等于 0] 存入 even
    odd <- nums[nums%%2 != 0]  # 把 数组[数组 对…取模 对…取模 2 不等于 0] 存入 odd
    c(even, odd)  # 字符(even, odd)
}
g1 <- sort_array_by_parity(c(3, 1, 2, 3 + 1))  # 把 sort_array_by_parity(字符(3, 1, 2, 3 加 1)) 存入 g1
stopifnot(length(g1) == 4, g1[1]%%2 == 0, g1[2]%%2 == 0, g1[3]%%2 == 1)  # 断言校验
g2 <- sort_array_by_parity(c(1, 2, 3))  # 把 sort_array_by_parity(字符(1, 2, 3)) 存入 g2
stopifnot(identical(g2, c(2, 1, 3)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
