# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145634738 LeetCode 1797. 设计一个验证系统 — R
# 版（方案1） 定义函数 AuthenticationManager（参数：ttl）
AuthenticationManager <- function(ttl) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$ttl <- ttl  # 把 ttl 存入 e$ttl
    e$expires_at <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e$expires_at
    e$generate <- function(token_id, current_time) {
        # 把 function(token_id, current_time) { 存入 e$generate
        e$expires_at[[token_id]] <<- current_time + e$ttl  # e$expires_at[[token_id]] 小于 小于 减 current_time 加 e$ttl
    }
    e$renew <- function(token_id, current_time) {
        # 把 function(token_id, current_time) { 存入 e$renew
        exp <- e$expires_at[[token_id]]  # 把 e$expires_at[[token_id]] 存入 exp
        if (!is.null(exp) && exp > current_time) {
            # 若 取反 is.null(exp) 且 exp 超过 current_time
            e$expires_at[[token_id]] <<- current_time + e$ttl  # e$expires_at[[token_id]] 小于 小于 减 current_time 加 e$ttl
        }
        e$count_valid_tokens(current_time)  # e$count_valid_tokens(current_time)
    }
    e$count_valid_tokens <- function(current_time) {
        # 把 function(current_time) { 存入 e$count_valid_tokens
        cnt <- 0L  # 把 0L 存入 计数
        for (k in ls(e$expires_at)) {
            # for (下标 k in ls(e$expires_at)) {
            if (e$expires_at[[k]] > current_time)
                cnt <- cnt + 1L  # 若 e$expires_at[[下标 k]] 超过 current_time) 计数 小于 减 计数 加 1L
        }
        cnt  # 计数
    }
    e
}
auth <- AuthenticationManager(5)  # 把 AuthenticationManager(5) 存入 auth
auth$generate("aaa", 1)  # auth$generate(「aaa」, 1)
stopifnot(auth$count_valid_tokens(3) == 1)  # 断言校验
stopifnot(auth$renew("aaa", 4) == 1)  # 断言校验
stopifnot(auth$count_valid_tokens(6) == 1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
