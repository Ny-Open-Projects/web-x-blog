# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934 LeetCode 104107934. 滑动验证码识别
# — R 版（方案4：SAD 绝对差和最佳窗口） 定义函数 best_match_window（参数：bg, puzzle）
best_match_window <- function(bg, puzzle) {
    best_x <- 1L  # 把 1L 存入 best_x
    best_score <- Inf  # 把 Inf 存入 best_score
    n <- length(puzzle)  # 把 长度(puzzle) 存入 元素个数
    for (x in 1:(length(bg) - n + 1L)) {
        # for (x in 1:(长度(bg) 减 元素个数 加 1L)) {
        score <- 0  # 把 0 存入 score
        for (y in 0:(n - 1L)) {
            # for (y in 0:(元素个数 减 1L)) {
            score <- score + abs(bg[x + y] - puzzle[y + 1L])  # 把 score 加 取绝对值 bg[x 加 y] 减 puzzle[y 加 1L]) 存入 score
        }
        if (score < best_score) {
            # 若 score 小于 best_score
            best_score <- score  # 把 score 存入 best_score
            best_x <- x  # 把 x 存入 best_x
        }
    }
    c(as.integer(best_x - 1L), as.integer(best_score))  # 字符(as.integer(best_x 减 1L), as.integer(best_score))
}
bg <- c(10, 10, 10, 10, 200, 200, 200, 200)  # 把 字符(10, 10, 10, 10, 200, 200, 200, 200) 存入 bg
puzzle <- c(10, 200, 200, 200)  # 把 字符(10, 200, 200, 200) 存入 puzzle
got <- best_match_window(bg, puzzle)  # 把 best_match_window(bg, puzzle) 存入 got
stopifnot(got[1] == 3L && got[2] == 0L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
