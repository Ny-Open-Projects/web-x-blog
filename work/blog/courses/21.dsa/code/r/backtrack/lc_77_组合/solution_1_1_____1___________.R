# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134178290 LeetCode 77. 组合 — R 版（方案1）
# 定义函数 combine（参数：元素个数, 下标 k）
combine <- function(n, k) {
    res <- list()  # 把 列表() 存入 结果
    path <- integer(0)  # 把 integer(0) 存入 当前路径
    dfs <- function(start) {
        # 定义函数 dfs（参数：起点） 若 长度(当前路径) 等于 下标 k
        if (length(path) == k) {
            res[[length(res) + 1L]] <<- path  # 结果[[长度(结果) 加 1L]] 小于 小于 减 当前路径
            return(invisible(NULL))  # 返回 invisible(NULL
        }
        upper <- as.integer(n - (k - length(path)) + 1)  # 把 as.integer(元素个数 减 (下标 k 减 长度(当前路径)) 加 1) 存入 upper
        if (start > upper)
            return(invisible(NULL))  # 若 起点 超过 upper) return(invisible(NULL
        for (i in start:upper) {
            # for (下标 i in 起点:upper) {
            path <<- c(path, i)  # 当前路径 小于 小于 减 字符(当前路径, 下标 i)
            dfs(i + 1L)  # dfs(下标 i 加 1L)
            path <<- path[-length(path)]  # 当前路径 小于 小于 减 当前路径[ 减 长度(当前路径)]
        }
    }
    dfs(1L)  # dfs(1L)
    res  # 结果
}
got <- combine(4, 2)  # 把 combine(4, 2) 存入 got
stopifnot(length(got) == 6)  # 断言校验
stopifnot(identical(got[[1]], c(1L, 2L)), identical(got[[6]], c(3L, 4L)))  # 断言校验
stopifnot(length(combine(1, 1)) == 1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
