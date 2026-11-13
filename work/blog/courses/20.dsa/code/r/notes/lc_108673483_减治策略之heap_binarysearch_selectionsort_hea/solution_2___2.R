# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483 LeetCode 108673483. 减治策略 — R
# 版（方案2：快速选择求第 k 小，k 从 0 起） 定义函数 select_k（参数：数组, 左边界, 右边界, 下标 k）
select_k <- function(a, lo, hi, k) {
    if (lo == hi)
        return(a[[lo]])  # 若 左边界 等于 右边界) return(数组[[左边界]]
    pivot <- a[[hi]]  # 把 数组[[右边界]] 存入 pivot
    i <- lo  # 把 左边界 存入 下标 i
    for (j in lo:(hi - 1L)) {
        # for (下标 j in 左边界:(右边界 减 1L)) { 若 数组[[下标 j]] 不超过 pivot
        if (a[[j]] <= pivot) {
            tmp <- a[[i]]  # 把 数组[[下标 i]] 存入 临时变量
            a[[i]] <- a[[j]]  # 把 数组[[下标 j]] 存入 a[[i]]
            a[[j]] <- tmp  # 把 临时变量 存入 a[[j]]
            i <- i + 1L  # 把 下标 i 加 1L 存入 下标 i
        }
    }
    tmp <- a[[i]]  # 把 数组[[下标 i]] 存入 临时变量
    a[[i]] <- a[[hi]]  # 把 数组[[右边界]] 存入 a[[i]]
    a[[hi]] <- tmp  # 把 临时变量 存入 a[[hi]]
    # R 列表按引用不可变，用环境回传
    if (i == k)
        return(a[[i]])  # 若 下标 i 等于 下标 k) return(数组[[下标 i]]
    if (i > k)
        return(select_k_rec(a, lo, i - 1L, k))  # 若 下标 i 超过 下标 k) return(select_k_rec(数组, 左边界, 下标 i 减 1L, 下标 k
    select_k_rec(a, i + 1L, hi, k)  # select_k_rec(数组, 下标 i 加 1L, 右边界, 下标 k)
}
# R 值语义：递归用环境包装保存数组
select_k_rec <- function(a, lo, hi, k) select_k(a, lo, hi, k)  # 定义函数 select_k_rec（参数：数组, 左边界, 右边界, 下标 k）
quick_select <- function(arr, k) {
    # 定义函数 quick_select（参数：数组, 下标 k）
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$a <- as.list(arr)  # 把 as.列表(数组) 存入 e$a
    get_k <- function(lo, hi, k) {
        # 定义函数 get_k（参数：左边界, 右边界, 下标 k）
        if (lo == hi)
            return(e$a[[lo]])  # 若 左边界 等于 右边界) return(e$数组[[左边界]]
        pivot <- e$a[[hi]]  # 把 e$数组[[右边界]] 存入 pivot
        i <- lo  # 把 左边界 存入 下标 i
        for (j in lo:(hi - 1L)) {
            # for (下标 j in 左边界:(右边界 减 1L)) { 若 e$数组[[下标 j]] 不超过 pivot
            if (e$a[[j]] <= pivot) {
                tmp <- e$a[[i]]  # 把 e$数组[[下标 i]] 存入 临时变量
                e$a[[i]] <- e$a[[j]]  # 把 e$数组[[下标 j]] 存入 e$a[[i]]
                e$a[[j]] <- tmp  # 把 临时变量 存入 e$a[[j]]
                i <- i + 1L  # 把 下标 i 加 1L 存入 下标 i
            }
        }
        tmp <- e$a[[i]]  # 把 e$数组[[下标 i]] 存入 临时变量
        e$a[[i]] <- e$a[[hi]]  # 把 e$数组[[右边界]] 存入 e$a[[i]]
        e$a[[hi]] <- tmp  # 把 临时变量 存入 e$a[[hi]]
        if (i == k)
            return(e$a[[i]])  # 若 下标 i 等于 下标 k) return(e$数组[[下标 i]]
        if (i > k)
            return(get_k(lo, i - 1L, k))  # 若 下标 i 超过 下标 k) return(get_k(左边界, 下标 i 减 1L, 下标 k
        get_k(i + 1L, hi, k)  # get_k(下标 i 加 1L, 右边界, 下标 k)
    }
    get_k(1L, length(e$a), k + 1L)  # get_k(1L, 长度(e$数组), 下标 k 加 1L)
}
base <- c(3L, 1L, 4L, 1L, 5L, 9L, 2L, 6L)  # 把 字符(3L, 1L, 4L, 1L, 5L, 9L, 2L, 6L) 存入 base
cases <- list(list(2L, 2L), list(3L, 3L), list(0L, 1L), list(7L, 9L))
for (idx in seq_along(cases)) {
    # for (idx in seq_along(cases)) {
    got <- quick_select(base, cases[[idx]][[1]])  # 把 quick_select(base, cases[[idx]][[1]]) 存入 got
    stopifnot(got == cases[[idx]][[2]])  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
