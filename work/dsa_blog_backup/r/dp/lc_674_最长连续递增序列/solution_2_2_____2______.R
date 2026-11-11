# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130771608 LeetCode 674. 最长连续递增序列 — R
# 版（方案2） 定义函数 find_length_of_lcis（参数：数组）
find_length_of_lcis <- function(nums) {
    if (length(nums) == 0)
        return(0L)  # 若 长度(数组) 等于 0) return(0L
    best <- 1L
    cur <- 1L  # 把 1L; 当前值 小于 减 1L 存入 当前最优
    for (i in 2:length(nums)) {
        # for (下标 i in 2:长度(数组)) {
        if (nums[i] > nums[i - 1]) {
            cur <- cur + 1L
            if (cur > best)
                best <- cur
        } else cur <- 1L
    }
    best  # 当前最优
}
stopifnot(find_length_of_lcis(c(1, 3, 5, 4, 7)) == 3)  # 断言校验
stopifnot(find_length_of_lcis(c(2, 2, 2, 2, 2)) == 1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
