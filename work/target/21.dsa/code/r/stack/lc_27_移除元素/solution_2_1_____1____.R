# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114689 LeetCode 27. 移除元素 — R
# 版（方案2） 定义函数 remove_element（参数：数组, 值）
remove_element <- function(nums, val) {
    k <- 1L  # 把 1L 存入 下标 k
    for (i in seq_along(nums)) {
        # for (下标 i in seq_along(数组)) { 若 数组[下标 i] 不等于 值
        if (nums[i] != val) {
            nums[k] <- nums[i]  # 把 数组[下标 i] 存入 nums[k]
            k <- k + 1L  # 把 下标 k 加 1L 存入 下标 k
        }
    }
    k - 1L  # 下标 k 减 1L
}
stopifnot(remove_element(c(3, 2, 2, 3), 3) == 2)  # 断言校验
stopifnot(remove_element(c(0, 1, 2, 2, 3, 0, 4, 2), 2) == 5)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
