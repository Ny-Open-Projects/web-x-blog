# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135533027 LeetCode 208. 实现 Trie (前缀树) —
# R 版（方案1） 定义函数 TrieNode（参数：无）
TrieNode <- function() {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$children <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e$children
    e$is_end <- FALSE  # 把 FALSE 存入 e$is_end
    e
}
Trie <- function() {
    e <- new.env(parent = emptyenv())
    e$root <- TrieNode()
    e
}  # 定义函数 Trie（参数：无）
trie_insert <- function(t, word) {
    # 定义函数 trie_insert（参数：另一字符串, 单词）
    node <- t$root  # 把 另一字符串$根节点 存入 节点
    chars <- strsplit(word, "")[[1]]  # 把 strsplit(单词, 「」)[[1]] 存入 chars
    for (ch in chars) {
        # for (字符 in chars) {
        if (is.null(node$children[[ch]]))
            node$children[[ch]] <- TrieNode()
        node <- node$children[[ch]]  # 把 节点$children[[字符]] 存入 节点
    }
    node$is_end <- TRUE  # 把 TRUE 存入 node$is_end
}
trie_walk <- function(t, s) {
    # 定义函数 trie_walk（参数：另一字符串, 字符串）
    node <- t$root  # 把 另一字符串$根节点 存入 节点
    chars <- strsplit(s, "")[[1]]  # 把 strsplit(字符串, 「」)[[1]] 存入 chars
    for (ch in chars) {
        # for (字符 in chars) {
        if (is.null(node$children[[ch]]))
            return(NULL)  # 若 is.null(节点$children[[字符]])) return(NULL
        node <- node$children[[ch]]  # 把 节点$children[[字符]] 存入 节点
    }
    node  # 节点
}
trie_search <- function(t, word) {
    n <- trie_walk(t, word)
    !is.null(n) && n$is_end
}  # 定义函数 trie_search（参数：另一字符串, 单词）
trie_starts <- function(t, prefix) !is.null(trie_walk(t, prefix))  # 定义函数 trie_starts（参数：另一字符串, prefix）
t <- Trie()  # 把 Trie() 存入 另一字符串
trie_insert(t, "apple")  # trie_insert(另一字符串, 「apple」)
stopifnot(trie_search(t, "apple"), !trie_search(t, "app"), trie_starts(t, "app"), !trie_search(t, "appl"))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
