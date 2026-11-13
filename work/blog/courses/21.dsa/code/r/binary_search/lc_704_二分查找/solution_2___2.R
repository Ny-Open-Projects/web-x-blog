# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134221939 LeetCode 704. 二分查找 — R 版
# 返回 0 基下标（与 TS 参考一致），R 向量本身 1 基，读取时 +1 定义函数 search（参数：数组, 目标值）
search <- function(nums, target) {
    left <- 0L  # 把 0L 存入 左边界
    right <- length(nums) - 1L  # 把 长度(数组) 减 1L 存入 右边界
    while (left <= right) {
        # 循环，直到不满足「左边界 不超过 右边界」
        mid <- left + (right - left)%/%2L  # 把 左边界 加 (右边界 减 左边界) 对…取模 除以 对…取模 2L 存入 中点
        v <- nums[mid + 1L]  # 把 数组[中点 加 1L] 存入 值
        if (v == target) {
            # 若 值 等于 目标值
            return(mid)  # 返回 中点
        } else if (v < target) {
            # 否则，若 值 小于 目标值
            left <- mid + 1L  # 把 中点 加 1L 存入 左边界
        } else {
            # 否则
            right <- mid - 1L  # 把 中点 减 1L 存入 右边界
        }
    }
    -1L  # 减 1L
}
# 自测：与 LeetCode 官方用例一致
stopifnot(identical(search(c(1, 2, 3), 1), 0L))  # 断言校验
stopifnot(identical(search(c(-1, 0, 3, 5, 9, 12), 9), 4L))  # 断言校验
stopifnot(identical(search(c(-1, 0, 3, 5, 9, 12), 2), -1L))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
