# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135749595 LeetCode 295. 数据流的中位数 — R
# 版（方案3） 定义函数 MedianFinder（参数：无）
MedianFinder <- function() {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$low <- integer(0)  # 排序数组模拟双堆（有序插入）
    e$add_num <- function(num) {
        # 把 function(num) { 存入 e$add_num
        e$low <<- sort(c(e$low, num))  # e$low 小于 小于 减 sort(字符(e$low, num))
    }
    e$find_median <- function() {
        # 把 function() { 存入 e$find_median
        n <- length(e$low)  # 把 长度(e$low) 存入 元素个数
        if (n == 0)
            return(NA)  # 若 元素个数 等于 0) return(NA
        if (n%%2 == 1)
            e$low[(n + 1)/2] else (e$low[n/2] + e$low[n/2 + 1])/2
    }
    e
}
mf <- MedianFinder()  # 把 MedianFinder() 存入 mf
for (x in c(1, 2, 3, 4, 5)) mf$add_num(x)  # for (x in 字符(1, 2, 3, 4, 5)) mf$add_num(x)
stopifnot(mf$find_median() == 3)  # 断言校验
mf2 <- MedianFinder()  # 把 MedianFinder() 存入 mf2
mf2$add_num(1)
mf2$add_num(2)  # mf2$add_num(1); mf2$add_num(2)
stopifnot(mf2$find_median() == 1.5)  # 断言校验
mf2$add_num(3)  # mf2$add_num(3)
stopifnot(mf2$find_median() == 2)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
