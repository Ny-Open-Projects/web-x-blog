# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023 求直方图最大面积算法分析 — R
# 版（方案2） 定义函数 get_result_hist（参数：元素个数, heights）
get_result_hist <- function(n, heights) {
    st <- integer(0)  # 把 integer(0) 存入 st
    best <- 0L  # 把 0L 存入 当前最优
    at <- function(i) if (i <= length(heights))
        heights[i] else 0  # 定义函数 at（参数：下标 i）
    for (i in 1:(length(heights) + 1L)) {
        # for (下标 i in 1:(长度(heights) 加 1L)) {
        cur <- at(i)  # 把 at(下标 i) 存入 当前值
        while (length(st) > 0 && heights[st[length(st)]] >= cur) {
            # 循环，直到不满足「长度(st) 超过 0 且 heights[st[长度(st)]] 不低于 当前值」
            t <- st[length(st)]  # 把 st[长度(st)] 存入 另一字符串
            st <- st[-length(st)]  # 把 st[ 减 长度(st)] 存入 st
            left <- if (length(st) > 0)
                st[length(st)] else 0L  # 把 if (长度(st) 超过 0) st[长度(st)] else 0L 存入 左边界
            width <- i - left - 1L  # 把 下标 i 减 左边界 减 1L 存入 width
            area <- as.numeric(heights[t]) * width  # 把 as.numeric(heights[另一字符串]) 乘 width 存入 area
            if (area > best)
                best <- as.integer(area)  # 若 area 超过 当前最优) 当前最优 小于 减 as.integer(area
        }
        st <- c(st, i)  # 把 字符(st, 下标 i) 存入 st
    }
    best  # 当前最优
}
stopifnot(get_result_hist(5, c(0, 2, 3, 3, 3, 2, 0)) == 10)  # 断言校验
stopifnot(get_result_hist(6, c(0, 2, 1, 5, 6, 2, 3, 0)) == 10)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
