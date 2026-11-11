# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134577890 LeetCode 179. 最大数 — R
# 版（方案2） 定义函数 cmp_concat_gt（参数：数组, b） a+b 是否大于 b+a（字节序，免 locale 影响）
cmp_concat_gt <- function(a, b) {
    ab <- utf8ToInt(paste0(a, b))  # 把 utf8ToInt(paste0(数组, b)) 存入 ab
    ba <- utf8ToInt(paste0(b, a))  # 把 utf8ToInt(paste0(b, 数组)) 存入 ba
    for (i in seq_along(ab)) {
        # for (下标 i in seq_along(ab)) {
        if (ab[i] != ba[i])
            return(ab[i] > ba[i])  # 若 ab[下标 i] 不等于 ba[下标 i]) return(ab[下标 i] 超过 ba[下标 i]
    }
    FALSE  # FALSE
}
largest_number <- function(nums) {
    # 定义函数 largest_number（参数：数组）
    strs <- as.character(nums)  # 把 as.character(数组) 存入 strs
    n <- length(strs)  # 把 长度(strs) 存入 元素个数
    repeat {
        # repeat {
        changed <- FALSE  # 把 FALSE 存入 changed
        for (i in 1:(n - 1)) {
            # for (下标 i in 1:(元素个数 减 1)) { 若 cmp_concat_gt(strs[下标 i 加 1], strs[下标 i]
            if (cmp_concat_gt(strs[i + 1], strs[i])) {
                t <- strs[i]
                strs[i] <- strs[i + 1]
                strs[i + 1] <- t
                changed <- TRUE  # 把 TRUE 存入 changed
            }
        }
        if (!changed)
            break  # 若 取反 changed) break
    }
    if (strs[1] == "0")
        return("0")  # 若 strs[1] 等于 「0」) return(「0」
    paste0(strs, collapse = "")  # 把 「」) 写入 paste0(strs, collapse
}
stopifnot(largest_number(c(10, 2)) == "210")  # 断言校验
stopifnot(largest_number(c(3, 30, 34, 5, 9)) == "9534330")  # 断言校验
stopifnot(largest_number(c(0, 0)) == "0")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
