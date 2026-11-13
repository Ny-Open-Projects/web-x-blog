# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695 LeetCode 110240695. 分治策略之
# greatest slice — R 版（方案C：分治 best/prefix/suffix/total） 定义函数 max_sub_array_dc（参数：数组）
max_sub_array_dc <- function(arr) {
    n <- length(arr)  # 把 长度(数组) 存入 元素个数
    if (n == 0L)
        return(0L)  # 若 元素个数 等于 0L) return(0L
    helper <- function(lo, hi) {
        # 定义函数 helper（参数：左边界, 右边界） 若 右边界 减 左边界 等于 1L
        if (hi - lo == 1L) {
            v <- as.integer(arr[lo + 1L])  # lo 为 0 基
            return(c(v, v, v, v))  # 返回 字符(值, 值, 值, 值
        }
        mi <- as.integer((lo + hi)%/%2L)  # 把 as.integer((左边界 加 右边界) 对…取模 除以 对…取模 2L) 存入 mi
        l <- helper(lo, mi)  # 把 helper(左边界, mi) 存入 左指针
        r <- helper(mi, hi)  # 把 helper(mi, 右边界) 存入 右指针
        crossing <- l[3] + r[2]  # 把 左指针[3] 加 右指针[2] 存入 crossing
        best <- max(l[1], r[1], crossing)  # 把 取较大值 左指针[1], 右指针[1], crossing) 存入 当前最优
        prefix <- max(l[2], l[4] + r[2])  # 把 取较大值 左指针[2], 左指针[4] 加 右指针[2]) 存入 prefix
        suffix <- max(r[3], r[4] + l[3])  # 把 取较大值 右指针[3], 右指针[4] 加 左指针[3]) 存入 suffix
        total <- l[4] + r[4]  # 把 左指针[4] 加 右指针[4] 存入 总和
        c(best, prefix, suffix, total)  # 字符(当前最优, prefix, suffix, 总和)
    }
    helper(0L, n)[1]  # helper(0L, 元素个数)[1]
}
stopifnot(max_sub_array_dc(c(-2L, 1L, -3L, 4L, -1L, 2L, 1L)) == 6L)  # 断言校验
stopifnot(max_sub_array_dc(c(1L, 2L, 3L)) == 6L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
