# 来源：https://blog.csdn.net/tyro_java/article/details/107490876 LeetCode 107490876. 分书和八皇后问题 — R
# 版（方案4：八皇后显式栈迭代） 定义函数 valid_q（参数：x, 数组）
valid_q <- function(x, a) {
    y <- length(a) + 1L  # 把 长度(数组) 加 1L 存入 y
    for (i in seq_along(a)) {
        # for (下标 i in seq_along(数组)) {
        if (x == a[i] || abs(y - i) == abs(x - a[i]))
            return(FALSE)
    }
    TRUE  # TRUE
}
n_queens_stack <- function(n) {
    # 定义函数 n_queens_stack（参数：元素个数）
    solutions <- list()  # 把 列表() 存入 solutions
    stack <- list(integer(0))  # 把 列表(integer(0)) 存入 栈
    while (length(stack) > 0L) {
        # 循环，直到不满足「长度(栈) 超过 0L」
        a <- stack[[length(stack)]]  # 把 栈[[长度(栈)]] 存入 数组
        stack <- stack[-length(stack)]  # 把 栈[ 减 长度(栈)] 存入 栈
        if (length(a) == n) {
            # 若 长度(数组) 等于 元素个数
            solutions[[length(solutions) + 1L]] <- a  # solutions[[长度(solutions) 加 1L]] 小于 减 数组
        } else {
            # 否则 for (下标 i in 1:元素个数) { 若 valid_q(下标 i, 数组
            for (i in 1:n) {
                if (valid_q(i, a)) {
                  stack[[length(stack) + 1L]] <- c(a, i)  # 栈[[长度(栈) 加 1L]] 小于 减 字符(数组, 下标 i)
                }
            }
        }
    }
    solutions  # solutions
}
cases <- list(list(8L, 92L, c(8, 4, 1, 3, 6, 2, 7, 5)), list(1L, 1L, c(1)), list(2L, 0L, NULL), list(4L, 2L, c(3,
    1, 4, 2))  # 列表(4L, 2L, 字符(3, 1, 4, 2))
)
for (idx in seq_along(cases)) {
    # for (idx in seq_along(cases)) {
    sols <- n_queens_stack(cases[[idx]][[1]])  # 把 n_queens_stack(cases[[idx]][[1]]) 存入 sols
    stopifnot(length(sols) == cases[[idx]][[2]])  # 断言校验
    if (!is.null(cases[[idx]][[3]])) {
        # 若 取反 is.null(cases[[idx]][[3]]
        stopifnot(identical(as.integer(sols[[1]]), as.integer(cases[[idx]][[3]])))  # 断言校验
    }
}
cat("PASS\n")  # 全部用例通过，输出 PASS
