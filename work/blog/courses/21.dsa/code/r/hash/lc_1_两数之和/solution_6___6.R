# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130663853 LeetCode 1. 两数之和 — R
# 版（方案6：哈希表一次遍历） 定义函数 two_sum（参数：数组, 目标值）
two_sum <- function(nums, target) {
    seen <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 已见集合
    for (i in seq_along(nums)) {
        # for (下标 i in seq_along(数组)) {
        need <- target - nums[i]  # 把 目标值 减 数组[下标 i] 存入 need
        if (!is.null(seen[[as.character(need)]])) {
            # 若 取反 is.null(已见集合[[as.character(need)]]
            return(c(seen[[as.character(need)]], i - 1L))  # 返回 字符(已见集合[[as.character(need)]], 下标 i 减 1L
        }
        seen[[as.character(nums[i])]] <- i - 1L  # 把 下标 i 减 1L 存入 seen[[as.character(nums[i])]]
    }
    integer(0)  # integer(0)
}
stopifnot(identical(two_sum(c(2, 7, 11, 15), 9), c(0L, 1L)))  # 断言校验
stopifnot(identical(two_sum(c(3, 2, 4), 6), c(1L, 2L)))  # 断言校验
stopifnot(identical(two_sum(c(3, 3), 6), c(0L, 1L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
