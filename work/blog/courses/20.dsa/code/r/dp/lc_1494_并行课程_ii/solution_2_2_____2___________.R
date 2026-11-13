# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134859412 LeetCode 1494. 并行课程II — R
# 版（方案2） 定义函数 min_number_of_semesters（参数：元素个数, relations, 下标 k）
min_number_of_semesters <- function(n, relations, k) {
    prereq <- rep(0L, n)  # 把 rep(0L, 元素个数) 存入 prereq
    for (r in seq_len(nrow(relations))) {
        # for (右指针 in seq_len(nrow(relations))) {
        prereq[relations[r, 2]] <- bitwOr(prereq[relations[r, 2]], bitwShiftL(1, relations[r, 1] - 1))
    }
    go <- function(done) {
        # 定义函数 go（参数：done）
        if (done == bitwShiftL(1, n) - 1L)
            return(0L)  # 若 done 等于 bitwShiftL(1, 元素个数) 减 1L) return(0L
        avail <- 0L  # 把 0L 存入 avail
        for (i in 1:n) {
            # for (下标 i in 1:元素个数) {
            if (bitwAnd(done, bitwShiftL(1, i - 1)) == 0L && bitwAnd(done, prereq[i]) == prereq[i]) {
                avail <- bitwOr(avail, bitwShiftL(1, i - 1))  # 把 bitwOr(avail, bitwShiftL(1, 下标 i 减 1)) 存入 avail
            }
        }
        cnt <- 0L
        chosen <- 0L
        a <- avail  # 把 0L; chosen 小于 减 0L; 数组 小于 减 avail 存入 计数
        while (a != 0L && cnt < k) {
            # 循环，直到不满足「数组 不等于 0L 且 计数 小于 下标 k」
            low <- bitwAnd(a, -a)  # 把 bitwAnd(数组, 减 数组) 存入 low
            chosen <- bitwOr(chosen, low)  # 把 bitwOr(chosen, low) 存入 chosen
            a <- bitwXor(a, low)  # 把 bitwXor(数组, low) 存入 数组
            cnt <- cnt + 1L  # 把 计数 加 1L 存入 计数
        }
        1L + go(bitwOr(done, chosen))  # 1L 加 go(bitwOr(done, chosen))
    }
    go(0L)  # go(0L)
}
r1 <- matrix(c(2, 1, 3, 1, 1, 4), ncol = 2, byrow = TRUE)  # 把 矩阵(字符(2,1, 3,1, 1,4), ncol 赋值为 2, byrow 赋值为 TRUE) 存入 r1
stopifnot(min_number_of_semesters(4, r1, 2) == 3)  # 断言校验
r2 <- matrix(c(2, 1, 3, 1, 4, 1, 1, 5), ncol = 2, byrow = TRUE)
stopifnot(min_number_of_semesters(5, r2, 3) == 3)  # 断言校验
stopifnot(min_number_of_semesters(3, matrix(integer(0), ncol = 2), 2) == 2)  # 断言校验
r4 <- matrix(c(1, 2, 2, 3), ncol = 2, byrow = TRUE)  # 把 矩阵(字符(1,2, 2,3), ncol 赋值为 2, byrow 赋值为 TRUE) 存入 r4
stopifnot(min_number_of_semesters(4, r4, 1) == 4)  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
