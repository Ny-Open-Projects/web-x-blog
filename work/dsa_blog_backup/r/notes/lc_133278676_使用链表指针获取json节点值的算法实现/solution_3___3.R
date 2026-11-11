# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676 LeetCode 133278676.
# 使用链表（指针链）获取 JSON 节点值 — R 版（方案B：逐键求值 / reduce 链式访问） 定义函数
# get_value_eval（参数：data, 当前路径）
get_value_eval <- function(data, path) {
    cur <- data  # 把 data 存入 当前值
    for (k in path) cur <- cur[[k]]  # for (下标 k in 当前路径) 当前值 小于 减 当前值[[下标 k]]
    cur  # 当前值
}
get_value_chain <- function(data, path) {
    # 定义函数 get_value_chain（参数：data, 当前路径）
    Reduce(function(acc, k) acc[[k]], path, init = data)  # 把 data) 写入 Reduce(function(acc, k) acc[[k]], path, init
}
data <- list(a = list(b = list(c = 1L)), d = list(e = 2L))
stopifnot(identical(get_value_eval(data, c("a", "b", "c")), 1L))  # 断言校验
stopifnot(identical(get_value_chain(data, c("d", "e")), 2L))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
