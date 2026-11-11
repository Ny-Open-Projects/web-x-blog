# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133865307 LeetCode 39. 组合总和 — R
# 版（方案1） 定义函数 combination_sum（参数：候选数组, 目标值）
combination_sum <- function(candidates, target) {
    res <- list()  # 把 列表() 存入 结果
    path <- integer(0)  # 把 integer(0) 存入 当前路径
    dfs <- function(start, remaining) {
        # 定义函数 dfs（参数：起点, remaining） 若 remaining 等于 0
        if (remaining == 0) {
            res[[length(res) + 1L]] <<- path  # 结果[[长度(结果) 加 1L]] 小于 小于 减 当前路径
            return(invisible(NULL))  # 返回 invisible(NULL
        }
        if (remaining < 0)
            return(invisible(NULL))  # 若 remaining 小于 0) return(invisible(NULL
        for (i in start:length(candidates)) {
            # for (下标 i in 起点:长度(候选数组)) {
            path <<- c(path, candidates[i])  # 当前路径 小于 小于 减 字符(当前路径, 候选数组[下标 i])
            dfs(i, remaining - candidates[i])  # dfs(下标 i, remaining 减 候选数组[下标 i])
            path <<- path[-length(path)]  # 当前路径 小于 小于 减 当前路径[ 减 长度(当前路径)]
        }
    }
    if (length(candidates) > 0)
        dfs(1L, target)  # 若 长度(候选数组) 超过 0) dfs(1L, 目标值
    res  # 结果
}
got <- combination_sum(c(2, 3, 6, 7), 7)  # 把 combination_sum(字符(2, 3, 6, 7), 7) 存入 got
stopifnot(length(got) == 2, identical(got[[1]], c(2, 2, 3)), identical(got[[2]], 7))  # 断言校验
got2 <- combination_sum(c(2, 3, 5), 8)  # 把 combination_sum(字符(2, 3, 5), 8) 存入 got2
stopifnot(length(got2) == 3, identical(got2[[3]], c(3, 5)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
