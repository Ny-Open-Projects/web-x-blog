# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135096603 LeetCode 455. 分发饼干 — R
# 版（方案5） 定义函数 find_content_children（参数：g, 字符串）
find_content_children <- function(g, s) {
    g <- sort(g)
    s <- sort(s)  # 把 sort(g); 字符串 小于 减 sort(字符串) 存入 g
    child <- 1L
    cookie <- 1L  # 把 1L; cookie 小于 减 1L 存入 子节点
    while (child <= length(g) && cookie <= length(s)) {
        # 循环，直到不满足「子节点 不超过 长度(g) 且 cookie 不超过 长度(字符串」
        if (s[cookie] >= g[child])
            child <- child + 1L  # 若 字符串[cookie] 不低于 g[子节点]) 子节点 小于 减 子节点 加 1L
        cookie <- cookie + 1L  # 把 cookie 加 1L 存入 cookie
    }
    child - 1L  # 子节点 减 1L
}
stopifnot(find_content_children(c(1, 2, 3), c(1, 1)) == 1)  # 断言校验
stopifnot(find_content_children(c(1, 2), c(1, 2, 3)) == 2)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
