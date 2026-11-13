# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116 LeetCode 3100. 换水问题 II — R
# 版（方案1） 定义函数 max_bottles_drunk（参数：num_bottles, num_exchange）
max_bottles_drunk <- function(num_bottles, num_exchange) {
    drunk <- num_bottles
    empty <- num_bottles  # 把 num_bottles; empty 小于 减 num_bottles 存入 drunk
    while (empty >= num_exchange) {
        # 循环，直到不满足「empty 不低于 num_exchange」
        empty <- empty - num_exchange  # 把 empty 减 num_exchange 存入 empty
        num_exchange <- num_exchange + 1  # 把 num_exchange 加 1 存入 num_exchange
        drunk <- drunk + 1  # 把 drunk 加 1 存入 drunk
        empty <- empty + 1  # 把 empty 加 1 存入 empty
    }
    drunk  # drunk
}
stopifnot(max_bottles_drunk(10, 3) == 13)  # 断言校验
stopifnot(max_bottles_drunk(1, 2) == 1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
