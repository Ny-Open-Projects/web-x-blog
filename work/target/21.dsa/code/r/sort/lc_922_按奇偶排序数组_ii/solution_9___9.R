# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975 LeetCode 922. 按奇偶排序数组II — R
# 版（方案9） 定义函数 sort_array_by_parity_ii（参数：数组）
sort_array_by_parity_ii <- function(nums) {
    sorted <- sort(nums)  # 把 sort(数组) 存入 sorted
    res <- integer(length(sorted))  # 把 integer(长度(sorted)) 存入 结果
    odd <- 2
    even <- 1  # 把 2; even 小于 减 1 存入 odd
    for (item in sorted) {
        # for (item in sorted) {
        if (item%%2 == 1) {
            res[odd] <- item
            odd <- odd + 2
        } else {
            res[even] <- item
            even <- even + 2
        }
    }
    res  # 结果
}
stopifnot(identical(sort_array_by_parity_ii(c(4, 2, 5, 7)), c(2, 5, 4, 7)))  # 断言校验
stopifnot(identical(sort_array_by_parity_ii(c(2, 3)), c(2, 3)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
