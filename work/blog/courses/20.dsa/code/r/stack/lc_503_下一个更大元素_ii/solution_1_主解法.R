# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145045460 LeetCode 503. 下一个更大元素 II — R
# 版（方案1） 定义函数 next_greater_elements（参数：数组）
next_greater_elements <- function(nums) {
    n <- length(nums)  # 把 长度(数组) 存入 元素个数
    res <- rep(-1L, n)  # 把 rep( 减 1L, 元素个数) 存入 结果
    st <- integer(0)  # 把 integer(0) 存入 st
    for (i in 1:(2 * n)) {
        # for (下标 i in 1:(2 乘 元素个数)) {
        ii <- (i - 1)%%n + 1  # 把 (下标 i 减 1) 对…取模 对…取模 元素个数 加 1 存入 ii
        while (length(st) > 0 && nums[st[length(st)]] < nums[ii]) {
            # 循环，直到不满足「长度(st) 超过 0 且 数组[st[长度(st)]] 小于 数组[ii]」
            res[st[length(st)]] <- nums[ii]  # 把 数组[ii] 存入 res[st[length(st)]]
            st <- st[-length(st)]  # 把 st[ 减 长度(st)] 存入 st
        }
        if (i <= n)
            st <- c(st, ii)  # 若 下标 i 不超过 元素个数) st 小于 减 字符(st, ii
    }
    res  # 结果
}
stopifnot(identical(as.integer(next_greater_elements(c(1, 2, 1))), c(2L, -1L, 2L)))  # 断言校验
stopifnot(identical(as.integer(next_greater_elements(c(3, 2, 1))), c(-1L, 3L, 3L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
