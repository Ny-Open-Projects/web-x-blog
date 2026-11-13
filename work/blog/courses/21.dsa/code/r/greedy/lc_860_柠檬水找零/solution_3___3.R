# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135167617 LeetCode 860. 柠檬水找零 — R
# 版（方案3） 定义函数 lemonade_change（参数：bills）
lemonade_change <- function(bills) {
    f5 <- 0L
    f10 <- 0L  # 把 0L; f10 小于 减 0L 存入 f5
    for (b in bills) {
        # for (b in bills) { 否则
        if (b == 5)
            f5 <- f5 + 1L  # 若 b 等于 5) f5 小于 减 f5 加 1L
 else if (b == 10)
            {
                f10 <- f10 + 1L
                f5 <- f5 - 1L
            }  # 否则，若 b 等于 10) { f10 小于 减 f10 加 1L; f5 小于 减 f5 减 1L }
 else {
            if (f10 > 0) {
                f10 <- f10 - 1L
                f5 <- f5 - 1L
            } else f5 <- f5 - 3L
        }
        if (f5 < 0)
            return(FALSE)  # 若 f5 小于 0) return(FALSE
    }
    TRUE  # TRUE
}
stopifnot(lemonade_change(c(5L, 5L, 5L, 10L, 20L)))  # 断言校验
stopifnot(!lemonade_change(c(5L, 5L, 10L, 10L, 20L)))  # 断言校验
stopifnot(lemonade_change(c(5L, 5L, 5L, 5L, 20L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
