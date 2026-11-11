# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760 LeetCode 1114. 按序打印 — R
# 版（方案1） 定义函数 print_in_order（参数：无）
print_in_order <- function() {
    out <- character(0)  # 把 character(0) 存入 out
    step <- 1L  # 把 1L 存入 步数
    first <- function() {
        out <<- c(out, "first")
        step <<- 2L
    }  # 定义函数 first（参数：无）
    second <- function() {
        out <<- c(out, "second")
        step <<- 3L
    }  # 定义函数 second（参数：无）
    third <- function() {
        out <<- c(out, "third")
    }  # 定义函数 third（参数：无）
    first()
    second()
    third()  # first(); second(); third()
    paste(out, collapse = "")  # 把 「」) 写入 paste(out, collapse
}
stopifnot(print_in_order() == "firstsecondthird")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
