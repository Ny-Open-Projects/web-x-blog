# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133982215 LeetCode 417. 太平洋大西洋水流问题
# — R 版
# 方案2（DFS 反向流动，从海洋边界出发） 定义函数 pacific_atlantic（参数：matrix_）
pacific_atlantic <- function(matrix_) {
    if (is.null(matrix_) || length(matrix_) == 0 || length(matrix_[[1]]) == 0) {
        return(list())  # 返回 列表(
    }
    m <- length(matrix_)  # 把 长度(matrix_) 存入 映射表
    n <- length(matrix_[[1]])  # 把 长度(matrix_[[1]]) 存入 元素个数
    # R 为传值拷贝语义，用 environment 包装 flow 矩阵以便递归内更新
    penv <- new.env(parent = emptyenv())
    penv$flow <- matrix(FALSE, m, n)
    aenv <- new.env(parent = emptyenv())
    aenv$flow <- matrix(FALSE, m, n)
    dfs <- function(r, c, fenv) {
        # 定义函数 dfs（参数：右指针, 字符, fenv）
        fenv$flow[r, c] <- TRUE  # fenv$flow[右指针, 字符] 小于 减 TRUE
        dirs <- list(c(-1L, 0L), c(1L, 0L), c(0L, -1L), c(0L, 1L))
        for (d in dirs) {
            # for (d in dirs) {
            nr <- r + d[1L]  # 把 右指针 加 d[1L] 存入 nr
            nc <- c + d[2L]  # 把 字符 加 d[2L] 存入 nc
            if (nr >= 1 && nr <= m && nc >= 1 && nc <= n && !fenv$flow[nr, nc] && matrix_[[nr]][nc] >= matrix_[[r]][c]) {
                dfs(nr, nc, fenv)  # dfs(nr, nc, fenv)
            }
        }
    }
    for (r in seq_len(m)) {
        # for (右指针 in seq_len(映射表)) {
        dfs(r, 1L, penv)  # dfs(右指针, 1L, penv)
        dfs(r, n, aenv)  # dfs(右指针, 元素个数, aenv)
    }
    for (cc in seq_len(n)) {
        # for (cc in seq_len(元素个数)) {
        dfs(1L, cc, penv)  # dfs(1L, cc, penv)
        dfs(m, cc, aenv)  # dfs(映射表, cc, aenv)
    }
    res <- list()  # 把 列表() 存入 结果
    for (r in seq_len(m)) {
        # for (右指针 in seq_len(映射表)) { for (cc in seq_len(元素个数)) { 若 penv$flow[右指针, cc] 且
        # aenv$flow[右指针, cc]
        for (cc in seq_len(n)) {
            if (penv$flow[r, cc] && aenv$flow[r, cc]) {
                res[[length(res) + 1L]] <- c(r - 1L, cc - 1L)  # 转回 0 基坐标
            }
        }
    }
    res  # 结果
}
got <- pacific_atlantic(list(c(1L, 2L, 2L, 3L, 5L), c(3L, 2L, 3L, 4L, 4L), c(2L, 4L, 5L, 3L, 1L), c(6L, 7L, 1L,
    4L, 5L), c(5L, 1L, 1L, 2L, 4L)  # 字符(5L, 1L, 1L, 2L, 4L)
))
expected <- list(c(0L, 4L), c(1L, 3L), c(1L, 4L), c(2L, 2L), c(3L, 0L), c(3L, 1L), c(4L, 0L))
stopifnot(length(got) == length(expected))  # 断言校验
for (i in seq_along(expected)) {
    # for (下标 i in seq_along(expected)) {
    stopifnot(identical(got[[i]], expected[[i]]))  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
