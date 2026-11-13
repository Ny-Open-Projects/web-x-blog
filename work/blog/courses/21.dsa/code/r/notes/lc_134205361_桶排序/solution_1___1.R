# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134205361 数据结构与算法之排序: 桶排序 — R
# 版（方案1） 定义函数 get_index（参数：数组, 下标 k）
get_index <- function(arr, k) {
    if (k %in% arr)
        as.integer(k) else -1L  # 若 下标 k 对…取模 in 对…取模 数组) as.integer(下标 k) else 减 1L
}
stopifnot(get_index(c(1, 2, 3), 1) == 1)  # 断言校验
stopifnot(get_index(c(1, 2, 3), 3) == 3)  # 断言校验
stopifnot(get_index(c(1, 2, 3), 5) == -1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
