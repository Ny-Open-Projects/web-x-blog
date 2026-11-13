# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496 LeetCode 107737496.
# 代码重构_隔离变化 — R 版（方案8：Filler 状态机 + hasNext 部分填充） 定义函数 Filler（参数：rn, cn）
Filler <- function(rn, cn) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$rowNum <- rn  # 把 rn 存入 e$rowNum
    e$colNum <- cn  # 把 cn 存入 e$colNum
    e$rule <- "ESVM"  # 把 「ESVM」 存入 e$rule
    e$pos <- c(0L, 0L)  # 0 基
    e$idx <- 0L  # 把 0L 存入 e$idx
    e$rMin <- 0L  # 把 0L 存入 e$rMin
    e$cMin <- 0L  # 把 0L 存入 e$cMin
    e$rMax <- rn - 1L  # 把 rn 减 1L 存入 e$rMax
    e$cMax <- cn - 1L  # 把 cn 减 1L 存入 e$cMax
    class(e) <- "Filler"  # 把 「Filler」 存入 class(e)
    e
}
filler_set_rule <- function(f, r) f$rule <- r  # 定义函数 filler_set_rule（参数：f, 右指针）
filler_has_next <- function(f) {
    # 定义函数 filler_has_next（参数：f）
    f$rMin <= f$pos[1] && f$pos[1] <= f$rMax && f$cMin <= f$pos[2] && f$pos[2] <= f$cMax  # 把 f$pos[2] 且 f$pos[2] 不超过 f$cMax 写入 f$cMin <
}
filler_next <- function(f) {
    # 定义函数 filler_next（参数：f）
    r <- f$pos[1]  # 把 f$pos[1] 存入 右指针
    c <- f$pos[2]  # 把 f$pos[2] 存入 字符
    cmd <- substr(f$rule, f$idx%%4L + 1L, f$idx%%4L + 1L)
    if (cmd == "E") {
        # 若 cmd 等于 「E」
        f$pos[1] <- f$pos[1] + 1L  # 把 f$pos[1] 加 1L 存入 f$pos[1]
        if (f$pos[1] == f$rMax) {
            f$idx <- f$idx + 1L
            f$cMin <- f$cMin + 1L
        }
    } else if (cmd == "S") {
        # 否则，若 cmd 等于 「S」
        f$pos[2] <- f$pos[2] + 1L  # 把 f$pos[2] 加 1L 存入 f$pos[2]
        if (f$pos[2] == f$cMax) {
            f$idx <- f$idx + 1L
            f$rMax <- f$rMax - 1L
        }
    } else if (cmd == "V") {
        # 否则，若 cmd 等于 「V」
        f$pos[1] <- f$pos[1] - 1L  # 把 f$pos[1] 减 1L 存入 f$pos[1]
        if (f$pos[1] == f$rMin) {
            f$idx <- f$idx + 1L
            f$cMax <- f$cMax - 1L
        }
    } else if (cmd == "M") {
        # 否则，若 cmd 等于 「M」
        f$pos[2] <- f$pos[2] - 1L  # 把 f$pos[2] 减 1L 存入 f$pos[2]
        if (f$pos[2] == f$cMin) {
            f$idx <- f$idx + 1L
            f$rMin <- f$rMin + 1L
        }
    }
    c(r, c)  # 字符(右指针, 字符)
}
fill_matrix <- function(rn, cn, rule) {
    # 定义函数 fill_matrix（参数：rn, cn, rule）
    mat <- matrix(0L, nrow = rn, ncol = cn)  # 把 矩阵(0L, nrow 赋值为 rn, ncol 赋值为 cn) 存入 mat
    f <- Filler(rn, cn)  # 把 Filler(rn, cn) 存入 f
    filler_set_rule(f, rule)  # filler_set_rule(f, rule)
    i <- 1L  # 把 1L 存入 下标 i
    while (filler_has_next(f)) {
        # 循环，直到不满足「filler_has_next(f」
        rc <- filler_next(f)  # 把 filler_next(f) 存入 rc
        mat[rc[1] + 1L, rc[2] + 1L] <- i  # mat[rc[1] 加 1L, rc[2] 加 1L] 小于 减 下标 i
        i <- i + 1L  # 把 下标 i 加 1L 存入 下标 i
    }
    mat  # mat
}
got1 <- fill_matrix(6L, 6L, "ESVM")  # 把 fill_matrix(6L, 6L, 「ESVM」) 存入 got1
want1 <- matrix(c(1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0), nrow = 6, byrow = TRUE)
stopifnot(identical(as.integer(got1), as.integer(want1)))  # 断言校验
got2 <- fill_matrix(3L, 3L, "ESVM")  # 把 fill_matrix(3L, 3L, 「ESVM」) 存入 got2
want2 <- matrix(c(1, 0, 0, 2, 0, 0, 0, 0, 0), nrow = 3, byrow = TRUE)
stopifnot(identical(as.integer(got2), as.integer(want2)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
