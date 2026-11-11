# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114011 LeetCode 232. 用栈实现队列 — R
# 版（方案1） 定义函数 MyQueue（参数：无）
MyQueue <- function() {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$in_ <- integer(0)
    e$out_ <- integer(0)  # 把 integer(0); e$out_ 小于 减 integer(0) 存入 e$in_
    in2out <- function() {
        # 定义函数 in2out（参数：无） 循环，直到不满足「长度(e$in_) 超过 0」
        while (length(e$in_) > 0) {
            e$out_ <<- c(e$out_, e$in_[length(e$in_)])  # e$out_ 小于 小于 减 字符(e$out_, e$in_[长度(e$in_)])
            e$in_ <<- e$in_[-length(e$in_)]  # e$in_ 小于 小于 减 e$in_[ 减 长度(e$in_)]
        }
    }
    e$push <- function(x) e$in_ <<- c(e$in_, x)  # 把 function(x) e$in_ 小于 小于 减 字符(e$in_, x) 存入 e$push
    e$pop <- function() {
        # 把 function() { 存入 e$pop
        if (length(e$out_) == 0)
            in2out()  # 若 长度(e$out_) 等于 0) in2out(
        v <- e$out_[length(e$out_)]  # 把 e$out_[长度(e$out_)] 存入 值
        e$out_ <<- e$out_[-length(e$out_)]  # e$out_ 小于 小于 减 e$out_[ 减 长度(e$out_)]
        v
    }
    e$peek <- function() {
        # 把 function() { 存入 e$peek
        if (length(e$out_) == 0)
            in2out()  # 若 长度(e$out_) 等于 0) in2out(
        e$out_[length(e$out_)]  # e$out_[长度(e$out_)]
    }
    e$empty <- function() length(e$in_) == 0 && length(e$out_) == 0  # 把 function() 长度(e$in_) 等于 0 且 长度(e$out_) 等于 0 存入 e$empty
    e
}
mq <- MyQueue()  # 把 MyQueue() 存入 mq
mq$push(1)
mq$push(2)  # mq$push(1); mq$push(2)
stopifnot(mq$peek() == 1)  # 断言校验
stopifnot(mq$pop() == 1)  # 断言校验
stopifnot(!mq$empty())  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
