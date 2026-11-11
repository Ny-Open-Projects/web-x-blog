# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134368624 LeetCode 71. 简化路径 — R
# 版（方案1） 定义函数 simplify_path（参数：当前路径）
simplify_path <- function(path) {
    parts <- strsplit(path, "/")[[1]]  # 把 strsplit(当前路径, 「 除以 」)[[1]] 存入 parts
    st <- character(0)  # 把 character(0) 存入 st
    for (p in parts) {
        # for (节点 in parts) {
        if (p == "" || p == ".")
            next  # 若 节点 等于 「」 或 节点 等于 「」) 下一个
        if (p == "..")
            {
                if (length(st) > 0)
                  st <- st[-length(st)]
            }  # 若 节点 等于 「..」) { if (长度(st) 超过 0) st 小于 减 st[ 减 长度(st)] }
 else st <- c(st, p)  # 否则
    }
    if (length(st) == 0)
        return("/")  # 若 长度(st) 等于 0) return(「 除以 」
    paste0("/", paste(st, collapse = "/"))  # 把 「 除以 」)) 写入 paste0('/', paste(st, collapse
}
stopifnot(simplify_path("/home/") == "/home")  # 断言校验
stopifnot(simplify_path("/../") == "/")  # 断言校验
stopifnot(simplify_path("/home//foo/") == "/home/foo")  # 断言校验
stopifnot(simplify_path("/a/./b/../../c/") == "/c")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
