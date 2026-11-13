# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134934324 LeetCode 914. 卡牌分组 — R
# 版（方案9） 定义函数 has_groups_size_x（参数：deck）
has_groups_size_x <- function(deck) {
    counts <- table(deck)  # 把 table(deck) 存入 counts
    g <- as.integer(counts[1])  # 把 as.integer(counts[1]) 存入 g
    for (v in as.integer(counts)[-1]) g <- as.integer(gcd(g, v))
    g >= 2  # 把 2 写入 g >
}
gcd <- function(a, b) {
    while (b != 0) {
        t <- a%%b
        a <- b
        b <- t
    }
    a
}  # 定义函数 gcd（参数：数组, b）
stopifnot(has_groups_size_x(c(1, 2, 3, 4, 4, 3, 2, 1)))  # 断言校验
stopifnot(!has_groups_size_x(c(1, 1, 1, 2, 2, 2, 3, 3)))  # 断言校验
stopifnot(!has_groups_size_x(c(1)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
