# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400 LeetCode 347. 前K个高频元素 — R
# 版（方案1） 定义函数 top_k_frequent（参数：数组, 下标 k）
top_k_frequent <- function(nums, k) {
    counts <- table(nums)  # 把 table(数组) 存入 counts
    items <- data.frame(v = as.integer(names(counts)), c = as.integer(counts))
    items <- items[order(-items$c, items$v), ]  # 把 items[order( 减 items$字符, items$值), ] 存入 items
    head(items$v, k)  # 头节点(items$值, 下标 k)
}
got <- sort(top_k_frequent(c(1, 1, 1, 2, 2, 3), 2))  # 把 sort(top_k_frequent(字符(1, 1, 1, 2, 2, 3), 2)) 存入 got
stopifnot(identical(got, c(1L, 2L)))  # 断言校验
stopifnot(identical(top_k_frequent(c(1), 1), 1L))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
