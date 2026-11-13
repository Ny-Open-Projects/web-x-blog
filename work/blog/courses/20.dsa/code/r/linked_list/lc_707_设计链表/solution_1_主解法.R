# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134120377 LeetCode 707. 设计链表 — R
# 版（方案1） 定义函数 MyList（参数：无）
MyList <- function() {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$items <- integer(0)  # 把 integer(0) 存入 e$items
    e$addAtHead <- function(x) e$items <<- c(x, e$items)  # 把 function(x) e$items 小于 小于 减 字符(x, e$items) 存入 e$addAtHead
    e$addAtTail <- function(x) e$items <<- c(e$items, x)  # 把 function(x) e$items 小于 小于 减 字符(e$items, x) 存入 e$addAtTail
    e$addAtIndex <- function(idx, x) {
        # 把 function(idx, x) { 存入 e$addAtIndex
        if (idx < 0)
            idx <- 1  # 若 idx 小于 0) idx 小于 减 1
        if (idx > length(e$items) + 1)
            return(invisible(NULL))  # 若 idx 超过 长度(e$items) 加 1) return(invisible(NULL
        e$items <<- append(e$items, x, after = idx)  # 把 idx) 写入 e$items <<- append(e$items, x, after
    }
    e$get <- function(idx) {
        # 把 function(idx) { 存入 e$get
        if (idx < 0 || idx >= length(e$items))
            return(-1L)  # 若 idx 小于 0 或 idx 不低于 长度(e$items)) return( 减 1L
        e$items[idx + 1]  # e$items[idx 加 1]
    }
    e$deleteAtIndex <- function(idx) {
        # 把 function(idx) { 存入 e$deleteAtIndex
        if (idx < 0 || idx >= length(e$items))
            return(invisible(NULL))  # 若 idx 小于 0 或 idx 不低于 长度(e$items)) return(invisible(NULL
        e$items <<- e$items[-(idx + 1)]  # e$items 小于 小于 减 e$items[ 减 (idx 加 1)]
    }
    e
}
l <- MyList()  # 把 MyList() 存入 左指针
l$addAtHead(1)  # 左指针$addAtHead(1)
l$addAtTail(3)  # 左指针$addAtTail(3)
l$addAtIndex(1, 2)  # 左指针$addAtIndex(1, 2)
stopifnot(l$get(1) == 2)  # 断言校验
l$deleteAtIndex(1)  # 左指针$deleteAtIndex(1)
stopifnot(l$get(1) == 3)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
