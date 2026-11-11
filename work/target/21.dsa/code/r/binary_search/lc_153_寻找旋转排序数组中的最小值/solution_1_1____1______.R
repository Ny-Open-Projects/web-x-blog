# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233483 LeetCode 153.
# 寻找旋转排序数组中的最小值 — R 版（方案1：二分查找）
# 0 基下标语义与 TS 参考一致（R 向量本身 1 基，读取时 +1） 定义函数 findMin（参数：数组）
findMin <- function(nums) {
    low <- 0L  # 把 0L 存入 low
    high <- length(nums) - 1L  # 把 长度(数组) 减 1L 存入 high
    while (low < high) {
        # 循环，直到不满足「low 小于 high」
        pivot <- low + (high - low)%/%2L  # 防溢出写法（R 整数除法 %/%）
        if (nums[pivot + 1L] < nums[high + 1L]) {
            # 若 数组[pivot 加 1L] 小于 数组[high 加 1L]
            high <- pivot  # 把 pivot 存入 high
        } else {
            # 否则
            low <- pivot + 1L  # 把 pivot 加 1L 存入 low
        }
    }
    nums[low + 1L]  # 数组[low 加 1L]
}
# 自测：与 LeetCode 官方用例一致
stopifnot(identical(findMin(c(1L, 2L, 3L)), 1L))  # 断言校验
stopifnot(identical(findMin(c(3L, 4L, 5L, 1L, 2L)), 1L))  # 断言校验
stopifnot(identical(findMin(c(4L, 5L, 6L, 7L, 0L, 1L, 2L)), 0L))  # 断言校验
stopifnot(identical(findMin(c(11L, 13L, 15L, 17L)), 11L))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
