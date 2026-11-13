# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440 LeetCode 215. 数组中的第K个最大元素
# — R 版（方案10） 定义函数 find_kth_largest（参数：数组, 下标 k）
find_kth_largest <- function(nums, k) {
    a <- nums  # 把 数组 存入 数组
    n <- length(a)  # 把 长度(数组) 存入 元素个数
    for (i in (n - 1):(n - k)) {
        # R 降序需守卫
        if (i < 1)
            break  # 若 下标 i 小于 1) break
        for (j in seq_len(i)) {
            # for (下标 j in seq_len(下标 i)) {
            if (a[j] > a[j + 1]) {
                t <- a[j]
                a[j] <- a[j + 1]
                a[j + 1] <- t
            }
        }
    }
    a[n - k + 1]  # 数组[元素个数 减 下标 k 加 1]
}
stopifnot(find_kth_largest(c(3, 2, 1, 5, 6, 4), 2) == 5)  # 断言校验
stopifnot(find_kth_largest(c(3, 2, 3, 1, 2, 4, 5, 5, 6), 4) == 4)  # 断言校验
stopifnot(find_kth_largest(c(1), 1) == 1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
