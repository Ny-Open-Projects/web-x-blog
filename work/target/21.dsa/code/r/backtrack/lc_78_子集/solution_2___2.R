# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134109616 LeetCode 78. 子集 — R 版（方案2）
# 定义函数 subsets（参数：数组）
subsets <- function(nums) {
    res <- list()  # 把 列表() 存入 结果
    path <- integer(0)  # 把 integer(0) 存入 当前路径
    dfs <- function(start) {
        # 定义函数 dfs（参数：起点）
        res[[length(res) + 1L]] <<- path  # 结果[[长度(结果) 加 1L]] 小于 小于 减 当前路径
        if (start > length(nums))
            return(invisible(NULL))  # 若 起点 超过 长度(数组)) return(invisible(NULL
        for (i in start:length(nums)) {
            # for (下标 i in 起点:长度(数组)) {
            path <<- c(path, nums[i])  # 当前路径 小于 小于 减 字符(当前路径, 数组[下标 i])
            dfs(i + 1L)  # dfs(下标 i 加 1L)
            path <<- path[-length(path)]  # 当前路径 小于 小于 减 当前路径[ 减 长度(当前路径)]
        }
    }
    if (length(nums) > 0)
        dfs(1L) else res[[1L]] <- integer(0)  # 若 长度(数组) 超过 0) dfs(1L) else 结果[[1L]] 小于 减 integer(0
    res  # 结果
}
stopifnot(length(subsets(c(1, 2, 3))) == 8)  # 断言校验
stopifnot(length(subsets(0)) == 2)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
