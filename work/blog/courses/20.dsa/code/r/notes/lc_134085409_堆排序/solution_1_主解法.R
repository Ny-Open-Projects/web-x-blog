# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085409 数据结构与算法之排序: 堆排序 — R
# 版（方案1） 定义函数 heap_sort（参数：数组）
heap_sort <- function(nums) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$v <- nums  # 把 数组 存入 e$v
    n <- length(nums)  # 把 长度(数组) 存入 元素个数
    sift <- function(start, end_) {
        # 定义函数 sift（参数：起点, end_）
        root <- start  # 把 起点 存入 根节点
        while (TRUE) {
            # 循环，直到不满足「TRUE」
            child <- 2L * root  # 把 2L 乘 根节点 存入 子节点
            if (child > end_)
                break  # 若 子节点 超过 end_) break
            swap <- root  # 把 根节点 存入 swap
            if (e$v[swap] < e$v[child])
                swap <- child  # 若 e$值[swap] 小于 e$值[子节点]) swap 小于 减 子节点
            if (child + 1L <= end_ && e$v[swap] < e$v[child + 1L])
                swap <- child + 1L
            if (swap == root)
                break  # 若 swap 等于 根节点) break
            t <- e$v[root]  # 把 e$值[根节点] 存入 另一字符串
            e$v[root] <- e$v[swap]  # 把 e$值[swap] 存入 e$v[root]
            e$v[swap] <- t  # 把 另一字符串 存入 e$v[swap]
            root <- swap  # 把 swap 存入 根节点
        }
    }
    if (n >= 2) {
        # 若 元素个数 不低于 2
        for (i in (n%/%2L):1) sift(i, n)  # for (下标 i in (元素个数 对…取模 除以 对…取模 2L):1) sift(下标 i, 元素个数)
        for (end_ in n:2) {
            # for (end_ in 元素个数:2) {
            t <- e$v[1]  # 把 e$值[1] 存入 另一字符串
            e$v[1] <- e$v[end_]  # 把 e$值[end_] 存入 e$v[1]
            e$v[end_] <- t  # 把 另一字符串 存入 e$v[end_]
            sift(1, end_ - 1L)  # sift(1, end_ 减 1L)
        }
    }
    e$v  # e$值
}
stopifnot(identical(as.integer(heap_sort(c(5, 2, 4, 6, 1, 3))), 1:6))  # 断言校验
stopifnot(identical(as.integer(heap_sort(c(9, 8, 7, 6, 5))), 5:9))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
