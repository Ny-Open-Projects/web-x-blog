# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703 LeetCode 107524703. 人鬼渡河问题 —
# R 版（方案4：方向入状态的 DFS 变体，断言无可行路径）
D <- list(c(2L, 0L), c(1L, 0L), c(1L, 1L), c(0L, 1L), c(0L, 2L))
safe <- function(r, g) {
    # 定义函数 safe（参数：右指针, g）
    0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g)
}
solve <- function() {
    # 定义函数 solve（参数：无）
    path <- list()  # 把 列表() 存入 当前路径
    visited <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 已访问集合
    jump <- function(dir, r, g, step) {
        # 定义函数 jump（参数：dir, 右指针, g, 步数）
        if (r == 0L && g == 0L && step%%2L == 0L)
            return(TRUE)  # 若 右指针 等于 0L 且 g 等于 0L 且 步数 对…取模 对…取模 2L 等于 0L) return(TRUE
        key <- paste(r, g, step%%2L, sep = ",")  # 把 paste(右指针, g, 步数 对…取模 对…取模 2L, sep 赋值为 「,」) 存入 key
        if (!is.null(visited[[key]]))
            return(FALSE)  # 若 取反 is.null(已访问集合[[key]])) return(FALSE
        visited[[key]] <- TRUE  # 把 TRUE 存入 visited[[key]]
        for (d in D) {
            # for (d in D) {
            dr <- d[1]
            dg <- d[2]  # 把 d[1]; dg 小于 减 d[2] 存入 dr
            nr <- r + dir * dr  # 把 右指针 加 dir 乘 dr 存入 nr
            ng <- g + dir * dg  # 把 g 加 dir 乘 dg 存入 ng
            if (safe(nr, ng) && jump(-dir, nr, ng, step + 1L)) {
                # 若 safe(nr, ng) 且 jump( 减 dir, nr, ng, 步数 加 1L
                path <<- c(path, list(c(dr, dg)))  # 当前路径 小于 小于 减 字符(当前路径, 列表(字符(dr, dg)))
                return(TRUE)  # 返回 TRUE
            }
        }
        FALSE  # FALSE
    }
    jump(-1L, 3L, 3L, 0L)  # jump( 减 1L, 3L, 3L, 0L)
    rev(path)  # rev(当前路径)
}
# 与 TS 原文件一致：该变体断言返回空路径（parity 约束下无解）
got <- solve()  # 把 solve() 存入 got
stopifnot(length(got) == 0L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
