# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934 LeetCode 104107934. 滑动验证码识别
# — R 版（方案3：NCC 归一化互相关） 定义函数 ncc_match（参数：bg, puzzle）
ncc_match <- function(bg, puzzle) {
    best_x <- 1L  # 把 1L 存入 best_x
    best_score <- -Inf  # 把 减 Inf 存入 best_score
    n <- length(puzzle)  # 把 长度(puzzle) 存入 元素个数
    for (x in 1:(length(bg) - n + 1L)) {
        # for (x in 1:(长度(bg) 减 元素个数 加 1L)) {
        window <- bg[x:(x + n - 1L)]  # 把 bg[x:(x 加 元素个数 减 1L)] 存入 window
        bw <- mean(window)  # 把 mean(window) 存入 bw
        pw <- mean(puzzle)  # 把 mean(puzzle) 存入 pw
        num <- 0
        db <- 0
        dp <- 0  # 把 0; db 小于 减 0; DP 表 小于 减 0 存入 num
        for (i in 1:n) {
            # for (下标 i in 1:元素个数) {
            a <- window[i] - bw  # 把 window[下标 i] 减 bw 存入 数组
            b <- puzzle[i] - pw  # 把 puzzle[下标 i] 减 pw 存入 b
            num <- num + a * b  # 把 num 加 数组 乘 b 存入 num
            db <- db + a * a  # 把 db 加 数组 乘 数组 存入 db
            dp <- dp + b * b  # 把 DP 表 加 b 乘 b 存入 DP 表
        }
        denom <- sqrt(db) * sqrt(dp)  # 把 sqrt(db) 乘 sqrt(DP 表) 存入 denom
        score <- if (denom != 0)
            num/denom else 0  # 把 if (denom 不等于 0) num 除以 denom else 0 存入 score
        if (score > best_score) {
            # 若 score 超过 best_score
            best_score <- score  # 把 score 存入 best_score
            best_x <- x  # 把 x 存入 best_x
        }
    }
    as.integer(best_x - 1L)  # as.integer(best_x 减 1L)
}
bg <- c(10, 10, 10, 10, 200, 200, 200, 200)  # 把 字符(10, 10, 10, 10, 200, 200, 200, 200) 存入 bg
puzzle <- c(10, 200, 200, 200)  # 把 字符(10, 200, 200, 200) 存入 puzzle
stopifnot(ncc_match(bg, puzzle) == 3L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
