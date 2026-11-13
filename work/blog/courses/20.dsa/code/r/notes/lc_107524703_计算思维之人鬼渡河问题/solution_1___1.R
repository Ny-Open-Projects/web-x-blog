# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703 LeetCode 107524703. 人鬼渡河问题 —
# R 版（方案1：安全判定谓词） 定义函数 is_safe（参数：右指针, g）
is_safe <- function(r, g) {
    0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g)
}
cases <- list(list(3L, 3L, TRUE), list(3L, 1L, TRUE), list(2L, 2L, TRUE), list(1L, 3L, FALSE), list(0L, 0L, TRUE)  # 列表(1L, 3L, FALSE), 列表(0L, 0L, TRUE)
)
for (idx in seq_along(cases)) {
    # for (idx in seq_along(cases)) {
    stopifnot(is_safe(cases[[idx]][[1]], cases[[idx]][[2]]) == cases[[idx]][[3]])  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
