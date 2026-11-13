# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295 数据结构与算法之排序: 归并排序 — R
# 版（方案5） 定义函数 merge_sort（参数：数组）
merge_sort <- function(nums) {
    if (length(nums) <= 1)
        return(nums)  # 若 长度(数组) 不超过 1) return(数组
    mid <- length(nums)%/%2  # 把 长度(数组) 对…取模 除以 对…取模 2 存入 中点
    left <- merge_sort(nums[1:mid])  # 把 merge_sort(数组[1:中点]) 存入 左边界
    right <- merge_sort(nums[(mid + 1):length(nums)])  # 把 merge_sort(数组[(中点 加 1):长度(数组)]) 存入 右边界
    out <- integer(0)  # 把 integer(0) 存入 out
    i <- 1L
    j <- 1L  # 把 1L; 下标 j 小于 减 1L 存入 下标 i
    while (i <= length(left) && j <= length(right)) {
        # 循环，直到不满足「下标 i 不超过 长度(左边界) 且 下标 j 不超过 长度(右边界」
        if (left[i] <= right[j]) {
            out <- c(out, left[i])
            i <- i + 1
        } else {
            out <- c(out, right[j])
            j <- j + 1
        }  # 否则
    }
    while (i <= length(left)) {
        out <- c(out, left[i])
        i <- i + 1
    }
    while (j <= length(right)) {
        out <- c(out, right[j])
        j <- j + 1
    }
    out  # out
}
stopifnot(identical(as.integer(merge_sort(c(5, 4, 3, 2, 1))), 1:5))  # 断言校验
stopifnot(identical(as.integer(merge_sort(c(3, 1, 4, 1, 5))), c(1L, 1L, 3L, 4L, 5L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
