# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726 LeetCode 107431726. 最大红矩形分析
# — R 版（方案D：逐行高度 + 单调栈） 定义函数 max_red_rectangle（参数：矩阵）
max_red_rectangle <- function(matrix) {
    n <- length(matrix)  # 把 长度(矩阵) 存入 元素个数
    m <- nchar(matrix[1])  # 把 nchar(矩阵[1]) 存入 映射表
    ans <- 0L  # 把 0L 存入 答案
    height <- rep(0L, m + 2L)  # 把 rep(0L, 映射表 加 2L) 存入 height
    for (k in 1:n) {
        # for (下标 k in 1:元素个数) { for (下标 i in 1:映射表) {
        for (i in 1:m) {
            if (substr(matrix[k], i, i) == ".")
                height[i] <- height[i] + 1L else height[i] <- 0L
        }
        stack <- c(0L)  # 把 字符(0L) 存入 栈
        h_at <- function(i) if (i == 0L)
            0L else height[i]  # 定义函数 h_at（参数：下标 i）
        for (i in 1:(m + 1L)) {
            # for (下标 i in 1:(映射表 加 1L)) {
            hi <- if (i <= m)
                height[i] else 0L  # 把 if (下标 i 不超过 映射表) height[下标 i] else 0L 存入 右边界
            while (h_at(stack[length(stack)]) > hi) {
                # 循环，直到不满足「h_at(栈[长度(栈)]) 超过 右边界」
                now_h <- h_at(stack[length(stack)])  # 把 h_at(栈[长度(栈)]) 存入 now_h
                stack <- stack[-length(stack)]  # 把 栈[ 减 长度(栈)] 存入 栈
                width <- i - stack[length(stack)] - 1L  # 把 下标 i 减 栈[长度(栈)] 减 1L 存入 width
                area <- now_h * width  # 把 now_h 乘 width 存入 area
                if (area > ans)
                  ans <- area  # 若 area 超过 答案) 答案 小于 减 area
            }
            stack <- c(stack, i)  # 把 字符(栈, 下标 i) 存入 栈
        }
    }
    ans  # 答案
}
matrix <- c(".....", "XXXXX", ".X...", ".....")  # 把 字符(「.....」, 「.....」, 「.....」, 「.....」) 存入 矩阵
stopifnot(max_red_rectangle(matrix) == 6L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
