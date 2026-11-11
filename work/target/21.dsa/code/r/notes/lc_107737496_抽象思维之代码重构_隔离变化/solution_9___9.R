# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496 LeetCode 107737496.
# 代码重构_隔离变化 — R 版（方案9：规则串状态机，8 方向字母） 定义函数 Filler（参数：rn, cn）
Filler <- function(rn, cn) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$rowNum <- rn  # 把 rn 存入 e$rowNum
    e$colNum <- cn  # 把 cn 存入 e$colNum
    e$pos <- c(0L, 0L)  # 把 字符(0L, 0L) 存入 e$pos
    e$idx <- 0L  # 把 0L 存入 e$idx
    e$rMin <- 0L  # 把 0L 存入 e$rMin
    e$cMin <- 0L  # 把 0L 存入 e$cMin
    e$rMax <- rn - 1L  # 把 rn 减 1L 存入 e$rMax
    e$cMax <- cn - 1L  # 把 cn 减 1L 存入 e$cMax
    e$rule <- "ESVM"  # 把 「ESVM」 存入 e$rule
    class(e) <- "Filler"  # 把 「Filler」 存入 class(e)
    e
}
filler_set_rule <- function(f, rule) f$rule <- rule  # 定义函数 filler_set_rule（参数：f, rule）
filler_next <- function(f) {
    # 定义函数 filler_next（参数：f）
    res <- c(f$pos[1], f$pos[2])  # 把 字符(f$pos[1], f$pos[2]) 存入 结果
    ch <- substr(f$rule, f$idx%%nchar(f$rule) + 1L, f$idx%%nchar(f$rule) + 1L)
    if (ch == "E") {
        # 若 字符 等于 「E」
        f$pos[1] <- f$pos[1] + 1L  # 把 f$pos[1] 加 1L 存入 f$pos[1]
        if (f$pos[1] == f$rMax) {
            f$idx <- f$idx + 1L
            f$cMin <- f$cMin + 1L
        }
    } else if (ch == "S") {
        # 否则，若 字符 等于 「S」
        f$pos[2] <- f$pos[2] + 1L  # 把 f$pos[2] 加 1L 存入 f$pos[2]
        if (f$pos[2] == f$cMax) {
            f$idx <- f$idx + 1L
            f$rMax <- f$rMax - 1L
        }
    } else if (ch == "V") {
        # 否则，若 字符 等于 「V」
        f$pos[1] <- f$pos[1] - 1L  # 把 f$pos[1] 减 1L 存入 f$pos[1]
        if (f$pos[1] == f$rMin) {
            f$idx <- f$idx + 1L
            f$cMax <- f$cMax - 1L
        }
    } else if (ch == "M") {
        # 否则，若 字符 等于 「M」
        f$pos[2] <- f$pos[2] - 1L  # 把 f$pos[2] 减 1L 存入 f$pos[2]
        if (f$pos[2] == f$cMin) {
            f$idx <- f$idx + 1L
            f$rMin <- f$rMin + 1L
        }
    } else if (ch == "e") {
        # 否则，若 字符 等于 「e」
        f$pos[1] <- f$pos[1] + 1L  # 把 f$pos[1] 加 1L 存入 f$pos[1]
        if (f$pos[1] == f$rMax) {
            f$idx <- f$idx + 1L
            f$cMax <- f$cMax - 1L
        }
    } else if (ch == "s") {
        # 否则，若 字符 等于 「字符串」
        f$pos[2] <- f$pos[2] + 1L  # 把 f$pos[2] 加 1L 存入 f$pos[2]
        if (f$pos[2] == f$cMax) {
            f$idx <- f$idx + 1L
            f$rMin <- f$rMin + 1L
        }
    } else if (ch == "v") {
        # 否则，若 字符 等于 「值」
        f$pos[1] <- f$pos[1] - 1L  # 把 f$pos[1] 减 1L 存入 f$pos[1]
        if (f$pos[1] == f$rMin) {
            f$idx <- f$idx + 1L
            f$cMin <- f$cMin + 1L
        }
    } else if (ch == "m") {
        # 否则，若 字符 等于 「映射表」
        f$pos[2] <- f$pos[2] - 1L  # 把 f$pos[2] 减 1L 存入 f$pos[2]
        if (f$pos[2] == f$cMin) {
            f$idx <- f$idx + 1L
            f$rMax <- f$rMax - 1L
        }
    }
    res  # 结果
}
test_filler <- function(rule, rn, cn) {
    # 定义函数 test_filler（参数：rule, rn, cn）
    obj <- Filler(rn, cn)  # 把 Filler(rn, cn) 存入 obj
    filler_set_rule(obj, rule)  # filler_set_rule(obj, rule)
    seq <- list()  # 把 列表() 存入 seq
    for (i in 1:(rn * cn)) {
        # for (下标 i in 1:(rn 乘 cn)) {
        rc <- filler_next(obj)  # 把 filler_next(obj) 存入 rc
        seq[[i]] <- as.integer(rc)  # 把 as.integer(rc) 存入 seq[[i]]
    }
    seq  # seq
}
want_esvm <- list(c(0, 0), c(1, 0), c(2, 0), c(3, 0), c(3, 1), c(3, 2), c(3, 3), c(2, 3), c(1, 3), c(0, 3), c(0,
    2), c(0, 1), c(1, 1), c(2, 1), c(2, 2), c(1, 2))
got <- test_filler("ESVM", 4L, 4L)  # 把 test_filler(「ESVM」, 4L, 4L) 存入 got
for (i in 1:16) stopifnot(identical(got[[i]], as.integer(want_esvm[[i]])))  # 断言校验
want_semv <- list(c(0, 0), c(0, 1), c(0, 2), c(0, 3), c(1, 3), c(2, 3), c(3, 3), c(3, 2), c(3, 1), c(3, 0), c(2,
    0), c(1, 0), c(1, 1), c(1, 2), c(2, 2), c(2, 1))
got <- test_filler("semv", 4L, 4L)  # 把 test_filler(「semv」, 4L, 4L) 存入 got
for (i in 1:16) stopifnot(identical(got[[i]], as.integer(want_semv[[i]])))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
