# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483 LeetCode 108673483. 减治策略 — R
# 版（方案3：Boyer-Moore 摩尔投票求多数元素） 定义函数 majority_element（参数：数组）
majority_element <- function(arr) {
    candidate <- NULL  # 把 NULL 存入 candidate
    count <- 0L  # 把 0L 存入 计数
    for (num in arr) {
        # for (num in 数组) {
        if (count == 0L)
            candidate <- num  # 若 计数 等于 0L) candidate 小于 减 num
        if (num == candidate)
            count <- count + 1L else count <- count - 1L  # 若 num 等于 candidate) 计数 小于 减 计数 加 1L else 计数 小于 减 计数 减 1L
    }
    cnt <- sum(arr == candidate)  # 把 累计和(数组 等于 candidate) 存入 计数
    if (cnt > length(arr)%/%2L)
        return(as.integer(candidate))  # 若 计数 超过 长度(数组) 对…取模 除以 对…取模 2L) return(as.integer(candidate
    -1L  # 减 1L
}
cases <- list(list(c(2L, 2L, 1L, 1L, 1L, 1L, 1L), 1L), list(c(1L, 2L, 3L), -1L), list(c(3L, 3L, 4L), 3L)  # 列表(字符(3L, 3L, 4L), 3L)
)
for (idx in seq_along(cases)) {
    # for (idx in seq_along(cases)) {
    got <- majority_element(cases[[idx]][[1]])  # 把 majority_element(cases[[idx]][[1]]) 存入 got
    stopifnot(got == cases[[idx]][[2]])  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
