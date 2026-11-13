# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133657416 LeetCode 92. 反转链表II — R
# 版（方案3） 定义函数 reverse_between（参数：vals, 左边界, 右边界）
reverse_between <- function(vals, left, right) {
    v <- vals  # 把 vals 存入 值
    v[left:right] <- rev(v[left:right])  # 把 rev(值[左边界:右边界]) 存入 v[left:right]
    v
}
stopifnot(identical(reverse_between(1:5, 2, 4), c(1L, 4L, 3L, 2L, 5L)))  # 断言校验
stopifnot(identical(reverse_between(1:5, 1, 4), c(4L, 3L, 2L, 1L, 5L)))  # 断言校验
stopifnot(identical(reverse_between(5, 1, 1), 5))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
