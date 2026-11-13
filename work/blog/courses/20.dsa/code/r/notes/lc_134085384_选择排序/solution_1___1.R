# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085384 数据结构与算法之排序: 选择排序 — R
# 版（方案1） 定义函数 selection_sort（参数：数组）
selection_sort <- function(nums) {
    v <- nums  # 把 数组 存入 值
    n <- length(v)  # 把 长度(值) 存入 元素个数
    for (i in 1:(n - 1)) {
        # for (下标 i in 1:(元素个数 减 1)) {
        m <- i  # 把 下标 i 存入 映射表
        for (j in (i + 1):n) if (v[j] < v[m])
            m <- j
        t <- v[i]
        v[i] <- v[m]
        v[m] <- t  # 把 值[下标 i]; 值[下标 i] 小于 减 值[映射表]; 值[映射表] 小于 减 另一字符串 存入 另一字符串
    }
    v
}
stopifnot(identical(as.integer(selection_sort(c(5, 4, 3, 2, 1))), 1:5))  # 断言校验
stopifnot(identical(as.integer(selection_sort(c(3, 1, 2))), c(1L, 2L, 3L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
