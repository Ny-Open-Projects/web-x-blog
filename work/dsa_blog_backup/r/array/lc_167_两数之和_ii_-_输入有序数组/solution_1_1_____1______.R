# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133524779 LeetCode 167. 两数之和II — R
# 版（方案1） 定义函数 two_sum_ii（参数：numbers, 目标值）
two_sum_ii <- function(numbers, target) {
    l <- 1L
    r <- length(numbers)  # 把 1L; 右指针 小于 减 长度(numbers) 存入 左指针
    while (l < r) {
        # 循环，直到不满足「左指针 小于 右指针」
        s <- numbers[l] + numbers[r]  # 把 numbers[左指针] 加 numbers[右指针] 存入 字符串
        if (s == target)
            return(c(l, r))  # 若 字符串 等于 目标值) return(字符(左指针, 右指针
        if (s < target)
            l <- l + 1L else r <- r - 1L  # 若 字符串 小于 目标值) 左指针 小于 减 左指针 加 1L else 右指针 小于 减 右指针 减 1L
    }
    integer(0)  # integer(0)
}
stopifnot(identical(two_sum_ii(c(2, 7, 11, 15), 9), c(1L, 2L)))  # 断言校验
stopifnot(identical(two_sum_ii(c(2, 3, 4), 6), c(1L, 3L)))  # 断言校验
stopifnot(identical(two_sum_ii(c(-1, 0), -1), c(1L, 2L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
