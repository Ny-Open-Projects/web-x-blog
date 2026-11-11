# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792 数据结构与算法之排序: 快速排序 — R
# 版（方案1） 定义函数 quick_sort（参数：数组）
quick_sort <- function(nums) {
    if (length(nums) <= 1)
        return(nums)  # 若 长度(数组) 不超过 1) return(数组
    pivot <- nums[floor(length(nums)/2) + 1]  # 把 数组[floor(长度(数组) 除以 2) 加 1] 存入 pivot
    c(quick_sort(nums[nums < pivot]), nums[nums == pivot], quick_sort(nums[nums > pivot]))
}
stopifnot(identical(as.integer(quick_sort(c(5, 4, 3, 2, 1))), 1:5))  # 断言校验
stopifnot(identical(as.integer(quick_sort(c(3, 1, 4, 1, 5))), c(1L, 1L, 3L, 4L, 5L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
