# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145568435 LeetCode 350. 两个数组的交集 II — R
# 版（方案1） 定义函数 intersect_fn（参数：数组1, 数组2）
intersect_fn <- function(nums1, nums2) {
    a <- if (length(nums1) <= length(nums2))
        nums1 else nums2  # 把 if (长度(数组1) 不超过 长度(数组2)) 数组1 else 数组2 存入 数组
    b <- if (length(nums1) <= length(nums2))
        nums2 else nums1  # 把 if (长度(数组1) 不超过 长度(数组2)) 数组2 else 数组1 存入 b
    used <- rep(FALSE, length(a))  # 把 rep(FALSE, 长度(数组)) 存入 已用标记
    res <- integer(0)  # 把 integer(0) 存入 结果
    for (v in b) {
        # for (值 in b) { for (下标 k in seq_along(数组)) { 若 取反 已用标记[下标 k] 且 数组[下标 k] 等于 值
        for (k in seq_along(a)) {
            if (!used[k] && a[k] == v) {
                used[k] <- TRUE  # 把 TRUE 存入 used[k]
                res <- c(res, v)  # 把 字符(结果, 值) 存入 结果
                break  # 跳出循环
            }
        }
    }
    res  # 结果
}
stopifnot(identical(intersect_fn(c(1L, 2L, 2L, 1L), c(2L, 2L)), c(2L, 2L)))  # 断言校验
stopifnot(identical(intersect_fn(c(4L, 9L, 5L), c(9L, 4L, 9L, 8L, 4L)), c(9L, 4L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
