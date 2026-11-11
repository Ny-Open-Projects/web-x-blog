# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489 LeetCode 133270489. 原型链原理 — R
# 版（方案4：null/undefined 边界：instanceOf 均返回 false） 定义函数 instance_of（参数：数组, b）
instance_of <- function(a, b) {
    p <- a  # 把 数组 存入 节点
    while (!is.null(p)) {
        # 循环，直到不满足「取反 is.null(节点」
        if (identical(p, b$prototype))
            return(TRUE)  # 若 identical(节点, b$prototype)) return(TRUE
        p <- p$`__proto__`
    }
    FALSE  # FALSE
}
ctor <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 ctor
ctor$prototype <- NULL  # 把 NULL 存入 ctor$prototype
stopifnot(!instance_of(NULL, ctor))  # 断言校验
stopifnot(!instance_of(NULL, ctor))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
