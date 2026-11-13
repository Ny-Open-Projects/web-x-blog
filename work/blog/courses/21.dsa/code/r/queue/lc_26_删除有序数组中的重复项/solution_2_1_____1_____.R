# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114454 LeetCode 26. 删除有序数组中的重复项
# — R 版
# 方案2：快慢指针 —— fast 扫描，slow 指向已去重区间末尾 定义函数 remove_duplicates（参数：数组）
remove_duplicates <- function(nums) {
    if (length(nums) == 0)
        return(list(k = 0L, nums = nums))  # 若 长度(数组) 等于 0) return(列表(下标 k 赋值为 0L, 数组 赋值为 数组
    slow <- 1L  # 把 1L 存入 慢指针
    for (fast in seq_along(nums)[-1]) {
        # for (快指针 in seq_along(数组)[ 减 1]) { 若 数组[快指针] 不等于 数组[慢指针]
        if (nums[fast] != nums[slow]) {
            slow <- slow + 1L  # 把 慢指针 加 1L 存入 慢指针
            nums[slow] <- nums[fast]  # 把 数组[快指针] 存入 nums[slow]
        }
    }
    list(k = slow, nums = nums)  # 把 慢指针, 数组 赋值为 数组) 写入 list(k
}
eq_arr <- function(a, b) {
    # 定义函数 eq_arr（参数：数组, b）
    length(a) == length(b) && (length(a) == 0 || all(a == b))  # 把 赋值为 长度(b) 且 (长度(数组) 等于 0 或 all(数组 等于 b)) 写入 length(a)
}
# 自测：与 TS 事实源内嵌用例一致
cases <- list(list(input = c(1L, 1L, 2L), k = 2L, pre = c(1L, 2L)), list(input = c(1L, 2L, 3L), k = 3L, pre = c(1L,
    2L, 3L)), list(input = integer(0), k = 0L, pre = integer(0))  # 把 integer(0), 下标 k 赋值为 0L, 前缀和 赋值为 integer(0)) 写入 list(input
)
for (cs in cases) {
    # for (cs in cases) {
    res <- remove_duplicates(cs$input)  # 把 remove_duplicates(cs$input) 存入 结果
    prefix <- res$nums[seq_len(res$k)]  # 把 结果$数组[seq_len(结果$下标 k)] 存入 prefix
    stopifnot(res$k == cs$k, eq_arr(prefix, cs$pre))  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
