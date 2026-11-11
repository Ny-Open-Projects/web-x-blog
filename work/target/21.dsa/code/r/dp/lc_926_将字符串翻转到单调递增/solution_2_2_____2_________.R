# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130659442 LeetCode 926.
# 将字符串翻转到单调递增 — R 版（方案2） 定义函数 min_flips_mono_incr（参数：字符串）
min_flips_mono_incr <- function(s) {
    chars <- strsplit(s, "")[[1]]  # 把 strsplit(字符串, 「」)[[1]] 存入 chars
    ones <- 0L
    flips <- 0L  # 把 0L; flips 小于 减 0L 存入 ones
    for (c in chars) {
        # for (字符 in chars) { 否则
        if (c == "1")
            ones <- ones + 1L  # 若 字符 等于 「1」) ones 小于 减 ones 加 1L
 else {
            flips <- flips + 1L  # 把 flips 加 1L 存入 flips
            if (ones < flips)
                flips <- ones  # 若 ones 小于 flips) flips 小于 减 ones
        }
    }
    flips  # flips
}
stopifnot(min_flips_mono_incr("00110") == 1)  # 断言校验
stopifnot(min_flips_mono_incr("010110") == 2)  # 断言校验
stopifnot(min_flips_mono_incr("00011000") == 2)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
