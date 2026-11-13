# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134026430 LeetCode 54. 螺旋矩阵 — R 版
# 四边界逐层收缩（1 基下标，与 TS 事实源逻辑一致） 注意：R 的 a:b 在 a>b 时生成降序序列，故每处循环都加与 TS
# 零次迭代等价的守卫 定义函数 spiral_order（参数：mat）
spiral_order <- function(mat) {
    if (is.null(mat) || length(mat) == 0 || length(mat[[1]]) == 0)
        return(integer(0))
    result <- integer(0)  # 把 integer(0) 存入 结果
    top <- 1L  # 把 1L 存入 top
    bottom <- length(mat)  # 把 长度(mat) 存入 bottom
    left <- 1L  # 把 1L 存入 左边界
    right <- length(mat[[1]])  # 把 长度(mat[[1]]) 存入 右边界
    while (top <= bottom && left <= right) {
        # 循环，直到不满足「top 不超过 bottom 且 左边界 不超过 右边界」
        if (left <= right)
            for (i in left:right) result <- c(result, mat[[top]][i])
        top <- top + 1L  # 把 top 加 1L 存入 top
        if (top <= bottom)
            for (i in top:bottom) result <- c(result, mat[[i]][right])
        right <- right - 1L  # 把 右边界 减 1L 存入 右边界
        if (top <= bottom) {
            # 若 top 不超过 bottom
            if (right >= left)
                for (i in right:left) result <- c(result, mat[[bottom]][i])
            bottom <- bottom - 1L  # 把 bottom 减 1L 存入 bottom
        }
        if (left <= right) {
            # 若 左边界 不超过 右边界
            if (bottom >= top)
                for (i in bottom:top) result <- c(result, mat[[i]][left])
            left <- left + 1L  # 把 左边界 加 1L 存入 左边界
        }
    }
    result  # 结果
}
# 自测：与 TS 事实源内嵌用例一致（3x3 螺旋）
mat <- list(c(1L, 2L, 3L), c(4L, 5L, 6L), c(7L, 8L, 9L))  # 把 列表(字符(1L, 2L, 3L), 字符(4L, 5L, 6L), 字符(7L, 8L, 9L)) 存入 mat
exp <- c(1L, 2L, 3L, 6L, 9L, 8L, 7L, 4L, 5L)  # 把 字符(1L, 2L, 3L, 6L, 9L, 8L, 7L, 4L, 5L) 存入 exp
got <- spiral_order(mat)  # 把 spiral_order(mat) 存入 got
stopifnot(identical(as.integer(got), exp))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
