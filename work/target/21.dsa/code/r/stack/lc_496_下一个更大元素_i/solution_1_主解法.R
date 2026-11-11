# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145012016 LeetCode 496. 下一个更大元素 I — R
# 版（方案1） 定义函数 next_greater_element（参数：数组1, 数组2）
next_greater_element <- function(nums1, nums2) {
    nxt <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 nxt
    st <- integer(0)  # 把 integer(0) 存入 st
    for (v in nums2) {
        # for (值 in 数组2) { 循环，直到不满足「长度(st) 超过 0 且 st[长度(st)] 小于 值」
        while (length(st) > 0 && st[length(st)] < v) {
            nxt[[as.character(st[length(st)])]] <- v  # 把 值 存入 nxt[[as.character(st[length(st)])]]
            st <- st[-length(st)]  # 把 st[ 减 长度(st)] 存入 st
        }
        st <- c(st, v)  # 把 字符(st, 值) 存入 st
    }
    sapply(nums1, function(v) {
        # sapply(数组1, function(值) {
        key <- as.character(v)  # 把 as.character(值) 存入 key
        if (!is.null(nxt[[key]]))
            nxt[[key]] else -1L  # 若 取反 is.null(nxt[[key]])) nxt[[key]] else 减 1L
    })  # })
}
stopifnot(identical(as.integer(next_greater_element(c(4, 1, 2), c(1, 3, 4, 2))), c(-1L, 3L, -1L)))  # 断言校验
stopifnot(identical(as.integer(next_greater_element(c(2, 4), c(1, 2, 3, 4))), c(3L, -1L)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
