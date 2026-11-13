# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483 LeetCode 108673483. 减治策略 — R
# 版（方案1：二分查找） 定义函数 binary_search（参数：数组, 目标值）
binary_search <- function(arr, target) {
    left <- 1L  # 把 1L 存入 左边界
    right <- length(arr)  # 把 长度(数组) 存入 右边界
    while (left <= right) {
        # 循环，直到不满足「左边界 不超过 右边界」
        mid <- as.integer((left + right)%/%2)  # 把 as.integer((左边界 加 右边界) 对…取模 除以 对…取模 2) 存入 中点
        if (arr[mid] == target)
            return(as.integer(mid - 1L))  # 若 数组[中点] 等于 目标值) return(as.integer(中点 减 1L
        if (arr[mid] < target)
            left <- mid + 1L else right <- mid - 1L  # 若 数组[中点] 小于 目标值) 左边界 小于 减 中点 加 1L else 右边界 小于 减 中点 减 1L
    }
    -1L  # 减 1L
}
cases <- list(list(c(1L, 3L, 5L, 7L, 9L), 5L, 2L), list(c(1L, 3L, 5L, 7L, 9L), 4L, -1L), list(c(), 5L, -1L), list(c(1L,
    3L, 5L, 7L, 9L), 1L, 0L)  # 列表(字符(1L, 3L, 5L, 7L, 9L), 1L, 0L)
)
for (idx in seq_along(cases)) {
    # for (idx in seq_along(cases)) {
    got <- binary_search(cases[[idx]][[1]], cases[[idx]][[2]])  # 把 binary_search(cases[[idx]][[1]], cases[[idx]][[2]]) 存入 got
    stopifnot(got == cases[[idx]][[3]])  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
