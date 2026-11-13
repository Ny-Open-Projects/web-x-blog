# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136847926 LeetCode 502. IPO — R 版（方案1）
# 定义函数 find_maximized_capital（参数：下标 k, 权重, profits, capital）
find_maximized_capital <- function(k, w, profits, capital) {
    n <- length(profits)  # 把 长度(profits) 存入 元素个数
    used <- rep(FALSE, n)  # 把 rep(FALSE, 元素个数) 存入 已用标记
    for (t in seq_len(k)) {
        # for (另一字符串 in seq_len(下标 k)) {
        best <- -1
        best_j <- -1  # 把 减 1; best_j 小于 减 减 1 存入 当前最优
        for (j in seq_len(n)) {
            # for (下标 j in seq_len(元素个数)) {
            if (!used[j] && capital[j] <= w && profits[j] > best) {
                best <- profits[j]
                best_j <- j
            }
        }
        if (best_j < 0)
            break  # 若 best_j 小于 0) break
        w <- w + best  # 把 权重 加 当前最优 存入 权重
        used[best_j] <- TRUE  # 把 TRUE 存入 used[best_j]
    }
    w  # 权重
}
stopifnot(find_maximized_capital(2, 0, c(1, 2, 3), c(0, 1, 1)) == 4)  # 断言校验
stopifnot(find_maximized_capital(3, 0, c(1, 2, 3), c(0, 1, 2)) == 6)  # 断言校验
stopifnot(find_maximized_capital(1, 0, c(1, 2), c(1, 2)) == 0)  # 断言校验
stopifnot(find_maximized_capital(2, 1, c(1, 2, 3), c(1, 1, 2)) == 6)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
