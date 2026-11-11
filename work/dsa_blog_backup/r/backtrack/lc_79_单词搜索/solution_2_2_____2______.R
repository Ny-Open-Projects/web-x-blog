# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134204437 LeetCode 79. 单词搜索 — R
# 版（方案2） 定义函数 exist（参数：棋盘, 单词）
exist <- function(board, word) {
    rows <- length(board)  # 把 长度(棋盘) 存入 行数
    cols <- length(board[[1]])  # 把 长度(棋盘[[1]]) 存入 列数
    w <- strsplit(word, "")[[1]]  # 把 strsplit(单词, 「」)[[1]] 存入 权重
    dfs <- function(i, j, k) {
        # 定义函数 dfs（参数：下标 i, 下标 j, 下标 k）
        if (k > length(w))
            return(TRUE)  # 若 下标 k 超过 长度(权重)) return(TRUE
        if (i < 1 || i > rows || j < 1 || j > cols)
            return(FALSE)
        if (env_board$cells[[i]][j] != w[k])
            return(FALSE)  # 若 env_board$cells[[下标 i]][下标 j] 不等于 权重[下标 k]) return(FALSE
        saved <- env_board$cells[[i]][j]  # 把 env_board$cells[[下标 i]][下标 j] 存入 saved
        env_board$cells[[i]][j] <<- "#"
        found <- dfs(i + 1, j, k + 1) || dfs(i - 1, j, k + 1) || dfs(i, j + 1, k + 1) || dfs(i, j - 1, k + 1)
        env_board$cells[[i]][j] <<- saved  # env_board$cells[[下标 i]][下标 j] 小于 小于 减 saved
        found  # found
    }
    env_board <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 env_board
    env_board$cells <- lapply(board, function(r) r)  # 把 lapply(棋盘, function(右指针) 右指针) 存入 env_board$cells
    for (i in seq_len(rows)) {
        # for (下标 i in seq_len(行数)) { for (下标 j in seq_len(列数)) {
        for (j in seq_len(cols)) {
            if (dfs(i, j, 1))
                return(TRUE)  # 若 dfs(下标 i, 下标 j, 1)) return(TRUE
        }
    }
    FALSE  # FALSE
}
b <- list(c("A", "B", "C", "E"), c("S", "F", "C", "S"), c("A", "D", "E", "E"))
stopifnot(exist(b, "ABCCED"))  # 断言校验
stopifnot(exist(b, "SEE"))  # 断言校验
stopifnot(!exist(b, "ABCB"))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
