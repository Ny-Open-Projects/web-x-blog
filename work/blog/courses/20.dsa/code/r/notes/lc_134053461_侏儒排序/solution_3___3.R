# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134053461 数据结构与算法之排序: 侏儒排序 — R
# 版（方案3） 定义函数 gnome_sort（参数：数组）
gnome_sort <- function(nums) {
    v <- nums  # 把 数组 存入 值
    i <- 1L  # 把 1L 存入 下标 i
    while (i <= length(v)) {
        # 循环，直到不满足「下标 i 不超过 长度(值」
        if (i == 1L || v[i - 1L] <= v[i])
            i <- i + 1L  # 若 下标 i 等于 1L 或 值[下标 i 减 1L] 不超过 值[下标 i]) 下标 i 小于 减 下标 i 加 1L
 else {
            t <- v[i - 1L]
            v[i - 1L] <- v[i]
            v[i] <- t
            i <- i - 1L
        }  # 否则
    }
    v
}
stopifnot(identical(as.integer(gnome_sort(c(5, 4, 3, 2, 1))), 1:5))  # 断言校验
stopifnot(identical(as.integer(gnome_sort(c(3, 1, 2))), c(1L, 2L, 3L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
