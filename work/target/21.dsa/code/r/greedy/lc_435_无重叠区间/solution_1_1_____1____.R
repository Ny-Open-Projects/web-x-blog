# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135941089 LeetCode 435. 无重叠区间 — R
# 版（方案1） 定义函数 erase_overlap_intervals（参数：intervals）
erase_overlap_intervals <- function(intervals) {
    if (nrow(intervals) == 0)
        return(0L)  # 若 nrow(intervals) 等于 0) return(0L
    ord <- order(intervals[, 2])  # 把 order(intervals[, 2]) 存入 ord
    arr <- intervals[ord, , drop = FALSE]  # 把 intervals[ord, , drop 赋值为 FALSE] 存入 数组
    count <- 1L
    end_ <- arr[1, 2]  # 把 1L; end_ 小于 减 数组[1, 2] 存入 计数
    for (i in 2:nrow(arr)) {
        # for (下标 i in 2:nrow(数组)) {
        if (arr[i, 1] >= end_) {
            count <- count + 1L
            end_ <- arr[i, 2]
        }
    }
    nrow(arr) - count  # nrow(数组) 减 计数
}
m1 <- matrix(c(1, 2, 2, 3, 3, 4, 1, 3), ncol = 2, byrow = TRUE)
m3 <- matrix(c(1, 2, 1, 2, 1, 2), ncol = 2, byrow = TRUE)  # 把 矩阵(字符(1, 2, 1, 2, 1, 2), ncol 赋值为 2, byrow 赋值为 TRUE) 存入 m3
stopifnot(erase_overlap_intervals(m1) == 1L)  # 断言校验
stopifnot(erase_overlap_intervals(matrix(integer(0), ncol = 2)) == 0L)  # 断言校验
stopifnot(erase_overlap_intervals(m3) == 2L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
