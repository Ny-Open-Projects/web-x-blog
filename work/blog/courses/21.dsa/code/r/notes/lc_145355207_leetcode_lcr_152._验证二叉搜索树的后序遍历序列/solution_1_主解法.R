# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355207 LeetCode LCR 152.
# 验证二叉搜索树的后序遍历序列 — R 版（方案1） 定义函数 verify_postorder（参数：postorder） 定义函数
# check（参数：左边界, 右边界）
verify_postorder <- function(postorder) {
    check <- function(lo, hi) {
        if (hi - lo <= 1L)
            return(TRUE)  # 若 右边界 减 左边界 不超过 1L) return(TRUE
        root <- postorder[hi]  # 把 postorder[右边界] 存入 根节点
        i <- lo  # 把 左边界 存入 下标 i
        while (i < hi && postorder[i] < root) i <- i + 1L
        if (i <= hi - 1L) {
            # 若 下标 i 不超过 右边界 减 1L for (下标 j in 下标 i:(右边界 减 1L)) {
            for (j in i:(hi - 1L)) {
                if (postorder[j] < root)
                  return(FALSE)  # 若 postorder[下标 j] 小于 根节点) return(FALSE
            }
        }
        check(lo, i - 1L) && check(i, hi - 1L)  # check(左边界, 下标 i 减 1L) 且 check(下标 i, 右边界 减 1L)
    }
    check(1L, length(postorder))  # check(1L, 长度(postorder))
}
stopifnot(!verify_postorder(c(1, 6, 3, 2, 5)))  # 断言校验
stopifnot(verify_postorder(c(1, 3, 2, 4, 5)))  # 断言校验
stopifnot(verify_postorder(c(4, 6, 5, 9, 8, 7)))  # 断言校验
stopifnot(verify_postorder(c(1, 2, 3)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
