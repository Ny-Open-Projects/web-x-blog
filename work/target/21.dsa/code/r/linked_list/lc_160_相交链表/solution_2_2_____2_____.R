# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133922762 LeetCode 160. 相交链表 — R
# 版（方案2）
ListNode <- function(val, nxt = NULL) {
    e <- new.env(parent = emptyenv())
    e$val <- val
    e$nxt <- nxt
    class(e) <- "ListNode"
    e
}  # 定义函数 ListNode（参数：值, nxt 赋值为 NULL）
get_intersection_node <- function(headA, headB) {
    # 定义函数 get_intersection_node（参数：链表 A, 链表 B）
    if (is.null(headA) || is.null(headB))
        return(NULL)  # 若 is.null(链表 A) 或 is.null(链表 B)) return(NULL
    p1 <- headA
    p2 <- headB  # 把 链表 A; p2 小于 减 链表 B 存入 p1
    while (!identical(p1, p2)) {
        # 循环，直到不满足「取反 identical(p1, p2」
        p1 <- if (!is.null(p1))
            p1$nxt else headB  # 把 if (取反 is.null(p1)) p1$nxt else 链表 B 存入 p1
        p2 <- if (!is.null(p2))
            p2$nxt else headA  # 把 if (取反 is.null(p2)) p2$nxt else 链表 A 存入 p2
    }
    p1  # p1
}
shared <- ListNode(8, ListNode(4, ListNode(5)))  # 把 ListNode(8, ListNode(4, ListNode(5))) 存入 shared
a <- ListNode(4, ListNode(1, shared))  # 把 ListNode(4, ListNode(1, shared)) 存入 数组
b <- ListNode(5, ListNode(6, ListNode(1, shared)))  # 把 ListNode(5, ListNode(6, ListNode(1, shared))) 存入 b
stopifnot(identical(get_intersection_node(a, b), shared))  # 断言校验
stopifnot(is.null(get_intersection_node(ListNode(1), ListNode(1))))  # 断言校验
stopifnot(is.null(get_intersection_node(NULL, NULL)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
