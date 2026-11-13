# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145338856 LeetCode 1472. 设计浏览器历史记录 —
# R 版（方案1） 定义函数 BrowserHistory（参数：homepage）
BrowserHistory <- function(homepage) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$history <- homepage
    e$cur <- 1L  # 把 homepage; e$当前值 小于 减 1L 存入 e$history
    e$visit <- function(url) {
        # 把 function(url) { 存入 e$visit
        e$history <<- c(e$history[seq_len(e$cur)], url)  # e$history 小于 小于 减 字符(e$history[seq_len(e$当前值)], url)
        e$cur <<- length(e$history)  # e$当前值 小于 小于 减 长度(e$history)
    }
    e$back <- function(steps) {
        # 把 function(steps) { 存入 e$back
        e$cur <<- max(1L, e$cur - steps)  # e$当前值 小于 小于 减 取较大值 1L, e$当前值 减 steps)
        e$history[e$cur]  # e$history[e$当前值]
    }
    e$forward <- function(steps) {
        # 把 function(steps) { 存入 e$forward
        e$cur <<- min(length(e$history), e$cur + steps)  # e$当前值 小于 小于 减 取较小值 长度(e$history), e$当前值 加 steps)
        e$history[e$cur]  # e$history[e$当前值]
    }
    e
}
b <- BrowserHistory("leetcode.com")  # 把 BrowserHistory(「leetcode.com」) 存入 b
b$visit("google.com")
b$visit("facebook.com")
b$visit("youtube.com")
stopifnot(b$back(1) == "facebook.com")  # 断言校验
stopifnot(b$back(1) == "google.com")  # 断言校验
stopifnot(b$forward(1) == "facebook.com")  # 断言校验
b$visit("linkedin.com")  # b$visit(「linkedin.com」)
stopifnot(b$forward(2) == "linkedin.com")  # 断言校验
stopifnot(b$back(2) == "google.com")  # 断言校验
stopifnot(b$back(7) == "leetcode.com")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
