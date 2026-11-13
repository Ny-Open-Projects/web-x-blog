# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726 LeetCode 107431726. 最大红矩形分析
# — R 版（方案A：逐行高度 + 暴力区间 / 卡片扩展） 定义函数 get_result（参数：元素个数, 映射表, 矩阵）
get_result <- function(n, m, matrix) {
    ans <- 0  # 把 0 存入 答案
    height <- rep(0L, m + 2L)  # 把 rep(0L, 映射表 加 2L) 存入 height
    for (k in 1:n) {
        # for (下标 k in 1:元素个数) { for (下标 i in 1:映射表) {
        for (i in 1:m) {
            if (substr(matrix[k], i, i) == ".")
                height[i] <- height[i] + 1L else height[i] <- 0L
        }
        for (a in 1:m) {
            # for (数组 in 1:映射表) {
            min_h <- 50000L  # 把 50000L 存入 min_h
            for (c in a:m) if (height[c] < min_h)
                min_h <- height[c]
            area <- (m - a + 1L) * min_h  # 把 (映射表 减 数组 加 1L) 乘 min_h 存入 area
            if (area > ans)
                ans <- area  # 若 area 超过 答案) 答案 小于 减 area
        }
    }
    ans  # 答案
}
get_result_card <- function(n, m, matrix) {
    # 定义函数 get_result_card（参数：元素个数, 映射表, 矩阵）
    ans <- 0  # 把 0 存入 答案
    height <- rep(0L, m + 2L)  # 把 rep(0L, 映射表 加 2L) 存入 height
    for (k in 1:n) {
        # for (下标 k in 1:元素个数) { for (下标 i in 1:映射表) {
        for (i in 1:m) {
            if (substr(matrix[k], i, i) == ".")
                height[i] <- height[i] + 1L else height[i] <- 0L
        }
        for (a in 1:m) {
            # for (数组 in 1:映射表) {
            cur_h <- height[a]  # 把 height[数组] 存入 cur_h
            lo <- a - 1L  # 把 数组 减 1L 存入 左边界
            while (lo >= 1L && height[lo] >= cur_h) lo <- lo - 1L
            hi <- a + 1L  # 把 数组 加 1L 存入 右边界
            while (hi <= m && height[hi] >= cur_h) hi <- hi + 1L
            area <- (hi - lo - 1L) * cur_h  # 把 (右边界 减 左边界 减 1L) 乘 cur_h 存入 area
            if (area > ans)
                ans <- area  # 若 area 超过 答案) 答案 小于 减 area
        }
    }
    ans  # 答案
}
matrix <- c(".....", "XXXXX", ".X...", ".....")  # 把 字符(「.....」, 「.....」, 「.....」, 「.....」) 存入 矩阵
stopifnot(get_result(4L, 5L, matrix) == 6L)  # 断言校验
stopifnot(get_result_card(4L, 5L, matrix) == 6L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
