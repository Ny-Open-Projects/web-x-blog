# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370 LeetCode 933. 最近的请求次数 — R 版
# 方案1：push + 真出队（q[-1] 等价 TS 数组 shift）；闭包工厂保存队列状态 定义函数 RecentCounter（参数：无）
RecentCounter <- function() {
    q <- numeric(0)  # 把 numeric(0) 存入 节点
    function(t) {
        # function(另一字符串) {
        q <<- c(q, t)  # 节点 小于 小于 减 字符(节点, 另一字符串)
        while (length(q) > 0 && q[1] < t - 3000) {
            # 循环，直到不满足「长度(节点) 超过 0 且 节点[1] 小于 另一字符串 减 3000」
            q <<- q[-1]  # 真出队
        }
        length(q)  # 长度(节点)
    }
}
# 自测：与 TS 事实源内嵌用例一致
ping <- RecentCounter()  # 把 RecentCounter() 存入 ping
got <- c(ping(1), ping(100), ping(3001), ping(3002))  # 把 字符(ping(1), ping(100), ping(3001), ping(3002)) 存入 got
want <- c(1L, 2L, 3L, 3L)  # 把 字符(1L, 2L, 3L, 3L) 存入 want
stopifnot(length(got) == length(want))  # 断言校验
for (i in seq_along(want)) {
    # for (下标 i in seq_along(want)) {
    stopifnot(got[i] == want[i])  # 断言校验
}
cat("PASS\n")  # 全部用例通过，输出 PASS
