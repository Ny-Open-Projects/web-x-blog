# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135949307 LeetCode 452.
# 用最少数量的箭引爆气球 — R 版（方案1） 定义函数 find_min_arrow_shots（参数：points）
find_min_arrow_shots <- function(points) {
    if (nrow(points) == 0)
        return(0L)  # 若 nrow(points) 等于 0) return(0L
    arr <- points[order(points[, 2]), , drop = FALSE]  # 把 points[order(points[, 2]), , drop 赋值为 FALSE] 存入 数组
    arrows <- 1L
    end_ <- arr[1, 2]  # 把 1L; end_ 小于 减 数组[1, 2] 存入 arrows
    for (k in 2:nrow(arr)) {
        # for (下标 k in 2:nrow(数组)) {
        if (arr[k, 1] > end_) {
            arrows <- arrows + 1L
            end_ <- arr[k, 2]
        }
    }
    arrows  # arrows
}
m1 <- matrix(c(10, 16, 2, 8, 1, 6, 7, 12), ncol = 2, byrow = TRUE)
m3 <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8), ncol = 2, byrow = TRUE)
stopifnot(find_min_arrow_shots(m1) == 2L)  # 断言校验
stopifnot(find_min_arrow_shots(matrix(integer(0), ncol = 2)) == 0L)  # 断言校验
stopifnot(find_min_arrow_shots(m3) == 4L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
