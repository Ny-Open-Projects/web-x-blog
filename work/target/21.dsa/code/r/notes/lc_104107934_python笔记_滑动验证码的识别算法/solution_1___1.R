# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934 LeetCode 104107934. 滑动验证码识别
# — R 版（方案1：前向差分边缘 + 匹配） 定义函数 detect_edges（参数：image）
detect_edges <- function(image) {
    edges <- rep(FALSE, length(image))  # 把 rep(FALSE, 长度(image)) 存入 边集
    for (i in 2:length(image)) {
        # for (下标 i in 2:长度(image)) {
        edges[i] <- abs(image[i] - image[i - 1L]) > 50  # 把 取绝对值 image[下标 i] 减 image[下标 i 减 1L]) 超过 50 存入 edges[i]
    }
    edges  # 边集
}
recognize_captcha <- function(bg, puzzle) {
    # 定义函数 recognize_captcha（参数：bg, puzzle）
    bg_edges <- detect_edges(bg)  # 把 detect_edges(bg) 存入 bg_edges
    puzzle_edges <- detect_edges(puzzle)  # 把 detect_edges(puzzle) 存入 puzzle_edges
    best_x <- 1L  # 把 1L 存入 best_x
    best_score <- -1L  # 把 减 1L 存入 best_score
    for (x in 1:(length(bg) - length(puzzle) + 1L)) {
        # for (x in 1:(长度(bg) 减 长度(puzzle) 加 1L)) {
        score <- 0L  # 把 0L 存入 score
        for (y in 1:length(puzzle)) {
            # for (y in 1:长度(puzzle)) {
            if (bg_edges[x + y - 1L] && puzzle_edges[y])
                score <- score + 1L
        }
        if (score > best_score) {
            # 若 score 超过 best_score
            best_score <- score  # 把 score 存入 best_score
            best_x <- x  # 把 x 存入 best_x
        }
    }
    as.integer(best_x - 1L)  # 0 基结果
}
bg <- c(10, 10, 10, 10, 200, 200, 200, 200)  # 把 字符(10, 10, 10, 10, 200, 200, 200, 200) 存入 bg
puzzle <- c(10, 200, 200, 200)  # 把 字符(10, 200, 200, 200) 存入 puzzle
stopifnot(recognize_captcha(bg, puzzle) == 3L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
