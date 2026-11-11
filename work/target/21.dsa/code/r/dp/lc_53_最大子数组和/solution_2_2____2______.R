# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130497821 LeetCode 53. 最大子数组和 — R
# 版（方案2） 定义函数 max_sub_array（参数：数组）
max_sub_array <- function(nums) {
    best <- nums[1]
    cur <- nums[1]  # 把 数组[1]; 当前值 小于 减 数组[1] 存入 当前最优
    for (v in nums[-1]) {
        # for (值 in 数组[ 减 1]) {
        cur <- max(cur + v, v)  # 把 取较大值 当前值 加 值, 值) 存入 当前值
        best <- max(best, cur)  # 把 取较大值 当前最优, 当前值) 存入 当前最优
    }
    best  # 当前最优
}
stopifnot(max_sub_array(c(-2, 1, -3, 4, -1, 2, 1, -5, 4)) == 6)  # 断言校验
stopifnot(max_sub_array(c(1)) == 1)  # 断言校验
stopifnot(max_sub_array(c(5, 4, -1, 7, 8)) == 23)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
