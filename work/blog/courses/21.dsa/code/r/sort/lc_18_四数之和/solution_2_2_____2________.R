# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133894317 LeetCode 18. 四数之和 — R
# 版（方案2） 定义函数 four_sum（参数：数组, 目标值）
four_sum <- function(nums, target) {
    arr <- sort(nums)  # 把 sort(数组) 存入 数组
    res <- list()  # 把 列表() 存入 结果
    n <- length(arr)  # 把 长度(数组) 存入 元素个数
    for (i in seq_len(n)) {
        # for (下标 i in seq_len(元素个数)) {
        if (i > 1 && arr[i] == arr[i - 1])
            next  # 若 下标 i 超过 1 且 数组[下标 i] 等于 数组[下标 i 减 1]) 下一个
        for (j in (i + 1):n) {
            # for (下标 j in (下标 i 加 1):元素个数) {
            if (j > i + 1 && arr[j] == arr[j - 1])
                next  # 若 下标 j 超过 下标 i 加 1 且 数组[下标 j] 等于 数组[下标 j 减 1]) 下一个
            left <- j + 1
            right <- n  # 把 下标 j 加 1; 右边界 小于 减 元素个数 存入 左边界
            while (left < right) {
                # 循环，直到不满足「左边界 小于 右边界」
                s <- arr[i] + arr[j] + arr[left] + arr[right]  # 把 数组[下标 i] 加 数组[下标 j] 加 数组[左边界] 加 数组[右边界] 存入 字符串
                if (s == target) {
                  # 若 字符串 等于 目标值
                  res[[length(res) + 1L]] <- c(arr[i], arr[j], arr[left], arr[right])
                  left <- left + 1
                  right <- right - 1  # 把 左边界 加 1; 右边界 小于 减 右边界 减 1 存入 左边界
                  while (left < right && arr[left] == arr[left - 1]) left <- left + 1
                  while (left < right && arr[right] == arr[right + 1]) right <- right - 1
                } else if (s < target)
                  left <- left + 1  # 否则，若 字符串 小于 目标值) 左边界 小于 减 左边界 加 1
 else right <- right - 1  # 否则
            }
        }
    }
    res  # 结果
}
got <- four_sum(c(1, 0, -1, 0, -2, 2), 0)  # 把 four_sum(字符(1, 0, 减 1, 0, 减 2, 2), 0) 存入 got
stopifnot(length(got) == 3)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
