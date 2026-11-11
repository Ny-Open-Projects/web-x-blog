# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496 LeetCode 107737496.
# 代码重构_隔离变化 — R 版（方案10：Filler+Matrix 组合 9x9 全螺旋） 定义函数 Filler（参数：rn, cn）
Filler <- function(rn, cn) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$pos <- c(0L, 0L)  # 把 字符(0L, 0L) 存入 e$pos
    e$idx <- 0L  # 把 0L 存入 e$idx
    e$rMin <- 0L  # 把 0L 存入 e$rMin
    e$cMin <- 0L  # 把 0L 存入 e$cMin
    e$rMax <- rn - 1L  # 把 rn 减 1L 存入 e$rMax
    e$cMax <- cn - 1L  # 把 cn 减 1L 存入 e$cMax
    class(e) <- "Filler"  # 把 「Filler」 存入 class(e)
    e
}
filler_next <- function(f) {
    # 定义函数 filler_next（参数：f）
    res <- c(f$pos[1], f$pos[2])  # 把 字符(f$pos[1], f$pos[2]) 存入 结果
    cmd <- substr("ESVM", f$idx%%4L + 1L, f$idx%%4L + 1L)
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
    res  # 结果
}
fmt_row <- function(row) paste(sprintf("%2d", row), collapse = " ")  # 定义函数 fmt_row（参数：row）
rn <- 9L
cn <- 9L  # 把 9L; cn 小于 减 9L 存入 rn
obj <- Filler(rn, cn)  # 把 Filler(rn, cn) 存入 obj
m <- matrix(0L, nrow = rn, ncol = cn)  # 把 矩阵(0L, nrow 赋值为 rn, ncol 赋值为 cn) 存入 映射表
for (i in 1:(rn * cn)) {
    # for (下标 i in 1:(rn 乘 cn)) {
    rc <- filler_next(obj)  # 把 filler_next(obj) 存入 rc
    m[rc[1] + 1L, rc[2] + 1L] <- i  # 映射表[rc[1] 加 1L, rc[2] 加 1L] 小于 减 下标 i
}
want <- c(" 1 32 31 30 29 28 27 26 25", " 2 33 56 55 54 53 52 51 24", " 3 34 57 72 71 70 69 50 23", " 4 35 58 73 80 79 68 49 22",
    " 5 36 59 74 81 78 67 48 21", " 6 37 60 75 76 77 66 47 20", " 7 38 61 62 63 64 65 46 19", " 8 39 40 41 42 43 44 45 18",
    " 9 10 11 12 13 14 15 16 17"  # 「 9 10 11 12 13 14 15 16 17」
)
for (i in 1:rn) {
    # for (下标 i in 1:rn) {
    got <- fmt_row(m[i, ])  # 把 fmt_row(映射表[下标 i, ]) 存入 got
    stopifnot(identical(got, want[i]))  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
