# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496 LeetCode 107737496.
# 代码重构_隔离变化 — R 版（方案12：Location/Rule/Filler 组合） 定义函数 Rule（参数：右指针）
Rule <- function(r) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$data <- r  # 把 右指针 存入 e$data
    e$idx <- 1L  # 把 1L 存入 e$idx
    e$len <- nchar(r)  # 把 nchar(右指针) 存入 e$len
    class(e) <- "Rule"  # 把 「Rule」 存入 class(e)
    e
}
rule_current <- function(r) substr(r$data, r$idx, r$idx)  # 定义函数 rule_current（参数：右指针）
rule_advance <- function(r) r$idx <- (r$idx - 1L + 1L)%%r$len + 1L  # 定义函数 rule_advance（参数：右指针）
Filler <- function(rn, cn, rule) {
    # 定义函数 Filler（参数：rn, cn, rule）
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$pos <- c(0L, 0L)  # 把 字符(0L, 0L) 存入 e$pos
    e$rMin <- 0L  # 把 0L 存入 e$rMin
    e$cMin <- 0L  # 把 0L 存入 e$cMin
    e$rMax <- rn - 1L  # 把 rn 减 1L 存入 e$rMax
    e$cMax <- cn - 1L  # 把 cn 减 1L 存入 e$cMax
    e$cmd <- Rule(rule)  # 把 Rule(rule) 存入 e$cmd
    class(e) <- "Filler"  # 把 「Filler」 存入 class(e)
    e
}
filler_next <- function(f) {
    # 定义函数 filler_next（参数：f）
    res <- c(f$pos[1], f$pos[2])  # 把 字符(f$pos[1], f$pos[2]) 存入 结果
    ch <- rule_current(f$cmd)  # 把 rule_current(f$cmd) 存入 字符
    if (ch == "E") {
        # 若 字符 等于 「E」
        f$pos[1] <- f$pos[1] + 1L  # 把 f$pos[1] 加 1L 存入 f$pos[1]
        if (f$pos[1] == f$rMax) {
            rule_advance(f$cmd)
            f$cMin <- f$cMin + 1L
        }
    } else if (ch == "S") {
        # 否则，若 字符 等于 「S」
        f$pos[2] <- f$pos[2] + 1L  # 把 f$pos[2] 加 1L 存入 f$pos[2]
        if (f$pos[2] == f$cMax) {
            rule_advance(f$cmd)
            f$rMax <- f$rMax - 1L
        }
    } else if (ch == "V") {
        # 否则，若 字符 等于 「V」
        f$pos[1] <- f$pos[1] - 1L  # 把 f$pos[1] 减 1L 存入 f$pos[1]
        if (f$pos[1] == f$rMin) {
            rule_advance(f$cmd)
            f$cMax <- f$cMax - 1L
        }
    } else if (ch == "M") {
        # 否则，若 字符 等于 「M」
        f$pos[2] <- f$pos[2] - 1L  # 把 f$pos[2] 减 1L 存入 f$pos[2]
        if (f$pos[2] == f$cMin) {
            rule_advance(f$cmd)
            f$rMin <- f$rMin + 1L
        }
    }
    res  # 结果
}
obj <- Filler(4L, 4L, "ESVM")  # 把 Filler(4L, 4L, 「ESVM」) 存入 obj
want <- list(c(0, 0), c(1, 0), c(2, 0), c(3, 0), c(3, 1), c(3, 2), c(3, 3), c(2, 3), c(1, 3), c(0, 3), c(0, 2),
    c(0, 1), c(1, 1), c(2, 1), c(2, 2), c(1, 2))
for (i in 1:16) {
    # for (下标 i in 1:16) {
    rc <- as.integer(filler_next(obj))  # 把 as.integer(filler_next(obj)) 存入 rc
    stopifnot(identical(rc, as.integer(want[[i]])))  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
