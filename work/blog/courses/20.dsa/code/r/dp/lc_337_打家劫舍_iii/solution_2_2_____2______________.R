# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130671359 LeetCode 337. 打家劫舍III — R
# 版（方案2） 定义函数 rob_tree（参数：vals）
rob_tree <- function(vals) {
    if (length(vals) == 0)
        return(0L)  # 若 长度(vals) 等于 0) return(0L
    dfs <- function(i) {
        # 定义函数 dfs（参数：下标 i）
        if (i > length(vals) || is.na(vals[i]))
            return(c(0, 0))  # 若 下标 i 超过 长度(vals) 或 is.na(vals[下标 i])) return(字符(0, 0
        l <- dfs(2 * i)  # 把 dfs(2 乘 下标 i) 存入 左指针
        r <- dfs(2 * i + 1)  # 把 dfs(2 乘 下标 i 加 1) 存入 右指针
        inc <- vals[i] + l[2] + r[2]  # 把 vals[下标 i] 加 左指针[2] 加 右指针[2] 存入 inc
        exc <- max(l[1], l[2]) + max(r[1], r[2])  # 把 取较大值 左指针[1], 左指针[2]) 加 取较大值 右指针[1], 右指针[2]) 存入 exc
        c(inc, exc)  # 字符(inc, exc)
    }
    local_res <- dfs(1)  # 把 dfs(1) 存入 local_res
    as.integer(max(local_res[1], local_res[2]))  # as.integer(取较大值 local_res[1], local_res[2]))
}
t1 <- c(3, 2, 3, NA, 3, NA, 1)  # 把 字符(3, 2, 3, NA, 3, NA, 1) 存入 t1
stopifnot(rob_tree(t1) == 7)  # 断言校验
t2 <- c(3, 4, 5, 1, 3, NA, 1)  # 把 字符(3, 4, 5, 1, 3, NA, 1) 存入 t2
stopifnot(rob_tree(t2) == 9)  # 断言校验
stopifnot(rob_tree(integer(0)) == 0)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
