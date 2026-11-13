# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381786 LeetCode 1329. 将矩阵按对角线排序 —
# R 版
# 方案2：优化版 —— 按 r-c 分组收集对角线（偏移 +cols 转为 1 基列表下标），升序排序， 写回时按
# shift（取队首）取值；R 传值拷贝等价于 TS 的 m.map(r => r.slice()) 定义函数 diagonal_sort（参数：mat）
diagonal_sort <- function(mat) {
    rows <- length(mat)  # 把 长度(mat) 存入 行数
    cols <- length(mat[[1]])  # 把 长度(mat[[1]]) 存入 列数
    diags <- vector("list", rows + cols - 1L)  # 预分配：避免 [[key]] 读缺失下标报错
    for (r in seq_len(rows)) {
        # for (右指针 in seq_len(行数)) { for (字符 in seq_len(列数)) {
        for (c in seq_len(cols)) {
            key <- (r - 1L) - (c - 1L) + cols  # = r - c + cols，恒 >= 1
            diags[[key]] <- c(diags[[key]], mat[[r]][c])  # 把 字符(diags[[key]], mat[[右指针]][字符]) 存入 diags[[key]]
        }
    }
    for (k in seq_along(diags)) diags[[k]] <- sort(diags[[k]])
    pos <- integer(rows + cols)  # 全 0 初始化
    for (r in seq_len(rows)) {
        # for (右指针 in seq_len(行数)) { for (字符 in seq_len(列数)) {
        for (c in seq_len(cols)) {
            key <- (r - 1L) - (c - 1L) + cols  # 把 (右指针 减 1L) 减 (字符 减 1L) 加 列数 存入 key
            pos[key] <- pos[key] + 1L  # 把 pos[key] 加 1L 存入 pos[key]
            mat[[r]][c] <- diags[[key]][pos[key]]  # 把 diags[[key]][pos[key]] 存入 mat[[r]][c]
        }
    }
    mat  # mat
}
eq_matrix <- function(a, b) {
    # 定义函数 eq_matrix（参数：数组, b）
    if (length(a) != length(b))
        return(FALSE)  # 若 长度(数组) 不等于 长度(b)) return(FALSE
    for (i in seq_along(a)) {
        # for (下标 i in seq_along(数组)) {
        if (length(a[[i]]) != length(b[[i]]))
            return(FALSE)  # 若 长度(数组[[下标 i]]) 不等于 长度(b[[下标 i]])) return(FALSE
        if (!all(a[[i]] == b[[i]]))
            return(FALSE)  # 若 取反 all(数组[[下标 i]] 等于 b[[下标 i]])) return(FALSE
    }
    TRUE  # TRUE
}
# 自测：与 TS 事实源内嵌用例一致
m <- list(c(3L, 3L, 1L, 1L), c(2L, 2L, 1L, 2L), c(1L, 1L, 1L, 2L))
got <- diagonal_sort(m)  # 把 diagonal_sort(映射表) 存入 got
exp <- list(c(1L, 1L, 1L, 1L), c(1L, 2L, 2L, 2L), c(1L, 2L, 3L, 3L))
stopifnot(eq_matrix(got, exp))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
