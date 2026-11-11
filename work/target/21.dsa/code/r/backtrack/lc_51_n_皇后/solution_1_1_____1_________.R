# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133970744 LeetCode 51. N皇后 — R 版（方案1）
# 定义函数 solve_n_queens（参数：元素个数）
solve_n_queens <- function(n) {
    res <- list()  # 把 列表() 存入 结果
    cols <- rep(-1L, n)  # 把 rep( 减 1L, 元素个数) 存入 列数
    dfs <- function(row) {
        # 定义函数 dfs（参数：row） 若 row 超过 元素个数
        if (row > n) {
            board <- character(0)  # 把 character(0) 存入 棋盘
            for (r in seq_len(n)) {
                # for (右指针 in seq_len(元素个数)) {
                line <- strrep(".", n)  # 把 strrep(「.」, 元素个数) 存入 line
                chars <- strsplit(line, "")[[1]]  # 把 strsplit(line, 「」)[[1]] 存入 chars
                chars[cols[r]] <- "Q"  # 把 「Q」 存入 chars[cols[r]]
                board <- c(board, paste(chars, collapse = ""))  # 把 字符(棋盘, paste(chars, collapse 赋值为 「」)) 存入 棋盘
            }
            res[[length(res) + 1L]] <<- board  # 结果[[长度(结果) 加 1L]] 小于 小于 减 棋盘
            return(invisible(NULL))  # 返回 invisible(NULL
        }
        for (col in seq_len(n)) {
            # for (col in seq_len(元素个数)) {
            valid <- TRUE  # 把 TRUE 存入 valid
            for (r in seq_len(row - 1L)) {
                # for (右指针 in seq_len(row 减 1L)) {
                if (cols[r] == col || abs(r - row) == abs(cols[r] - col)) {
                  valid <- FALSE
                  break
                }
            }
            if (valid) {
                # 若 valid
                cols[row] <<- col  # 列数[row] 小于 小于 减 col
                dfs(row + 1L)  # dfs(row 加 1L)
            }
        }
    }
    dfs(1L)  # dfs(1L)
    res  # 结果
}
got <- solve_n_queens(4)  # 把 solve_n_queens(4) 存入 got
stopifnot(length(got) == 2)  # 断言校验
stopifnot(identical(got[[1]], c(".Q..", "...Q", "Q...", "..Q.")))  # 断言校验
stopifnot(length(solve_n_queens(1)) == 1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
