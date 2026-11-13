# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134424807 LeetCode 485. 最大连续1的个数 — R
# 版（方案1） 定义函数 find_max_consecutive_ones（参数：数组）
find_max_consecutive_ones <- function(nums) {
    best <- 0L
    cur <- 0L  # 把 0L; 当前值 小于 减 0L 存入 当前最优
    for (v in nums) {
        # for (值 in 数组) {
        if (v == 1) {
            cur <- cur + 1L
            if (cur > best)
                best <- cur
        } else cur <- 0L
    }
    best  # 当前最优
}
stopifnot(find_max_consecutive_ones(c(1, 1, 0, 1, 1, 1)) == 3)  # 断言校验
stopifnot(find_max_consecutive_ones(c(1, 0, 1, 1, 0, 1)) == 2)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
