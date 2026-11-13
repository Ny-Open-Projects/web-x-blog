# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/112548608 LeetCode 112548608.
# 计算思维之经典农夫过河问题C++实现（DFS 求任一可行过河序列）
invalid <- function(st) {
    # 定义函数 invalid（参数：st）
    h <- st[1]
    w <- st[2]
    s <- st[3]
    v <- st[4]  # 把 st[1]; 权重 小于 减 st[2]; 字符串 小于 减 st[3]; 值 小于 减 st[4] 存入 h
    if (h != s && s == w)
        return(TRUE)  # 若 h 不等于 字符串 且 字符串 等于 权重) return(TRUE
    if (h != s && s == v)
        return(TRUE)  # 若 h 不等于 字符串 且 字符串 等于 值) return(TRUE
    FALSE  # FALSE
}
role_idx <- c(`-` = 0, W = 1, S = 2, V = 3)
solve_farmer <- function() {
    # 定义函数 solve_farmer（参数：无）
    path <- character(0)  # 把 character(0) 存入 当前路径
    visited <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 已访问集合
    go <- function(st) {
        # 定义函数 go（参数：st）
        if (st[1] == 1L && st[2] == 1L && st[3] == 1L && st[4] == 1L)
            return(TRUE)
        key <- paste(st, collapse = ",")  # 把 paste(st, collapse 赋值为 「,」) 存入 key
        if (!is.null(visited[[key]]))
            return(FALSE)  # 若 取反 is.null(已访问集合[[key]])) return(FALSE
        visited[[key]] <- TRUE  # 把 TRUE 存入 visited[[key]]
        for (role in c("-", "W", "S", "V")) {
            # for (role in 字符(「 减 」, 「 减 」, 「 减 」, 「 减 」)) {
            ns <- st  # 把 st 存入 ns
            ns[1] <- 1L - ns[1]  # 农夫总是过河
            ok <- TRUE  # 把 TRUE 存入 ok
            if (role != "-") {
                # 若 role 不等于 「 减 」
                idx <- as.integer(role_idx[[role]]) + 1L  # 把 as.integer(role_idx[[role]]) 加 1L 存入 idx
                if (st[1] != st[idx]) {
                  # 若 st[1] 不等于 st[idx]
                  ok <- FALSE  # 出发前不同岸，跳过
                } else {
                  # 否则
                  ns[idx] <- 1L - ns[idx]  # 把 1L 减 ns[idx] 存入 ns[idx]
                }
            }
            if (ok && !invalid(ns)) {
                # 若 ok 且 取反 invalid(ns 若 go(ns
                if (go(ns)) {
                  path <<- c(path, role)  # 当前路径 小于 小于 减 字符(当前路径, role)
                  return(TRUE)  # 返回 TRUE
                }
            }
        }
        FALSE  # FALSE
    }
    go(c(0L, 0L, 0L, 0L))  # go(字符(0L, 0L, 0L, 0L))
    rev(path)  # rev(当前路径)
}
simulate <- function(p) {
    # 定义函数 simulate（参数：节点）
    st <- c(0L, 0L, 0L, 0L)  # 把 字符(0L, 0L, 0L, 0L) 存入 st
    for (role in p) {
        # for (role in 节点) {
        before <- st  # 把 st 存入 before
        st[1] <- 1L - st[1]  # 把 1L 减 st[1] 存入 st[1]
        if (role != "-") {
            # 若 role 不等于 「 减 」
            idx <- as.integer(role_idx[[role]]) + 1L  # 把 as.integer(role_idx[[role]]) 加 1L 存入 idx
            if (before[1] != before[idx])
                return(FALSE)  # 若 before[1] 不等于 before[idx]) return(FALSE
            st[idx] <- 1L - st[idx]  # 把 1L 减 st[idx] 存入 st[idx]
        }
        if (invalid(st))
            return(FALSE)  # 若 invalid(st)) return(FALSE
    }
    st[1] == 1L && st[2] == 1L && st[3] == 1L && st[4] == 1L  # 把 赋值为 1L 且 st[2] 等于 1L 且 st[3] 等于 1L 且 st[4] 等于 1L 写入 st[1]
}
wantPath <- c("S", "-", "W", "S", "V", "-", "S")  # 把 字符(「S」, 「S」, 「S」, 「S」, 「S」, 「S」, 「S」) 存入 wantPath
wantReadable <- "HS H HW HS HV H HS"  # 把 「HS H HW HS HV H HS」 存入 wantReadable
gotPath <- solve_farmer()  # 把 solve_farmer() 存入 gotPath
# case1: 路径一致
stopifnot(length(gotPath) == length(wantPath))  # 断言校验
for (i in seq_along(wantPath)) {
    # for (下标 i in seq_along(wantPath)) {
    stopifnot(identical(gotPath[i], wantPath[i]))  # 断言校验
}
# case2: 可读方案串
parts <- ifelse(gotPath != "-", paste0("H", gotPath), "H")
gotReadable <- paste(parts, collapse = " ")  # 把 paste(parts, collapse 赋值为 「 」) 存入 gotReadable
stopifnot(identical(gotReadable, wantReadable))  # 断言校验
# case3: 7 步
stopifnot(length(gotPath) == 7L)  # 断言校验
# case4: 模拟校验
stopifnot(simulate(gotPath))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
