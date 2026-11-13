# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695 LeetCode 110240695. 分治策略之
# greatest slice — R 版（方案B：增量扫描） 定义函数 max_sub_array_ic（参数：数组）
max_sub_array_ic <- function(arr) {
    n <- length(arr)  # 把 长度(数组) 存入 元素个数
    if (n == 0L)
        return(0L)  # 若 元素个数 等于 0L) return(0L
    gs <- arr[1]  # 把 数组[1] 存入 gs
    for (i in 1:n) {
        # for (下标 i in 1:元素个数) {
        s <- 0L  # 把 0L 存入 字符串
        for (j in i:n) {
            # for (下标 j in 下标 i:元素个数) {
            s <- s + arr[j]  # 把 字符串 加 数组[下标 j] 存入 字符串
            if (gs < s)
                gs <- s  # 若 gs 小于 字符串) gs 小于 减 字符串
        }
    }
    as.integer(gs)  # as.integer(gs)
}
stopifnot(max_sub_array_ic(c(-2L, 1L, -3L, 4L, -1L, 2L, 1L)) == 6L)  # 断言校验
stopifnot(max_sub_array_ic(c(-1L, -2L, -3L)) == -1L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
