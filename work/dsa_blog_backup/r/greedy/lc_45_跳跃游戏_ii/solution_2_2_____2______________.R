# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133911745 LeetCode 45. 跳跃游戏II — R
# 版（方案2） 定义函数 jump（参数：数组）
jump <- function(nums) {
    position <- length(nums)
    steps <- 0L  # 把 长度(数组); steps 小于 减 0L 存入 position
    while (position > 1L) {
        # 循环，直到不满足「position 超过 1L」 for (下标 i in 1:(position 减 1L)) { 若 (下标 i 减 1L) 加
        # 数组[下标 i] 不低于 position 减 1L
        for (i in 1:(position - 1L)) {
            if ((i - 1L) + nums[i] >= position - 1L) {
                position <- i  # 把 下标 i 存入 position
                steps <- steps + 1L  # 把 steps 加 1L 存入 steps
                break  # 跳出循环
            }
        }
    }
    steps  # steps
}
stopifnot(jump(c(2, 3, 1, 1, 4)) == 2)  # 断言校验
stopifnot(jump(c(2, 3, 0, 1, 4)) == 2)  # 断言校验
stopifnot(jump(c(1)) == 0)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
