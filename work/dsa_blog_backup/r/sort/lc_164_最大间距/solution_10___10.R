# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135003383 LeetCode 164. 最大间距 — R
# 版（方案10） 定义函数 maximum_gap（参数：数组）
maximum_gap <- function(nums) {
    n <- length(nums)  # 把 长度(数组) 存入 元素个数
    if (n < 2L)
        return(0L)  # 若 元素个数 小于 2L) return(0L
    min_val <- min(nums)
    max_val <- max(nums)  # 把 取较小值 数组); max_val 小于 减 取较大值 数组) 存入 min_val
    if (min_val == max_val)
        return(0L)  # 若 min_val 等于 max_val) return(0L
    d <- max(1, (max_val - min_val)%/%(n - 1L))  # 把 取较大值 1, (max_val 减 min_val) 对…取模 除以 对…取模 (元素个数 减 1L)) 存入 d
    bucket_size <- (max_val - min_val)%/%d + 1L  # 把 (max_val 减 min_val) 对…取模 除以 对…取模 d 加 1L 存入 bucket_size
    buckets <- matrix(-1L, nrow = bucket_size, ncol = 2)  # 把 矩阵( 减 1L, nrow 赋值为 bucket_size, ncol 赋值为 2) 存入 buckets
    for (x in nums) {
        # for (x in 数组) {
        idx <- (x - min_val)%/%d + 1L  # 把 (x 减 min_val) 对…取模 除以 对…取模 d 加 1L 存入 idx
        if (buckets[idx, 1] == -1L) {
            # 若 buckets[idx, 1] 等于 减 1L
            buckets[idx, 1] <- x
            buckets[idx, 2] <- x  # buckets[idx, 1] 小于 减 x; buckets[idx, 2] 小于 减 x
        } else {
            # 否则
            if (x < buckets[idx, 1])
                buckets[idx, 1] <- x  # 若 x 小于 buckets[idx, 1]) buckets[idx, 1] 小于 减 x
            if (x > buckets[idx, 2])
                buckets[idx, 2] <- x  # 若 x 超过 buckets[idx, 2]) buckets[idx, 2] 小于 减 x
        }
    }
    ans <- 0L
    prev_max <- -1L  # 把 0L; prev_max 小于 减 减 1L 存入 答案
    for (i in seq_len(bucket_size)) {
        # for (下标 i in seq_len(bucket_size)) {
        if (buckets[i, 1] == -1L)
            next  # 若 buckets[下标 i, 1] 等于 减 1L) 下一个
        if (prev_max != -1L && buckets[i, 1] - prev_max > ans)
            ans <- buckets[i, 1] - prev_max
        prev_max <- buckets[i, 2]  # 把 buckets[下标 i, 2] 存入 prev_max
    }
    ans  # 答案
}
stopifnot(maximum_gap(c(1, 2, 3)) == 1)  # 断言校验
stopifnot(maximum_gap(c(3, 6, 9, 1)) == 3)  # 断言校验
stopifnot(maximum_gap(c(10)) == 0)  # 断言校验
stopifnot(maximum_gap(integer(0)) == 0)  # 断言校验
stopifnot(maximum_gap(c(1, 1e+07)) == 9999999)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
