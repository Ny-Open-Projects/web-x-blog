# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133845474 LeetCode 15. 三数之和 — R
# 版（方案1） 定义函数 three_sum（参数：数组）
three_sum <- function(nums) {
    arr <- sort(nums)  # 把 sort(数组) 存入 数组
    ans <- list()  # 把 列表() 存入 答案
    n <- length(arr)  # 把 长度(数组) 存入 元素个数
    for (first in seq_len(n)) {
        # for (first in seq_len(元素个数)) {
        if (first > 1 && arr[first] == arr[first - 1])
            next  # 若 first 超过 1 且 数组[first] 等于 数组[first 减 1]) 下一个
        third <- n  # 把 元素个数 存入 third
        target <- -arr[first]  # 把 减 数组[first] 存入 目标值
        for (second in (first + 1):n) {
            # for (second in (first 加 1):元素个数) {
            if (second > n)
                break  # 若 second 超过 元素个数) break
            if (second > first + 1 && arr[second] == arr[second - 1])
                next  # 若 second 超过 first 加 1 且 数组[second] 等于 数组[second 减 1]) 下一个
            while (second < third && arr[second] + arr[third] > target) third <- third - 1L
            if (second == third)
                break  # 若 second 等于 third) break
            if (arr[second] + arr[third] == target) {
                # 若 数组[second] 加 数组[third] 等于 目标值
                ans[[length(ans) + 1L]] <- c(arr[first], arr[second], arr[third])  # 答案[[长度(答案) 加 1L]] 小于 减 字符(数组[first], 数组[second], 数组[third])
            }
        }
    }
    ans  # 答案
}
got <- three_sum(c(-1, 0, 1, 2, -1, -4))  # 把 three_sum(字符( 减 1, 0, 1, 2, 减 1, 减 4)) 存入 got
stopifnot(length(got) == 2)  # 断言校验
got <- got[order(vapply(got, function(x) paste(x, collapse = ","), ""))]
stopifnot(identical(got[[1]], c(-1, -1, 2)))  # 断言校验
stopifnot(identical(got[[2]], c(-1, 0, 1)))  # 断言校验
g2 <- three_sum(c(0, 0, 0))  # 把 three_sum(字符(0, 0, 0)) 存入 g2
stopifnot(length(g2) == 1, identical(g2[[1]], c(0, 0, 0)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
