# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134150438 数据结构与算法之排序: 希尔排序 — R
# 版（方案2） 定义函数 shell_sort（参数：数组）
shell_sort <- function(nums) {
    v <- nums  # 把 数组 存入 值
    n <- length(v)  # 把 长度(值) 存入 元素个数
    gap <- n%/%2  # 把 元素个数 对…取模 除以 对…取模 2 存入 gap
    while (gap > 0) {
        # 循环，直到不满足「gap 超过 0」 for (下标 i in (gap 加 1):元素个数) {
        for (i in (gap + 1):n) {
            key <- v[i]  # 把 值[下标 i] 存入 key
            j <- i - gap  # 把 下标 i 减 gap 存入 下标 j
            while (j >= 1 && v[j] > key) {
                v[j + gap] <- v[j]
                j <- j - gap
            }
            v[j + gap] <- key  # 值[下标 j 加 gap] 小于 减 key
        }
        gap <- gap%/%2  # 把 gap 对…取模 除以 对…取模 2 存入 gap
    }
    v
}
stopifnot(identical(as.integer(shell_sort(c(5, 2, 4, 6, 1, 3))), 1:6))  # 断言校验
stopifnot(identical(as.integer(shell_sort(c(9, 8, 7, 6, 5, 4, 3, 2, 1))), 1:9))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
