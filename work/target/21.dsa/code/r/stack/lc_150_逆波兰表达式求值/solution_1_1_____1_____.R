# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130726302 LeetCode 150. 逆波兰表达式求值 — R
# 版（方案1） 定义函数 eval_rpn（参数：tokens）
eval_rpn <- function(tokens) {
    st <- numeric(0)  # 把 numeric(0) 存入 st
    for (t in tokens) {
        # for (另一字符串 in tokens) { 若 另一字符串 对…取模 in 对…取模 字符(「 加 」, 「 加 」, 「 加 」, 「
        # 加 」
        if (t %in% c("+", "-", "*", "/")) {
            b <- st[length(st)]
            st <- st[-length(st)]  # 把 st[长度(st)]; st 小于 减 st[ 减 长度(st)] 存入 b
            a <- st[length(st)]
            st <- st[-length(st)]  # 把 st[长度(st)]; st 小于 减 st[ 减 长度(st)] 存入 数组
            if (t == "+")
                r <- a + b  # 若 另一字符串 等于 「 加 」) 右指针 小于 减 数组 加 b
 else if (t == "-")
                r <- a - b  # 否则，若 另一字符串 等于 「 减 」) 右指针 小于 减 数组 减 b
 else if (t == "*")
                r <- a * b  # 否则，若 另一字符串 等于 「 乘 」) 右指针 小于 减 数组 乘 b
 else {
                # 否则
                q <- a/b  # 把 数组 除以 b 存入 节点
                r <- if (q >= 0)
                  floor(q) else ceiling(q)  # 把 if (节点 不低于 0) floor(节点) else ceiling(节点) 存入 右指针
            }
            st <- c(st, r)  # 把 字符(st, 右指针) 存入 st
        } else {
            # 否则
            st <- c(st, as.numeric(t))  # 把 字符(st, as.numeric(另一字符串)) 存入 st
        }
    }
    st[1]  # st[1]
}
stopifnot(eval_rpn(c("2", "1", "+", "3", "*")) == 9)  # 断言校验
stopifnot(eval_rpn(c("4", "13", "5", "/", "+")) == 6)  # 断言校验
stopifnot(eval_rpn(c("10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+")) == 22)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
