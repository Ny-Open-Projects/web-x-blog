# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133759617 LeetCode 20. 有效的括号 — R
# 版（方案12） 定义函数 is_valid（参数：字符串）
is_valid <- function(s) {
    chars <- strsplit(s, "")[[1]]  # 把 strsplit(字符串, 「」)[[1]] 存入 chars
    stack <- character(0)  # 把 character(0) 存入 栈
    pairs <- c(`)` = "(", `]` = "[", `}` = "{")  # 把 字符(「)」 赋值为 「)」, 「)」 赋值为 「)」, 「)」 赋值为 「)」) 存入 pairs
    for (ch in chars) {
        # for (字符 in chars) { 若 字符 对…取模 in 对…取模 names(pairs
        if (ch %in% names(pairs)) {
            top <- if (length(stack) > 0)
                stack[length(stack)] else "#"
            if (length(stack) > 0)
                stack <- stack[-length(stack)]  # 若 长度(栈) 超过 0) 栈 小于 减 栈[ 减 长度(栈)]
            if (top != pairs[[ch]])
                return(FALSE)  # 若 top 不等于 pairs[[字符]]) return(FALSE
        } else {
            # 否则
            stack <- c(stack, ch)  # 把 字符(栈, 字符) 存入 栈
        }
    }
    length(stack) == 0  # 把 赋值为 0 写入 length(stack)
}
tests <- c("(", "()", "()[]{}", "(]", "([)]", "abc")  # 把 字符(「(」, 「(」, 「(」, 「(」, 「(」, 「(」) 存入 tests
want <- c(FALSE, TRUE, TRUE, FALSE, FALSE, FALSE)  # 把 字符(FALSE, TRUE, TRUE, FALSE, FALSE, FALSE) 存入 want
for (i in seq_along(tests)) {
    # for (下标 i in seq_along(tests)) {
    stopifnot(is_valid(tests[i]) == want[i])  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
