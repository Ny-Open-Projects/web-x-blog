# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133767953 LeetCode 46. 全排列 — R 版（方案1）
# 定义函数 permute_fn（参数：数组）
permute_fn <- function(nums) {
    res <- list()  # 把 列表() 存入 结果
    n <- length(nums)  # 把 长度(数组) 存入 元素个数
    used <- rep(FALSE, n)  # 把 rep(FALSE, 元素个数) 存入 已用标记
    path <- integer(0)  # 把 integer(0) 存入 当前路径
    dfs <- function() {
        # 定义函数 dfs（参数：无） 若 长度(当前路径) 等于 元素个数
        if (length(path) == n) {
            res[[length(res) + 1L]] <<- path  # 结果[[长度(结果) 加 1L]] 小于 小于 减 当前路径
            return(invisible(NULL))  # 返回 invisible(NULL
        }
        for (i in seq_len(n)) {
            # for (下标 i in seq_len(元素个数)) { 若 取反 已用标记[下标 i]
            if (!used[i]) {
                used[i] <<- TRUE  # 已用标记[下标 i] 小于 小于 减 TRUE
                path <<- c(path, nums[i])  # 当前路径 小于 小于 减 字符(当前路径, 数组[下标 i])
                dfs()  # dfs()
                path <<- path[-length(path)]  # 当前路径 小于 小于 减 当前路径[ 减 长度(当前路径)]
                used[i] <<- FALSE  # 已用标记[下标 i] 小于 小于 减 FALSE
            }
        }
    }
    dfs()  # dfs()
    res  # 结果
}
got <- permute_fn(c(1L, 2L, 3L))  # 把 permute_fn(字符(1L, 2L, 3L)) 存入 got
stopifnot(length(got) == 6)  # 断言校验
stopifnot(identical(got[[1]], c(1L, 2L, 3L)))  # 断言校验
stopifnot(identical(got[[2]], c(1L, 3L, 2L)))  # 断言校验
stopifnot(identical(got[[3]], c(2L, 1L, 3L)))  # 断言校验
stopifnot(identical(got[[6]], c(3L, 2L, 1L)))  # 断言校验
stopifnot(length(permute_fn(c(0L, 1L))) == 2)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
