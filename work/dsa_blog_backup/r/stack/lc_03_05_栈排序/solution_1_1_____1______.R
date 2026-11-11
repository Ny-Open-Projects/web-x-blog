# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397311 LeetCode 面试题 03.05. 栈排序 — R
# 版（方案1） 定义函数 sorted_stack（参数：input）
sorted_stack <- function(input) {
    stk <- input  # 把 input 存入 栈
    temp <- integer(0)  # 把 integer(0) 存入 临时变量
    output <- integer(0)  # 把 integer(0) 存入 输出
    while (length(stk) > 0) {
        # 循环，直到不满足「长度(栈) 超过 0」
        v <- stk[length(stk)]  # 把 栈[长度(栈)] 存入 值
        stk <- stk[-length(stk)]  # 把 栈[ 减 长度(栈)] 存入 栈
        while (length(temp) > 0 && temp[length(temp)] > v) {
            # 循环，直到不满足「长度(临时变量) 超过 0 且 临时变量[长度(临时变量)] 超过 值」
            output <- c(output, temp[length(temp)])  # 把 字符(输出, 临时变量[长度(临时变量)]) 存入 输出
            temp <- temp[-length(temp)]  # 把 临时变量[ 减 长度(临时变量)] 存入 临时变量
        }
        temp <- c(temp, v)  # 把 字符(临时变量, 值) 存入 临时变量
    }
    while (length(temp) > 0) {
        # 循环，直到不满足「长度(临时变量) 超过 0」
        output <- c(output, temp[length(temp)])  # 把 字符(输出, 临时变量[长度(临时变量)]) 存入 输出
        temp <- temp[-length(temp)]  # 把 临时变量[ 减 长度(临时变量)] 存入 临时变量
    }
    sort(output)  # sort(输出)
}
stopifnot(identical(as.integer(sorted_stack(c(5, 2, 1, 4, 3))), 1:5))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
