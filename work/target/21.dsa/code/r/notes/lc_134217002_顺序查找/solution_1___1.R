# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134217002 数据结构与算法之查找: 顺序查找 — R
# 版（方案1） 定义函数 seq_search（参数：数组, key）
seq_search <- function(arr, key) {
    w <- which(arr == key)  # 把 which(数组 等于 key) 存入 权重
    if (length(w) == 0)
        -1L else as.integer(w[1] - 1L)  # 若 长度(权重) 等于 0) 减 1L else as.integer(权重[1] 减 1L
}
stopifnot(seq_search(c(1, 2, 3), 1) == 0)  # 断言校验
stopifnot(seq_search(c(1, 2, 3), 2) == 1)  # 断言校验
stopifnot(seq_search(c(1, 2, 3), 4) == -1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
