# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116 LeetCode 1518. 换水问题 — R
# 版（方案2） 定义函数 num_water_bottles（参数：num_bottles, num_exchange）
num_water_bottles <- function(num_bottles, num_exchange) {
    ans <- num_bottles
    empty <- num_bottles  # 把 num_bottles; empty 小于 减 num_bottles 存入 答案
    while (empty >= num_exchange) {
        # 循环，直到不满足「empty 不低于 num_exchange」
        new_b <- empty%/%num_exchange  # 把 empty 对…取模 除以 对…取模 num_exchange 存入 new_b
        ans <- ans + new_b  # 把 答案 加 new_b 存入 答案
        empty <- new_b + empty%%num_exchange  # 把 new_b 加 empty 对…取模 对…取模 num_exchange 存入 empty
    }
    ans  # 答案
}
stopifnot(num_water_bottles(9L, 3L) == 13L)  # 断言校验
stopifnot(num_water_bottles(15L, 4L) == 19L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
