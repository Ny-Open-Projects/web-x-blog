# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233077 LeetCode 35. 搜索插入位置 — R
# 版（方案1：二分查找） 定义函数 search_insert（参数：数组, 目标值）
search_insert <- function(nums, target) {
    left <- 1L
    right <- length(nums) + 1L  # 把 1L; 右边界 小于 减 长度(数组) 加 1L 存入 左边界
    while (left < right) {
        # 循环，直到不满足「左边界 小于 右边界」
        mid <- left + (right - left)%/%2L  # 把 左边界 加 (右边界 减 左边界) 对…取模 除以 对…取模 2L 存入 中点
        if (nums[mid] < target)
            left <- mid + 1L else right <- mid  # 若 数组[中点] 小于 目标值) 左边界 小于 减 中点 加 1L else 右边界 小于 减 中点
    }
    left - 1L  # 左边界 减 1L
}
stopifnot(search_insert(c(1L, 2L, 3L), 1L) == 0L)  # 断言校验
stopifnot(search_insert(c(1L, 3L, 5L, 6L), 5L) == 2L)  # 断言校验
stopifnot(search_insert(c(1L, 3L, 5L, 6L), 2L) == 1L)  # 断言校验
stopifnot(search_insert(c(1L, 3L, 5L, 6L), 7L) == 4L)  # 断言校验
stopifnot(search_insert(c(1L, 3L, 5L, 6L), 0L) == 0L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
