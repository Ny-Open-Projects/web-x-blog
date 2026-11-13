# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134312127 LeetCode 383. 赎金信 — R
# 版（方案1） 定义函数 can_construct（参数：ransom, magazine）
can_construct <- function(ransom, magazine) {
    cr <- table(strsplit(ransom, "")[[1]])  # 把 table(strsplit(ransom, 「」)[[1]]) 存入 cr
    cm <- table(strsplit(magazine, "")[[1]])  # 把 table(strsplit(magazine, 「」)[[1]]) 存入 cm
    ok <- TRUE  # 把 TRUE 存入 ok
    for (ch in names(cr)) {
        # for (字符 in names(cr)) {
        need <- cr[[ch]]  # 把 cr[[字符]] 存入 need
        have <- if (ch %in% names(cm))
            cm[[ch]] else 0L  # 把 if (字符 对…取模 in 对…取模 names(cm)) cm[[字符]] else 0L 存入 have
        if (have < need)
            {
                ok <- FALSE
                break
            }  # 若 have 小于 need) { ok 小于 减 FALSE; break }
    }
    ok  # ok
}
stopifnot(!can_construct("a", "b"))  # 断言校验
stopifnot(!can_construct("aa", "ab"))  # 断言校验
stopifnot(can_construct("aa", "aab"))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
