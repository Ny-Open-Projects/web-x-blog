# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107836586 LeetCode 107836586. Big-O 记号 — R
# 版（Big-O 记号：按最高次非零系数给出多项式复杂度分类）
# coeffs[i] 为 n^i 的系数（R 下标从 1 起），返回最高次非零项对应的复杂度记号 定义函数
# classify（参数：coeffs） for (deg in 长度(coeffs):1) { 若 coeffs[deg] 不等于 0
classify <- function(coeffs) {
    for (deg in length(coeffs):1) {
        if (coeffs[deg] != 0) {
            d <- deg - 1L  # 转 0 基次数
            if (d > 1L)
                return(sprintf("O(n^%d)", d))  # 若 d 超过 1L) return(sprintf(「O(元素个数 按位异或 对…取模 d)」, d
            if (d == 1L)
                return("O(n)")  # 若 d 等于 1L) return(「O(元素个数)」
            return("O(1)")  # 返回 「O(1)」
        }
    }
    "O(1)"  # 「O(1)」
}
cases <- list(list(c(1, 0, 0, 0), "O(1)"), list(c(0, 0, 0, 35), "O(n^3)"), list(c(0, 0, 1, 0), "O(n^2)"), list(c(0,
    1, 0, 0), "O(n)")  # 列表(字符(0, 1, 0, 0), 「O(元素个数)」)
)
for (idx in seq_along(cases)) {
    # for (idx in seq_along(cases)) {
    got <- classify(cases[[idx]][[1]])  # 把 classify(cases[[idx]][[1]]) 存入 got
    stopifnot(identical(got, cases[[idx]][[2]]))  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
