# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934 LeetCode 104107934. 滑动验证码识别
# — R 版（方案6：合成滑块数据 buildSynthetic） 定义函数 build_synthetic（参数：bg_len, gap_start,
# puzzle_len）
build_synthetic <- function(bg_len, gap_start, puzzle_len) {
    bg <- rep(10L, bg_len)  # 把 rep(10L, bg_len) 存入 bg
    for (i in (gap_start + 1L):min(gap_start + puzzle_len, bg_len)) {
        bg[i] <- 200L  # 把 200L 存入 bg[i]
    }
    puzzle <- bg[(gap_start + 1L):(gap_start + puzzle_len)]  # 把 bg[(gap_start 加 1L):(gap_start 加 puzzle_len)] 存入 puzzle
    list(bg, puzzle)  # 列表(bg, puzzle)
}
got <- build_synthetic(8L, 3L, 4L)  # 把 build_synthetic(8L, 3L, 4L) 存入 got
stopifnot(identical(as.integer(got[[1]]), as.integer(c(10, 10, 10, 200, 200, 200, 200, 10))))  # 断言校验
stopifnot(identical(as.integer(got[[2]]), as.integer(c(200, 200, 200, 200))))  # 断言校验
stopifnot(length(got[[2]]) == 4L)  # 断言校验
stopifnot(length(got[[1]]) == 8L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
