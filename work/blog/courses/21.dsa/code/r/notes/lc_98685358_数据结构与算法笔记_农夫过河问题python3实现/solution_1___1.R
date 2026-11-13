# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/98685358 LeetCode 98685358. 农夫过河问题 — R
# 版（农夫过河问题：BFS 求最短过河序列，状态 (农夫,狼,羊,菜)，0=左岸 1=右岸）
is_safe <- function(s) {
    # 定义函数 is_safe（参数：字符串）
    if (s[2] == s[3] && s[1] != s[2])
        return(FALSE)  # 若 字符串[2] 等于 字符串[3] 且 字符串[1] 不等于 字符串[2]) return(FALSE
    if (s[3] == s[4] && s[1] != s[3])
        return(FALSE)  # 若 字符串[3] 等于 字符串[4] 且 字符串[1] 不等于 字符串[3]) return(FALSE
    TRUE  # TRUE
}
key_of <- function(s) paste(s, collapse = ",")  # 定义函数 key_of（参数：字符串）
solve <- function() {
    # 定义函数 solve（参数：无）
    start <- c(0L, 0L, 0L, 0L)  # 把 字符(0L, 0L, 0L, 0L) 存入 起点
    goal <- c(1L, 1L, 1L, 1L)  # 把 字符(1L, 1L, 1L, 1L) 存入 goal
    prev <- new.env(parent = emptyenv())  # key -> 父 key（起点为 NA）
    state_by <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 state_by
    prev[[key_of(start)]] <- NA_character_  # 把 NA_character_ 存入 prev[[key_of(start)]]
    state_by[[key_of(start)]] <- start  # 把 起点 存入 state_by[[key_of(start)]]
    q <- list(start)  # 把 列表(起点) 存入 节点
    head <- 1L  # 把 1L 存入 头节点
    while (head <= length(q)) {
        # 循环，直到不满足「头节点 不超过 长度(节点」
        cur <- q[[head]]  # 把 节点[[头节点]] 存入 当前值
        head <- head + 1L  # 把 头节点 加 1L 存入 头节点
        ck <- key_of(cur)  # 把 key_of(当前值) 存入 ck
        if (identical(ck, key_of(goal))) {
            # 若 identical(ck, key_of(goal
            path <- list()  # 把 列表() 存入 当前路径
            k <- ck  # 把 ck 存入 下标 k
            while (!is.na(k)) {
                # 循环，直到不满足「取反 is.na(下标 k」
                path[[length(path) + 1L]] <- state_by[[k]]  # 当前路径[[长度(当前路径) 加 1L]] 小于 减 state_by[[下标 k]]
                k <- prev[[k]]  # 把 前一个[[下标 k]] 存入 下标 k
            }
            return(rev(path))  # 返回 rev(当前路径
        }
        farmer <- cur[1]  # 把 当前值[1] 存入 farmer
        for (i in 1:4) {
            # for (下标 i in 1:4) {
            if (i != 1L && cur[i] != farmer)
                next  # 若 下标 i 不等于 1L 且 当前值[下标 i] 不等于 farmer) 下一个
            nxt <- cur  # 把 当前值 存入 nxt
            nxt[1] <- 1L - farmer  # 把 1L 减 farmer 存入 nxt[1]
            if (i != 1L)
                nxt[i] <- 1L - farmer  # 若 下标 i 不等于 1L) nxt[下标 i] 小于 减 1L 减 farmer
            nk <- key_of(nxt)  # 把 key_of(nxt) 存入 nk
            if (!is.null(prev[[nk]]))
                next  # 若 取反 is.null(前一个[[nk]])) 下一个
            if (!is_safe(nxt))
                next  # 若 取反 is_safe(nxt)) 下一个
            prev[[nk]] <- ck  # 把 ck 存入 prev[[nk]]
            state_by[[nk]] <- nxt  # 把 nxt 存入 state_by[[nk]]
            q[[length(q) + 1L]] <- nxt  # 节点[[长度(节点) 加 1L]] 小于 减 nxt
        }
    }
    NULL  # NULL
}
want <- list(c(0L, 0L, 0L, 0L), c(1L, 0L, 1L, 0L), c(0L, 0L, 1L, 0L), c(1L, 1L, 1L, 0L), c(0L, 1L, 0L, 0L), c(1L,
    1L, 0L, 1L), c(0L, 1L, 0L, 1L), c(1L, 1L, 1L, 1L))
path <- solve()  # 把 solve() 存入 当前路径
stopifnot(!is.null(path))  # 断言校验
stopifnot(length(path) == length(want))  # 断言校验
for (i in seq_along(want)) {
    # for (下标 i in seq_along(want)) {
    stopifnot(identical(as.integer(path[[i]]), as.integer(want[[i]])))  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
