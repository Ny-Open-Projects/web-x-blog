# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107849059 Gnome Sort（侏儒排序）+ Bubble
# Sort（冒泡排序）+ 贪心找零 对比 定义函数 gnome_sort（参数：数组）
gnome_sort <- function(arr) {
    a <- as.list(arr)  # 把 as.列表(数组) 存入 数组
    i <- 1L  # 把 1L 存入 下标 i
    n <- length(a)  # 把 长度(数组) 存入 元素个数
    while (i <= n) {
        # 循环，直到不满足「下标 i 不超过 元素个数」 若 下标 i 等于 1L 或 数组[[下标 i]] 不低于 数组[[下标 i
        # 减 1L]]
        if (i == 1L || a[[i]] >= a[[i - 1L]]) {
            i <- i + 1L  # 把 下标 i 加 1L 存入 下标 i
        } else {
            # 否则
            tmp <- a[[i - 1L]]  # 把 数组[[下标 i 减 1L]] 存入 临时变量
            a[[i - 1L]] <- a[[i]]  # 数组[[下标 i 减 1L]] 小于 减 数组[[下标 i]]
            a[[i]] <- tmp  # 把 临时变量 存入 a[[i]]
            i <- i - 1L  # 把 下标 i 减 1L 存入 下标 i
        }
    }
    as.integer(vapply(a, function(x) x, integer(1)))  # as.integer(vapply(数组, function(x) x, integer(1)))
}
bubble_sort <- function(arr) {
    # 定义函数 bubble_sort（参数：数组）
    a <- as.list(arr)  # 把 as.列表(数组) 存入 数组
    n <- length(a)  # 把 长度(数组) 存入 元素个数
    swapped <- TRUE  # 把 TRUE 存入 swapped
    while (swapped) {
        # 循环，直到不满足「swapped」
        swapped <- FALSE  # 把 FALSE 存入 swapped
        for (i in 1:(n - 1L)) {
            # for (下标 i in 1:(元素个数 减 1L)) { 若 数组[[下标 i]] 超过 数组[[下标 i 加 1L]]
            if (a[[i]] > a[[i + 1L]]) {
                tmp <- a[[i]]  # 把 数组[[下标 i]] 存入 临时变量
                a[[i]] <- a[[i + 1L]]  # 把 数组[[下标 i 加 1L]] 存入 a[[i]]
                a[[i + 1L]] <- tmp  # 数组[[下标 i 加 1L]] 小于 减 临时变量
                swapped <- TRUE  # 把 TRUE 存入 swapped
            }
        }
    }
    as.integer(vapply(a, function(x) x, integer(1)))  # as.integer(vapply(数组, function(x) x, integer(1)))
}
coin_change <- function(coins, amount) {
    # 定义函数 coin_change（参数：硬币面额, 目标金额）
    cs <- sort(coins, decreasing = TRUE)  # 把 sort(硬币面额, decreasing 赋值为 TRUE) 存入 cs
    remaining <- amount  # 把 目标金额 存入 remaining
    count <- 0L  # 把 0L 存入 计数
    for (coin in cs) {
        # for (coin in cs) { 循环，直到不满足「remaining 不低于 coin」
        while (remaining >= coin) {
            remaining <- remaining - coin  # 把 remaining 减 coin 存入 remaining
            count <- count + 1L  # 把 计数 加 1L 存入 计数
        }
    }
    if (remaining == 0)
        count else -1L  # 若 remaining 等于 0) 计数 else 减 1L
}
g <- gnome_sort(c(3L, 2L, 1L))  # 把 gnome_sort(字符(3L, 2L, 1L)) 存入 g
stopifnot(identical(as.integer(g), 1:3))  # 断言校验
b <- bubble_sort(c(3L, 2L, 1L))  # 把 bubble_sort(字符(3L, 2L, 1L)) 存入 b
stopifnot(identical(as.integer(b), 1:3))  # 断言校验
stopifnot(coin_change(c(1L, 5L, 10L, 25L), 63L) == 6L)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
