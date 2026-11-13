# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066237 数据结构与算法之排序: 冒泡排序 — R
# 版（方案9） 定义函数 gnome_sort_bubble（参数：数组）
gnome_sort_bubble <- function(nums) {
    v <- nums  # 把 数组 存入 值
    n <- length(v)  # 把 长度(值) 存入 元素个数
    if (n >= 2) {
        # 若 元素个数 不低于 2 for (下标 i in seq_len(元素个数 减 1)) { for (下标 j in 1:(元素个数 减 下标
        # i)) {
        for (i in seq_len(n - 1)) {
            for (j in 1:(n - i)) {
                if (v[j] > v[j + 1]) {
                  t <- v[j]
                  v[j] <- v[j + 1]
                  v[j + 1] <- t
                }
            }
        }
    }
    v
}
stopifnot(identical(as.integer(gnome_sort_bubble(c(5, 4, 3, 2, 1))), 1:5))  # 断言校验
stopifnot(identical(as.integer(gnome_sort_bubble(c(3, 1, 2))), c(1L, 2L, 3L)))  # 断言校验
stopifnot(length(gnome_sort_bubble(integer(0))) == 0)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
