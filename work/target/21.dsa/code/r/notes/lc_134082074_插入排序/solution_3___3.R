# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134082074 数据结构与算法之排序: 插入排序 — R
# 版（方案3） 定义函数 insertion_sort（参数：数组）
insertion_sort <- function(nums) {
    v <- nums  # 把 数组 存入 值
    for (i in 2:length(v)) {
        # for (下标 i in 2:长度(值)) {
        key <- v[i]  # 把 值[下标 i] 存入 key
        j <- i - 1  # 把 下标 i 减 1 存入 下标 j
        while (j >= 1 && v[j] > key) {
            v[j + 1] <- v[j]
            j <- j - 1
        }
        v[j + 1] <- key  # 值[下标 j 加 1] 小于 减 key
    }
    v
}
stopifnot(identical(as.integer(insertion_sort(c(5, 4, 3, 2, 1))), 1:5))  # 断言校验
stopifnot(identical(as.integer(insertion_sort(c(3, 1, 2))), c(1L, 2L, 3L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
