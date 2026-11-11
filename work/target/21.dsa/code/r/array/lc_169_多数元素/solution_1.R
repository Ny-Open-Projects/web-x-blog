# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133531071 LeetCode 169. 多数元素 — R
# 版（方案1） 定义函数 majority_element（参数：数组）
majority_element <- function(nums) {
    t <- table(nums)  # 把 table(数组) 存入 另一字符串
    as.integer(names(t)[which.max(t)])  # as.integer(names(另一字符串)[which.取较大值 另一字符串)])
}
stopifnot(majority_element(c(3, 2, 3)) == 3)  # 断言校验
stopifnot(majority_element(c(2, 2, 1, 1, 1, 2, 2)) == 2)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
