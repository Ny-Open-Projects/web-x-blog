# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676 LeetCode 133278676.
# 使用链表（指针链）获取 JSON 节点值 — R 版（方案A：安全遍历，缺失返回 NULL） 定义函数 get_value（参数：data,
# 当前路径）
get_value <- function(data, path) {
    node <- data  # 把 data 存入 节点
    for (key in path) {
        # for (key in 当前路径) {
        if (!is.list(node) || is.null(node[[key]]))
            return(NULL)  # 若 取反 is.列表(节点) 或 is.null(节点[[key]])) return(NULL
        node <- node[[key]]  # 把 节点[[key]] 存入 节点
    }
    node  # 节点
}
data <- list(a = list(b = list(c = 1L)), d = list(e = 2L))
stopifnot(identical(get_value(data, c("a", "b", "c")), 1L))  # 断言校验
stopifnot(is.null(get_value(data, c("a", "z"))))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
