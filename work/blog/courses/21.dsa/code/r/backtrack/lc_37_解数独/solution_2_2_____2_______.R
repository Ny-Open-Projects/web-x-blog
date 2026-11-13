# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134045157 LeetCode 37. 解数独 — R 版（方案2）
# 定义函数 solve_sudoku（参数：棋盘） 定义函数 valid（参数：右指针, 字符, 字符） for (下标 i in 1:9) {
solve_sudoku <- function(board) {
    valid <- function(r, c, ch) {
        for (i in 1:9) {
            if (env_b$cells[[r]][i] == ch || env_b$cells[[i]][c] == ch)
                return(FALSE)
        }
        br <- (floor((r - 1)/3)) * 3 + 1  # 把 (floor((右指针 减 1) 除以 3)) 乘 3 加 1 存入 br
        bc <- (floor((c - 1)/3)) * 3 + 1  # 把 (floor((字符 减 1) 除以 3)) 乘 3 加 1 存入 bc
        for (i in br:(br + 2)) for (j in bc:(bc + 2)) {
            # for (下标 i in br:(br 加 2)) for (下标 j in bc:(bc 加 2)) {
            if (env_b$cells[[i]][j] == ch)
                return(FALSE)  # 若 env_b$cells[[下标 i]][下标 j] 等于 字符) return(FALSE
        }
        TRUE  # TRUE
    }
    env_b <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 env_b
    env_b$cells <- lapply(board, function(r) r)  # 把 lapply(棋盘, function(右指针) 右指针) 存入 env_b$cells
    dfs <- function() {
        # 定义函数 dfs（参数：无） for (右指针 in 1:9) for (字符 in 1:9) { 若 env_b$cells[[右指针]][字符]
        # 等于 「.」 for (元素个数 in 1:9) {
        for (r in 1:9) for (c in 1:9) {
            if (env_b$cells[[r]][c] == ".") {
                for (n in 1:9) {
                  ch <- as.character(n)  # 把 as.character(元素个数) 存入 字符
                  if (valid(r, c, ch)) {
                    # 若 valid(右指针, 字符, 字符
                    env_b$cells[[r]][c] <<- ch  # env_b$cells[[右指针]][字符] 小于 小于 减 字符
                    if (dfs())
                      return(TRUE)  # 若 dfs()) return(TRUE
                    env_b$cells[[r]][c] <<- "."  # env_b$cells[[右指针]][字符] 小于 小于 减 「.」
                  }
                }
                return(FALSE)  # 返回 FALSE
            }
        }
        TRUE  # TRUE
    }
    dfs()  # dfs()
    env_b$cells  # env_b$cells
}
board <- list(c("5", "3", ".", ".", "7", ".", ".", ".", "."), c("6", ".", ".", "1", "9", "5", ".", ".", "."), c(".",
    "9", "8", ".", ".", ".", ".", "6", "."), c("8", ".", ".", ".", "6", ".", ".", ".", "3"), c("4", ".", ".", "8",
    ".", "3", ".", ".", "1"), c("7", ".", ".", ".", "2", ".", ".", ".", "6"), c(".", "6", ".", ".", ".", ".", "2",
    "8", "."), c(".", ".", ".", "4", "1", "9", ".", ".", "5"), c(".", ".", ".", ".", "8", ".", ".", "7", "9")  # 字符(「.」,「.」,「.」,「.」,「.」,「.」,「.」,「.」,「.」)
)
solved <- solve_sudoku(board)  # 把 solve_sudoku(棋盘) 存入 solved
want <- c("534678912", "672195348", "198342567", "859761423", "426853791", "713924856", "961537284", "287419635",
    "345286179")
for (r in 1:9) {
    # for (右指针 in 1:9) {
    stopifnot(paste(solved[[r]], collapse = "") == want[r])  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
