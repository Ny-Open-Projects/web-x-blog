# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703 LeetCode 107524703. 人鬼渡河问题 —
# R 版（方案2：DFS+奇偶步求解）
D <- list(c(2L, 0L), c(1L, 0L), c(1L, 1L), c(0L, 1L), c(0L, 2L))
safe <- function(r, g) {
    # 定义函数 safe（参数：右指针, g）
    0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g)
}
solve <- function() {
    # 定义函数 solve（参数：无）
    path <- list()  # 把 列表() 存入 当前路径
    visited <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 已访问集合
    dfs <- function(r, g, step) {
        # 定义函数 dfs（参数：右指针, g, 步数）
        if (r == 0L && g == 0L)
            return(TRUE)  # 若 右指针 等于 0L 且 g 等于 0L) return(TRUE
        key <- paste(r, g, step%%2L, sep = ",")  # 把 paste(右指针, g, 步数 对…取模 对…取模 2L, sep 赋值为 「,」) 存入 key
        if (!is.null(visited[[key]]))
            return(FALSE)  # 若 取反 is.null(已访问集合[[key]])) return(FALSE
        visited[[key]] <- TRUE  # 把 TRUE 存入 visited[[key]]
        odd <- (step%%2L == 1L)  # 把 (步数 对…取模 对…取模 2L 等于 1L) 存入 odd
        for (d in D) {
            # for (d in D) {
            dr <- d[1]
            dg <- d[2]  # 把 d[1]; dg 小于 减 d[2] 存入 dr
            nr <- 0L
            ng <- 0L  # 把 0L; ng 小于 减 0L 存入 nr
            skip <- FALSE  # 把 FALSE 存入 skip
            if (odd) {
                # 若 odd 若 右指针 小于 dr 或 g 小于 dg
                if (r < dr || g < dg) {
                  skip <- TRUE  # 把 TRUE 存入 skip
                } else {
                  # 否则
                  nr <- r - dr
                  ng <- g - dg  # 把 右指针 减 dr; ng 小于 减 g 减 dg 存入 nr
                }
            } else {
                # 否则 若 (3L 减 右指针) 小于 dr 或 (3L 减 g) 小于 dg
                if ((3L - r) < dr || (3L - g) < dg) {
                  skip <- TRUE  # 把 TRUE 存入 skip
                } else {
                  # 否则
                  nr <- r + dr
                  ng <- g + dg  # 把 右指针 加 dr; ng 小于 减 g 加 dg 存入 nr
                }
            }
            if (!skip && safe(nr, ng) && dfs(nr, ng, step + 1L)) {
                # 若 取反 skip 且 safe(nr, ng) 且 dfs(nr, ng, 步数 加 1L
                path <<- c(path, list(c(dr, dg)))  # 当前路径 小于 小于 减 字符(当前路径, 列表(字符(dr, dg)))
                return(TRUE)  # 返回 TRUE
            }
        }
        FALSE  # FALSE
    }
    dfs(3L, 3L, 1L)  # dfs(3L, 3L, 1L)
    rev(path)  # rev(当前路径)
}
want <- list(c(1L, 1L), c(1L, 0L), c(0L, 2L), c(0L, 1L), c(2L, 0L), c(1L, 1L), c(2L, 0L), c(0L, 1L), c(0L, 2L),
    c(1L, 0L), c(1L, 1L))
got <- solve()  # 把 solve() 存入 got
stopifnot(length(got) == length(want))  # 断言校验
for (i in seq_along(want)) {
    # for (下标 i in seq_along(want)) {
    stopifnot(identical(as.integer(got[[i]]), as.integer(want[[i]])))  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
