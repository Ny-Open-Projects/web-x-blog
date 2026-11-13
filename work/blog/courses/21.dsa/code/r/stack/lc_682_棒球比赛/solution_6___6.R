# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734875 LeetCode 682. 棒球比赛 — R
# 版（方案6） 定义函数 cal_points（参数：ops）
cal_points <- function(ops) {
    st <- integer(0)  # 把 integer(0) 存入 st
    for (op in ops) {
        # for (op in ops) {
        if (op == "+")
            st <- c(st, st[length(st)] + st[length(st) - 1])  # 若 op 等于 「 加 」) st 小于 减 字符(st, st[长度(st)] 加 st[长度(st) 减 1]
 else if (op == "D")
            st <- c(st, st[length(st)] * 2)  # 否则，若 op 等于 「D」) st 小于 减 字符(st, st[长度(st)] 乘 2
 else if (op == "C")
            st <- st[-length(st)]  # 否则，若 op 等于 「C」) st 小于 减 st[ 减 长度(st)]
 else st <- c(st, as.integer(op))  # 否则
    }
    sum(st)  # 累计和(st)
}
stopifnot(cal_points(c("5", "2", "C", "D", "+")) == 30)  # 断言校验
stopifnot(cal_points(c("5", "-2", "4", "C", "D", "9", "+", "+")) == 27)  # 断言校验
stopifnot(cal_points(c("1", "C")) == 0)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
