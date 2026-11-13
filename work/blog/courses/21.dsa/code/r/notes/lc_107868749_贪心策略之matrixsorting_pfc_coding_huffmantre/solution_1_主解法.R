# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107868749 LeetCode 107868749. 贪心策略 — R
# 版（贪心策略之 matrixSort / PFC 编码 / Huffman 树）
matrix_sort <- function(matrix) {
    # 定义函数 matrix_sort（参数：矩阵）
    rows <- nrow(matrix)  # 把 nrow(矩阵) 存入 行数
    cols <- ncol(matrix)  # 把 ncol(矩阵) 存入 列数
    for (c in 1:cols) {
        # for (字符 in 1:列数) {
        col <- sort(matrix[, c])  # 把 sort(矩阵[, 字符]) 存入 col
        for (r in 1:rows) matrix[r, c] <- col[r]  # for (右指针 in 1:行数) 矩阵[右指针, 字符] 小于 减 col[右指针]
    }
    for (r in 1:rows) matrix[r, ] <- sort(matrix[r, ])  # for (右指针 in 1:行数) 矩阵[右指针, ] 小于 减 sort(矩阵[右指针, ])
    matrix  # 矩阵
}
# 节点：list(freq=, sym=) 叶子 或 list(freq=, left=, right=) 内部 定义函数 build_huffman（参数：freqs）
build_huffman <- function(freqs) {
    nodes <- list()  # 把 列表() 存入 nodes
    for (nm in names(freqs)) {
        # for (nm in names(freqs)) {
        nodes[[length(nodes) + 1L]] <- list(freq = freqs[[nm]], sym = nm)
    }
    nodes <- nodes[order(vapply(nodes, function(n) n$freq, numeric(1)))]
    while (length(nodes) > 1L) {
        # 循环，直到不满足「长度(nodes) 超过 1L」
        a <- nodes[[1]]  # 把 nodes[[1]] 存入 数组
        b <- nodes[[2]]  # 把 nodes[[2]] 存入 b
        nodes <- nodes[-c(1, 2)]  # 把 nodes[ 减 字符(1, 2)] 存入 nodes
        merged <- list(freq = a$freq + b$freq, left = a, right = b)
        i <- 1L  # 把 1L 存入 下标 i
        while (i <= length(nodes) && nodes[[i]]$freq < merged$freq) i <- i + 1L
        nodes <- append(nodes, list(merged), after = i - 1L)  # 把 append(nodes, 列表(merged), after 赋值为 下标 i 减 1L) 存入 nodes
    }
    nodes[[1]]  # nodes[[1]]
}
huffman_codes <- function(freqs) {
    # 定义函数 huffman_codes（参数：freqs）
    root <- build_huffman(freqs)  # 把 build_huffman(freqs) 存入 根节点
    codes <- list()  # 把 列表() 存入 codes
    walk <- function(node, prefix) {
        # 定义函数 walk（参数：节点, prefix） 若 取反 is.null(节点$sym
        if (!is.null(node$sym)) {
            codes[[node$sym]] <<- if (nchar(prefix) == 0)
                "0" else prefix
        } else {
            # 否则
            walk(node$left, paste0(prefix, "0"))  # walk(节点$左边界, paste0(prefix, 「0」))
            walk(node$right, paste0(prefix, "1"))  # walk(节点$右边界, paste0(prefix, 「1」))
        }
    }
    walk(root, "")  # walk(根节点, 「」)
    codes  # codes
}
freqs <- list(A = 5, B = 9, C = 12, D = 13, E = 16, F = 45)
# case1: matrixSort
mat <- matrix_sort(matrix(c(5, 3, 4, 1, 6, 2, 7, 9, 8), nrow = 3, byrow = TRUE))
want <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow = 3, byrow = TRUE)
stopifnot(all(mat == want))  # 断言校验
# case2: WPL
codes <- huffman_codes(freqs)  # 把 huffman_codes(freqs) 存入 codes
wpl <- 0  # 把 0 存入 wpl
code_list <- c()  # 把 字符() 存入 code_list
for (nm in names(freqs)) {
    # for (nm in names(freqs)) {
    c <- codes[[nm]]  # 把 codes[[nm]] 存入 字符
    wpl <- wpl + freqs[[nm]] * nchar(c)  # 把 wpl 加 freqs[[nm]] 乘 nchar(字符) 存入 wpl
    code_list <- c(code_list, c)  # 把 字符(code_list, 字符) 存入 code_list
}
stopifnot(wpl == 224)  # 断言校验
# case3: 前缀无关
prefix_free <- TRUE  # 把 TRUE 存入 prefix_free
for (i in seq_along(code_list)) {
    # for (下标 i in seq_along(code_list)) { for (下标 j in seq_along(code_list)) {
    for (j in seq_along(code_list)) {
        if (i != j && substr(code_list[j], 1, nchar(code_list[i])) == code_list[i]) {
            prefix_free <- FALSE  # 把 FALSE 存入 prefix_free
        }
    }
}
stopifnot(prefix_free)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
