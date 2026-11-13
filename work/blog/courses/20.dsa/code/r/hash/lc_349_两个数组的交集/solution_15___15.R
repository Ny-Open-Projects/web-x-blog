# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135064368 LeetCode 349. 两个数组的交集 — R
# 版（方案15） 定义函数 intersection_fn（参数：数组1, 数组2）
intersection_fn <- function(nums1, nums2) {
    seen <- integer(0)  # 把 integer(0) 存入 已见集合
    for (v in nums2) {
        # for (值 in 数组2) {
        if (v %in% nums1 && !(v %in% seen))
            seen <- c(seen, v)
    }
    seen  # 已见集合
}
stopifnot(identical(intersection_fn(c(1L, 2L, 2L, 1L), c(2L, 2L)), 2L))  # 断言校验
stopifnot(identical(intersection_fn(c(4L, 9L, 5L), c(9L, 4L, 9L, 8L, 4L)), c(9L, 4L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
