# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066015 LeetCode 41. 缺失的第一个正数 — R
# 版（方案4） 定义函数 first_missing_positive（参数：数组）
first_missing_positive <- function(nums) {
    if (length(nums) == 0L)
        return(1L)  # 若 长度(数组) 等于 0L) return(1L
    pos <- sort(nums[nums > 0])  # 把 sort(数组[数组 超过 0]) 存入 pos
    if (length(pos) == 0L)
        return(1L)  # 若 长度(pos) 等于 0L) return(1L
    if (pos[1] != 1)
        return(1L)  # 若 pos[1] 不等于 1) return(1L
    n <- length(pos)  # 把 长度(pos) 存入 元素个数
    for (i in 1:(n - 1)) {
        # for (下标 i in 1:(元素个数 减 1)) {
        if (pos[i + 1] - pos[i] > 1)
            return(pos[i] + 1)  # 若 pos[下标 i 加 1] 减 pos[下标 i] 超过 1) return(pos[下标 i] 加 1
    }
    pos[n] + 1  # pos[元素个数] 加 1
}
stopifnot(first_missing_positive(c(1, 2, 0)) == 3)  # 断言校验
stopifnot(first_missing_positive(c(3, 4, -1, 1)) == 2)  # 断言校验
stopifnot(first_missing_positive(c(7, 8, 9, 11, 12)) == 1)  # 断言校验
stopifnot(first_missing_positive(integer(0)) == 1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
