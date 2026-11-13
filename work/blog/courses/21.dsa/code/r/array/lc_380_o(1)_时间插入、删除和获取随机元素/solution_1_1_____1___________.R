# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134255301 LeetCode 380.
# O(1)时间插入删除和获取随机元素 — R 版（方案1） 定义函数 RandomizedSet（参数：无）
RandomizedSet <- function() {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$vals <- integer(0)
    e$pos <- new.env(parent = emptyenv())
    e$insert <- function(val) {
        # 把 function(值) { 存入 e$insert
        if (!is.null(e$pos[[as.character(val)]]))
            return(FALSE)  # 若 取反 is.null(e$pos[[as.character(值)]])) return(FALSE
        e$pos[[as.character(val)]] <<- length(e$vals) + 1L  # e$pos[[as.character(值)]] 小于 小于 减 长度(e$vals) 加 1L
        e$vals <<- c(e$vals, val)  # e$vals 小于 小于 减 字符(e$vals, 值)
        TRUE  # TRUE
    }
    e$remove <- function(val) {
        # 把 function(值) { 存入 e$remove
        key <- as.character(val)  # 把 as.character(值) 存入 key
        if (is.null(e$pos[[key]]))
            return(FALSE)  # 若 is.null(e$pos[[key]])) return(FALSE
        idx <- e$pos[[key]]  # 把 e$pos[[key]] 存入 idx
        last <- e$vals[length(e$vals)]  # 把 e$vals[长度(e$vals)] 存入 last
        e$vals[idx] <<- last  # e$vals[idx] 小于 小于 减 last
        e$pos[[as.character(last)]] <<- idx  # e$pos[[as.character(last)]] 小于 小于 减 idx
        e$vals <<- e$vals[-length(e$vals)]  # e$vals 小于 小于 减 e$vals[ 减 长度(e$vals)]
        e$pos[[key]] <<- NULL  # e$pos[[key]] 小于 小于 减 NULL
        TRUE  # TRUE
    }
    e$get_random <- function() e$vals[sample(length(e$vals), 1L)]  # 把 function() e$vals[sample(长度(e$vals), 1L)] 存入 e$get_random
    e
}
set.seed(42)  # set.seed(42)
s <- RandomizedSet()  # 把 RandomizedSet() 存入 字符串
stopifnot(s$insert(1))  # 断言校验
stopifnot(!s$remove(2))  # 断言校验
stopifnot(s$insert(2))  # 断言校验
r <- s$get_random()  # 把 字符串$get_random() 存入 右指针
stopifnot(r == 1 || r == 2)  # 断言校验
stopifnot(s$remove(1))  # 断言校验
stopifnot(!s$insert(2))  # 断言校验
stopifnot(s$get_random() == 2)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
