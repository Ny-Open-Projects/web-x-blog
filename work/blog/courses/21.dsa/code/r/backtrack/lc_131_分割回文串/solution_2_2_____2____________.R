# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133772625 LeetCode 131. 分割回文串 — R
# 版（方案2） 定义函数 is_pal（参数：字符串）
is_pal <- function(s) {
    chars <- strsplit(s, "")[[1]]  # 把 strsplit(字符串, 「」)[[1]] 存入 chars
    identical(chars, rev(chars))  # identical(chars, rev(chars))
}
partition <- function(s) {
    # 定义函数 partition（参数：字符串）
    chars <- strsplit(s, "")[[1]]  # 把 strsplit(字符串, 「」)[[1]] 存入 chars
    n <- length(chars)  # 把 长度(chars) 存入 元素个数
    res <- list()  # 把 列表() 存入 结果
    path <- character(0)  # 把 character(0) 存入 当前路径
    dfs <- function(start) {
        # 定义函数 dfs（参数：起点） 若 起点 超过 元素个数
        if (start > n) {
            res[[length(res) + 1L]] <<- path  # 结果[[长度(结果) 加 1L]] 小于 小于 减 当前路径
            return(invisible(NULL))  # 返回 invisible(NULL
        }
        for (e in start:n) {
            # for (e in 起点:元素个数) {
            sub <- paste(chars[start:e], collapse = "")  # 把 paste(chars[起点:e], collapse 赋值为 「」) 存入 sub
            if (is_pal(sub)) {
                # 若 is_pal(sub
                path <<- c(path, sub)  # 当前路径 小于 小于 减 字符(当前路径, sub)
                dfs(e + 1L)  # dfs(e 加 1L)
                path <<- path[-length(path)]  # 当前路径 小于 小于 减 当前路径[ 减 长度(当前路径)]
            }
        }
    }
    if (n > 0)
        dfs(1L) else res[[1L]] <- character(0)  # 若 元素个数 超过 0) dfs(1L) else 结果[[1L]] 小于 减 character(0
    res  # 结果
}
got <- partition("aab")  # 把 partition(「aab」) 存入 got
stopifnot(length(got) == 2)  # 断言校验
stopifnot(identical(got[[1]], c("a", "a", "b")))  # 断言校验
stopifnot(identical(got[[2]], c("aa", "b")))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
