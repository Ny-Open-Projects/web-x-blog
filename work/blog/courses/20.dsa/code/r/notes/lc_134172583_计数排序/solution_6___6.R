# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583 数据结构与算法之排序: 计数排序 — R
# 版（方案6） 定义函数 count_sort（参数：数组）
count_sort <- function(nums) {
    if (length(nums) == 0)
        return(nums)  # 若 长度(数组) 等于 0) return(数组
    mx <- max(nums)
    mn <- min(nums)  # 把 取较大值 数组); mn 小于 减 取较小值 数组) 存入 mx
    range_ <- mx - mn + 1L  # 把 mx 减 mn 加 1L 存入 range_
    count <- rep(0L, range_)  # 把 rep(0L, range_) 存入 计数
    for (v in nums) count[v - mn + 1L] <- count[v - mn + 1L] + 1L  # for (值 in 数组) 计数[值 减 mn 加 1L] 小于 减 计数[值 减 mn 加 1L] 加 1L
    for (i in 2:range_) count[i] <- count[i] + count[i - 1L]
    output <- integer(length(nums))  # 把 integer(长度(数组)) 存入 输出
    for (i in length(nums):1) {
        # for (下标 i in 长度(数组):1) {
        idx <- nums[i] - mn + 1L  # 把 数组[下标 i] 减 mn 加 1L 存入 idx
        output[count[idx]] <- nums[i]  # 把 数组[下标 i] 存入 output[count[idx]]
        count[idx] <- count[idx] - 1L  # 把 计数[idx] 减 1L 存入 count[idx]
    }
    output  # 输出
}
stopifnot(identical(as.integer(count_sort(c(5, 3, 8, 3, 1))), c(1L, 3L, 3L, 5L, 8L)))  # 断言校验
big <- count_sort(c(102, 103, 108, 107, 101, 102, 102, 102, 107, 103, 109, 108, 102, 101, 104, 102, 104, 106, 109,
    102))
stopifnot(length(big) == 20, as.integer(big[1]) == 101, as.integer(big[20]) == 109)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
