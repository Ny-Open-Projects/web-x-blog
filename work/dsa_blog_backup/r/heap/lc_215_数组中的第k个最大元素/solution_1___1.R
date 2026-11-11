# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440 LeetCode 215. 数组中的第K个最大元素
# — R 版（方案1） 定义函数 find_kth_largest（参数：数组, 下标 k）
find_kth_largest <- function(nums, k) {
    sort(nums, decreasing = TRUE)[k]  # 把 TRUE)[下标 k] 写入 sort(nums, decreasing
}
stopifnot(find_kth_largest(c(3, 2, 1, 5, 6, 4), 2) == 5)  # 断言校验
stopifnot(find_kth_largest(c(3, 2, 3, 1, 2, 4, 5, 5, 6), 4) == 4)  # 断言校验
stopifnot(find_kth_largest(c(1), 1) == 1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
