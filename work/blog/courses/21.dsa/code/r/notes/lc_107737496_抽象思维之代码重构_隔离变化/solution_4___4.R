# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496 LeetCode 107737496.
# 代码重构_隔离变化 — R 版（方案4：螺旋矩阵方向模拟 placeFill） 定义函数 place_fill（参数：元素个数）
place_fill <- function(n) {
    m <- matrix(0L, nrow = n, ncol = n)  # 把 矩阵(0L, nrow 赋值为 元素个数, ncol 赋值为 元素个数) 存入 映射表
    row <- 1L
    col <- 1L  # 把 1L; col 小于 减 1L 存入 row
    direction <- "D"  # 把 「D」 存入 direction
    num <- 1L  # 把 1L 存入 num
    total <- n * n  # 把 元素个数 乘 元素个数 存入 总和
    while (num <= total) {
        # 循环，直到不满足「num 不超过 总和」
        m[row, col] <- num  # 映射表[row, col] 小于 减 num
        num <- num + 1L  # 把 num 加 1L 存入 num
        if (direction == "D") {
            # 若 direction 等于 「D」 若 row 加 1L 不超过 元素个数 且 映射表[row 加 1L, col] 等于 0L
            if (row + 1L <= n && m[row + 1L, col] == 0L) {
                row <- row + 1L  # 把 row 加 1L 存入 row
            } else {
                # 否则
                direction <- "R"
                col <- col + 1L  # 把 「R」; col 小于 减 col 加 1L 存入 direction
            }
        } else if (direction == "R") {
            # 否则，若 direction 等于 「R」 若 col 加 1L 不超过 元素个数 且 映射表[row, col 加 1L] 等于 0L
            if (col + 1L <= n && m[row, col + 1L] == 0L) {
                col <- col + 1L  # 把 col 加 1L 存入 col
            } else {
                # 否则
                direction <- "U"
                row <- row - 1L  # 把 「U」; row 小于 减 row 减 1L 存入 direction
            }
        } else if (direction == "U") {
            # 否则，若 direction 等于 「U」 若 row 减 1L 不低于 1L 且 映射表[row 减 1L, col] 等于 0L
            if (row - 1L >= 1L && m[row - 1L, col] == 0L) {
                row <- row - 1L  # 把 row 减 1L 存入 row
            } else {
                # 否则
                direction <- "L"
                col <- col - 1L  # 把 「L」; col 小于 减 col 减 1L 存入 direction
            }
        } else {
            # 否则 若 col 减 1L 不低于 1L 且 映射表[row, col 减 1L] 等于 0L
            if (col - 1L >= 1L && m[row, col - 1L] == 0L) {
                col <- col - 1L  # 把 col 减 1L 存入 col
            } else {
                # 否则
                direction <- "D"
                row <- row + 1L  # 把 「D」; row 小于 减 row 加 1L 存入 direction
            }
        }
    }
    m  # 映射表
}
got3 <- place_fill(3L)  # 把 place_fill(3L) 存入 got3
want3 <- matrix(c(1, 8, 7, 2, 9, 6, 3, 4, 5), nrow = 3, byrow = TRUE)
stopifnot(identical(as.integer(got3), as.integer(want3)))  # 断言校验
got4 <- place_fill(4L)  # 把 place_fill(4L) 存入 got4
want4 <- matrix(c(1, 12, 11, 10, 2, 13, 16, 9, 3, 14, 15, 8, 4, 5, 6, 7), nrow = 4, byrow = TRUE)
stopifnot(identical(as.integer(got4), as.integer(want4)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
