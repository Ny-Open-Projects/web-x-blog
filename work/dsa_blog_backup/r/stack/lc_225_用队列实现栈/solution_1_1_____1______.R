# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145198996 LeetCode 225. 用队列实现栈 — R
# 版（方案1） 定义函数 MyStack（参数：无）
MyStack <- function() {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$q <- integer(0)  # 把 integer(0) 存入 e$q
    e$push <- function(x) e$q <<- c(x, e$q)  # 把 function(x) e$节点 小于 小于 减 字符(x, e$节点) 存入 e$push
    e$pop <- function() {
        v <- e$q[1]
        e$q <<- e$q[-1]
        v
    }
    e$top <- function() e$q[1]  # 把 function() e$节点[1] 存入 e$top
    e$empty <- function() length(e$q) == 0  # 把 function() 长度(e$节点) 等于 0 存入 e$empty
    e
}
ms <- MyStack()  # 把 MyStack() 存入 ms
ms$push(1)
ms$push(2)  # ms$push(1); ms$push(2)
stopifnot(ms$top() == 2)  # 断言校验
stopifnot(ms$pop() == 2)  # 断言校验
stopifnot(!ms$empty())  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
