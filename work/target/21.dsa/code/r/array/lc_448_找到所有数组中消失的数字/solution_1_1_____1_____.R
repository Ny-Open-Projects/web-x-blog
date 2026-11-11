# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134378688 LeetCode 448.
# 找到所有数组中消失的数字 — R 版（方案1） 定义函数 find_disappeared（参数：数组）
find_disappeared <- function(nums) {
    n <- length(nums)  # 把 长度(数组) 存入 元素个数
    present <- seq_len(n) %in% nums  # 把 seq_len(元素个数) 对…取模 in 对…取模 数组 存入 present
    which(!present)  # which(取反 present)
}
stopifnot(identical(find_disappeared(c(4, 3, 2, 7, 8, 2, 3, 1)), c(5L, 6L)))  # 断言校验
stopifnot(identical(find_disappeared(c(1, 1)), 2L))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
