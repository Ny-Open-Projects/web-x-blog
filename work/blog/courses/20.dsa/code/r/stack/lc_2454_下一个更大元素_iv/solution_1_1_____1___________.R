# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397916 LeetCode 2454. 下一个更大元素 IV —
# R 版（方案1） 定义函数 second_greater（参数：数组）
second_greater <- function(nums) {
    n <- length(nums)  # 把 长度(数组) 存入 元素个数
    res <- rep(-1L, n)  # 把 rep( 减 1L, 元素个数) 存入 结果
    s1 <- integer(0)
    s2 <- integer(0)  # 把 integer(0); s2 小于 减 integer(0) 存入 s1
    for (i in seq_len(n)) {
        # for (下标 i in seq_len(元素个数)) { 循环，直到不满足「长度(s2) 超过 0 且 数组[s2[长度(s2)]] 小于
        # 数组[下标 i]」
        while (length(s2) > 0 && nums[s2[length(s2)]] < nums[i]) {
            res[s2[length(s2)]] <- nums[i]  # 把 数组[下标 i] 存入 res[s2[length(s2)]]
            s2 <- s2[-length(s2)]  # 把 s2[ 减 长度(s2)] 存入 s2
        }
        while (length(s1) > 0 && nums[s1[length(s1)]] < nums[i]) {
            # 循环，直到不满足「长度(s1) 超过 0 且 数组[s1[长度(s1)]] 小于 数组[下标 i]」
            s2 <- c(s2, s1[length(s1)])  # 把 字符(s2, s1[长度(s1)]) 存入 s2
            s1 <- s1[-length(s1)]  # 把 s1[ 减 长度(s1)] 存入 s1
        }
        s1 <- c(s1, i)  # 把 字符(s1, 下标 i) 存入 s1
    }
    res  # 结果
}
stopifnot(identical(as.integer(second_greater(c(2, 4, 0, 9, 6))), c(9L, 6L, 6L, -1L, -1L)))  # 断言校验
stopifnot(identical(as.integer(second_greater(c(5, 4, 3, 2, 1))), rep(-1L, 5)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
