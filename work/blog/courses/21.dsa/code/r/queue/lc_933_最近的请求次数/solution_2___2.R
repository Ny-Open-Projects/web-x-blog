# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370 LeetCode 933. 最近的请求次数 — R 版
# 方案2：front 指针懒删除（不真正移除元素，仅移动队头下标） 定义函数 RecentCounter（参数：无）
RecentCounter <- function() {
    queue <- numeric(0)  # 把 numeric(0) 存入 队列
    front <- 0L  # 已懒删除的元素个数（0 基）
    function(t) {
        # function(另一字符串) {
        queue <<- c(queue, t)  # 队列 小于 小于 减 字符(队列, 另一字符串)
        while (queue[front + 1L] < t - 3000) {
            # 循环，直到不满足「队列[front 加 1L] 小于 另一字符串 减 3000」
            front <<- front + 1L  # front 小于 小于 减 front 加 1L
        }
        length(queue) - front  # 长度(队列) 减 front
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
