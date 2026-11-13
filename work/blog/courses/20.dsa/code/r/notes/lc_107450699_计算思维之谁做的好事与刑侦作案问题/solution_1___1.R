# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107450699 计算思维之谁做的好事 — R
# 版（方案1） 定义函数 find_good_man（参数：无）
find_good_man <- function() {
    men <- c("A", "B", "C", "D")  # 把 字符(「A」, 「A」, 「A」, 「A」) 存入 men
    for (m in men) {
        # for (映射表 in men) {
        t <- 0L  # 把 0L 存入 另一字符串
        if (m != "A")
            t <- t + 1L  # 若 映射表 不等于 「A」) 另一字符串 小于 减 另一字符串 加 1L
        if (m == "C")
            t <- t + 1L  # 若 映射表 等于 「C」) 另一字符串 小于 减 另一字符串 加 1L
        if (m == "D")
            t <- t + 1L  # 若 映射表 等于 「D」) 另一字符串 小于 减 另一字符串 加 1L
        if (m != "D")
            t <- t + 1L  # 若 映射表 不等于 「D」) 另一字符串 小于 减 另一字符串 加 1L
        if (t == 3L)
            return(m)  # 若 另一字符串 等于 3L) return(映射表
    }
    "?"  # 「?」
}
stopifnot(find_good_man() == "C")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
