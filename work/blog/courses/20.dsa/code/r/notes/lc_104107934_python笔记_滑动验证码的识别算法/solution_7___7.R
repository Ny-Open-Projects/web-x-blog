# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934 LeetCode 104107934. 滑动验证码识别
# — R 版（方案7：合成数据 + 识别全流程） 定义函数 detect_edges（参数：image）
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
    as.integer(best_x - 1L)  # as.integer(best_x 减 1L)
}
build_synthetic <- function(bg_len, gap_start, puzzle_len) {
    # 定义函数 build_synthetic（参数：bg_len, gap_start, puzzle_len）
    bg <- rep(10L, bg_len)  # 把 rep(10L, bg_len) 存入 bg
    for (i in (gap_start + 1L):min(gap_start + puzzle_len, bg_len)) {
        bg[i] <- 200L  # 把 200L 存入 bg[i]
    }
    puzzle <- bg[(gap_start + 1L):(gap_start + puzzle_len)]  # 把 bg[(gap_start 加 1L):(gap_start 加 puzzle_len)] 存入 puzzle
    list(bg, puzzle)  # 列表(bg, puzzle)
}
got <- build_synthetic(8L, 3L, 4L)  # 把 build_synthetic(8L, 3L, 4L) 存入 got
# 与 TS 原文件一致：合成数据下 puzzle 边缘全平，识别结果为 0
stopifnot(recognize_captcha(got[[1]], got[[2]]) == 0L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
