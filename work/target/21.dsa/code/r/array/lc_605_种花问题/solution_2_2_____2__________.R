# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134638462 LeetCode 605. 种花问题 — R
# 版（方案2） 定义函数 can_place_flowers（参数：bed, 元素个数）
can_place_flowers <- function(bed, n) {
    v <- bed  # 把 bed 存入 值
    count <- 0  # 把 0 存入 计数
    for (i in seq_along(v)) {
        # for (下标 i in seq_along(值)) {
        if (v[i] == 0 && (i == 1 || v[i - 1] == 0) && (i == length(v) || v[i + 1] == 0)) {
            v[i] <- 1  # 把 1 存入 v[i]
            count <- count + 1  # 把 计数 加 1 存入 计数
        }
    }
    count >= n  # 把 元素个数 写入 count >
}
stopifnot(can_place_flowers(c(1, 0, 0, 0, 1), 1))  # 断言校验
stopifnot(!can_place_flowers(c(1, 0, 0, 0, 1), 2))  # 断言校验
stopifnot(can_place_flowers(c(0, 0, 1, 0, 0), 1))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
