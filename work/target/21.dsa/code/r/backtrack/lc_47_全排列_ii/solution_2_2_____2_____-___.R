# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134134491 LeetCode 47. 全排列II — R
# 版（方案2） 定义函数 permute_unique（参数：数组）
permute_unique <- function(nums) {
    arr <- sort(nums)  # 把 sort(数组) 存入 数组
    res <- list()  # 把 列表() 存入 结果
    n <- length(arr)  # 把 长度(数组) 存入 元素个数
    used <- rep(FALSE, n)  # 把 rep(FALSE, 元素个数) 存入 已用标记
    path <- integer(0)  # 把 integer(0) 存入 当前路径
    dfs <- function() {
        # 定义函数 dfs（参数：无） 若 长度(当前路径) 等于 元素个数
        if (length(path) == n) {
            res[[length(res) + 1L]] <<- path  # 结果[[长度(结果) 加 1L]] 小于 小于 减 当前路径
            return(invisible(NULL))  # 返回 invisible(NULL
        }
        for (i in seq_len(n)) {
            # for (下标 i in seq_len(元素个数)) { 若 取反 已用标记[下标 i] 若 下标 i 等于 1 或 数组[下标 i]
            # 不等于 数组[下标 i 减 1] 或 已用标记[下标 i 减 1]
            if (!used[i]) {
                if (i == 1 || arr[i] != arr[i - 1] || used[i - 1]) {
                  used[i] <<- TRUE  # 已用标记[下标 i] 小于 小于 减 TRUE
                  path <<- c(path, arr[i])  # 当前路径 小于 小于 减 字符(当前路径, 数组[下标 i])
                  dfs()  # dfs()
                  path <<- path[-length(path)]  # 当前路径 小于 小于 减 当前路径[ 减 长度(当前路径)]
                  used[i] <<- FALSE  # 已用标记[下标 i] 小于 小于 减 FALSE
                }
            }
        }
    }
    dfs()  # dfs()
    res  # 结果
}
got <- permute_unique(c(1, 1, 2))  # 把 permute_unique(字符(1, 1, 2)) 存入 got
stopifnot(length(got) == 3)  # 断言校验
stopifnot(identical(got[[1]], c(1, 1, 2)), identical(got[[2]], c(1, 2, 1)), identical(got[[3]], c(2, 1, 1)))  # 断言校验
stopifnot(length(permute_unique(c(1, 2, 3))) == 6)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
