# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806 数据结构与算法笔记: 复杂度 — R
# 版（方案6） 定义函数 func_calls（参数：元素个数）
func_calls <- function(n) {
    if (n <= 1)
        return(1)  # 若 元素个数 不超过 1) return(1
    2 * func_calls(n - 1)  # 2 乘 func_calls(元素个数 减 1)
}
stopifnot(func_calls(1) == 1, func_calls(2) == 2, func_calls(5) == 16, func_calls(10) == 512)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
