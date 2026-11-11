# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134135902 LeetCode 344. 反转字符串 — R
# 版（方案2）
reverse_string <- function(s) paste(rev(strsplit(s, "")[[1]]), collapse = "")  # 定义函数 reverse_string（参数：字符串）
stopifnot(reverse_string("hello") == "olleh")  # 断言校验
stopifnot(reverse_string("Hannah") == "hannaH")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
