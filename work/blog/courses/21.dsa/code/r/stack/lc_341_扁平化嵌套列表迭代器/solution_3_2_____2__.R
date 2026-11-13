# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145078849 LeetCode 341. 扁平化嵌套列表迭代器
# — R 版（方案3） 定义函数 flatten_nested（参数：nested）
flatten_nested <- function(nested) {
    out <- integer(0)  # 把 integer(0) 存入 out
    go <- function(items) {
        # 定义函数 go（参数：items） for (it in items) {
        for (it in items) {
            if (is.numeric(it) && length(it) == 1)
                out <<- c(out, it)  # 若 is.numeric(it) 且 长度(it) 等于 1) out 小于 小于 减 字符(out, it
 else go(it)  # 否则
        }
    }
    go(nested)  # go(nested)
    out  # out
}
stopifnot(identical(flatten_nested(list(1, list(2, list(3, 4)))), c(1, 2, 3, 4)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
