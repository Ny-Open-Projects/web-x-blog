# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496 LeetCode 107737496.
# 代码重构_隔离变化 — R 版（方案11：Rule 循环游标） 定义函数 Rule（参数：右指针）
Rule <- function(r) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$data <- strsplit(r, "")[[1]]  # 把 strsplit(右指针, 「」)[[1]] 存入 e$data
    e$idx <- 1L  # 把 1L 存入 e$idx
    e$len <- nchar(r)  # 把 nchar(右指针) 存入 e$len
    class(e) <- "Rule"  # 把 「Rule」 存入 class(e)
    e
}
rule_next <- function(r) {
    # 定义函数 rule_next（参数：右指针）
    ch <- r$data[r$idx]  # 把 右指针$data[右指针$idx] 存入 字符
    r$idx <- (r$idx - 1L + 1L)%%r$len + 1L  # 把 (右指针$idx 减 1L 加 1L) 对…取模 对…取模 右指针$长度 加 1L 存入 r$idx
    ch  # 字符
}
r <- Rule("ESVM")  # 把 Rule(「ESVM」) 存入 右指针
s1 <- paste(replicate(10L, rule_next(r)), collapse = "")
r2 <- Rule("semv")  # 把 Rule(「semv」) 存入 r2
s2 <- paste(replicate(6L, rule_next(r2)), collapse = "")  # 把 paste(replicate(6L, rule_next(r2)), collapse 赋值为 「」) 存入 s2
stopifnot(identical(s1, "ESVMESVMES"))  # 断言校验
stopifnot(identical(s2, "semvse"))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
