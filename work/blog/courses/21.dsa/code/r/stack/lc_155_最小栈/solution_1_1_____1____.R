# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245934 LeetCode 155. 最小栈 — R
# 版（方案1） 定义函数 MinStack（参数：无）
MinStack <- function() {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$vals <- integer(0)
    e$mins <- integer(0)  # 把 integer(0); e$mins 小于 减 integer(0) 存入 e$vals
    e$push <- function(v) {
        # 把 function(值) { 存入 e$push
        e$vals <<- c(e$vals, v)  # e$vals 小于 小于 减 字符(e$vals, 值)
        m <- if (length(e$mins) > 0)
            min(e$mins[length(e$mins)], v) else v
        e$mins <<- c(e$mins, m)  # e$mins 小于 小于 减 字符(e$mins, 映射表)
    }
    e$pop <- function() {
        # 把 function() { 存入 e$pop
        e$vals <<- e$vals[-length(e$vals)]  # e$vals 小于 小于 减 e$vals[ 减 长度(e$vals)]
        e$mins <<- e$mins[-length(e$mins)]  # e$mins 小于 小于 减 e$mins[ 减 长度(e$mins)]
    }
    e$top <- function() e$vals[length(e$vals)]  # 把 function() e$vals[长度(e$vals)] 存入 e$top
    e$getMin <- function() e$mins[length(e$mins)]  # 把 function() e$mins[长度(e$mins)] 存入 e$getMin
    e
}
ms <- MinStack()  # 把 MinStack() 存入 ms
ms$push(-2)
ms$push(0)
ms$push(-3)  # ms$push( 减 2); ms$push(0); ms$push( 减 3)
stopifnot(ms$getMin() == -3)  # 断言校验
ms$pop()  # ms$pop()
stopifnot(ms$top() == 0, ms$getMin() == -2)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
