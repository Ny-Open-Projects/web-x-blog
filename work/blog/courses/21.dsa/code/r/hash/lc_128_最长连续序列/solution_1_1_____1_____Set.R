# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135167108 LeetCode 128. 最长连续序列 — R
# 版（方案1） 定义函数 longest_consecutive（参数：数组）
longest_consecutive <- function(nums) {
    if (length(nums) == 0L)
        return(0L)  # 若 长度(数组) 等于 0L) return(0L
    s <- sort(unique(nums))  # 把 sort(unique(数组)) 存入 字符串
    best <- 1L
    streak <- 1L  # 把 1L; streak 小于 减 1L 存入 当前最优
    for (i in 2:length(s)) {
        # for (下标 i in 2:长度(字符串)) {
        if (s[i] == s[i - 1L] + 1L)
            streak <- streak + 1L else streak <- 1L
        if (streak > best)
            best <- streak  # 若 streak 超过 当前最优) 当前最优 小于 减 streak
    }
    best  # 当前最优
}
stopifnot(longest_consecutive(c(100, 4, 200, 1, 3, 2)) == 4L)  # 断言校验
stopifnot(longest_consecutive(c(0, 3, 7, 2, 5, 8, 4, 6, 0, 1)) == 9L)  # 断言校验
stopifnot(longest_consecutive(integer(0)) == 0L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
