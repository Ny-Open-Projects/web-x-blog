# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440 LeetCode 215. 数组中的第K个最大元素
# — R 版（方案4） 定义函数 find_kth_largest（参数：数组, 下标 k）
find_kth_largest <- function(nums, k) {
    e <- new.env(parent = emptyenv())
    e$a <- nums  # 把 new.env(parent 赋值为 emptyenv()); e$数组 小于 减 数组 存入 e
    qs <- function(l, r) {
        # 定义函数 qs（参数：左指针, 右指针）
        if (l >= r)
            return(invisible(NULL))  # 若 左指针 不低于 右指针) return(invisible(NULL
        i <- l
        j <- r  # 把 左指针; 下标 j 小于 减 右指针 存入 下标 i
        pivot <- e$a[floor((l + r)/2)]  # 把 e$数组[floor((左指针 加 右指针) 除以 2)] 存入 pivot
        while (i <= j) {
            # 循环，直到不满足「下标 i 不超过 下标 j」
            while (e$a[i] > pivot) i <- i + 1L  # 循环，直到不满足「e$数组[下标 i] 超过 pivot) 下标 i 小于 减 下标 i 加 1L」
            while (e$a[j] < pivot) j <- j - 1L  # 循环，直到不满足「e$数组[下标 j] 小于 pivot) 下标 j 小于 减 下标 j 减 1L」
            if (i <= j) {
                # 若 下标 i 不超过 下标 j
                t <- e$a[i]
                e$a[i] <- e$a[j]
                e$a[j] <- t
                i <- i + 1L
                j <- j - 1L  # 把 下标 i 加 1L; 下标 j 小于 减 下标 j 减 1L 存入 下标 i
            }
        }
        if (k <= j && l < j)
            qs(l, j)  # 若 下标 k 不超过 下标 j 且 左指针 小于 下标 j) qs(左指针, 下标 j
 else if (k >= i && i < r)
            qs(i, r)  # 否则，若 下标 k 不低于 下标 i 且 下标 i 小于 右指针) qs(下标 i, 右指针
    }
    qs(1L, length(e$a))  # qs(1L, 长度(e$数组))
    e$a[k]  # e$数组[下标 k]
}
stopifnot(find_kth_largest(c(3, 2, 1, 5, 6, 4), 2) == 5)  # 断言校验
stopifnot(find_kth_largest(c(3, 2, 3, 1, 2, 4, 5, 5, 6), 4) == 4)  # 断言校验
stopifnot(find_kth_largest(c(1), 1) == 1)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
