# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/99759428 数据结构与算法之数组操作 — R
# 版（方案1） 定义函数 two_sum（参数：数组, 目标值） for (下标 i in seq_along(数组)) { for (下标 j in (下标 i
# 加 1L):长度(数组)) {
two_sum <- function(nums, target) {
    for (i in seq_along(nums)) {
        for (j in (i + 1L):length(nums)) {
            if (nums[i] + nums[j] == target)
                return(c(i - 1L, j - 1L))  # 若 数组[下标 i] 加 数组[下标 j] 等于 目标值) return(字符(下标 i 减 1L, 下标 j 减 1L
        }
    }
    integer(0)  # integer(0)
}
max_sub_array <- function(nums) {
    # 定义函数 max_sub_array（参数：数组）
    best <- nums[1]
    cur <- nums[1]  # 把 数组[1]; 当前值 小于 减 数组[1] 存入 当前最优
    for (v in nums[-1]) {
        # for (值 in 数组[ 减 1]) {
        cur <- max(cur + v, v)  # 把 取较大值 当前值 加 值, 值) 存入 当前值
        best <- max(best, cur)  # 把 取较大值 当前最优, 当前值) 存入 当前最优
    }
    best  # 当前最优
}
rotate_array <- function(nums, k) {
    # 定义函数 rotate_array（参数：数组, 下标 k）
    n <- length(nums)  # 把 长度(数组) 存入 元素个数
    k <- k%%n  # 把 下标 k 对…取模 对…取模 元素个数 存入 下标 k
    c(nums[(n - k + 1L):n], nums[1:(n - k)])  # 字符(数组[(元素个数 减 下标 k 加 1L):元素个数], 数组[1:(元素个数 减 下标 k)])
}
stopifnot(identical(as.integer(two_sum(c(2, 7, 11, 15), 9)), c(0L, 1L)))  # 断言校验
stopifnot(max_sub_array(c(-2, 1, -3, 4, -1, 2, 1, -5, 4)) == 6)  # 断言校验
stopifnot(identical(as.integer(rotate_array(c(1, 2, 3, 4, 5, 6, 7), 3)), c(5L, 6L, 7L, 1L, 2L, 3L, 4L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
