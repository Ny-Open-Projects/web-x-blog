# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138684407 LeetCode 649. Dota2参议院 — R
# 版（方案2） 定义函数 predict_party_victory（参数：senate）
predict_party_victory <- function(senate) {
    chars <- strsplit(senate, "")[[1]]  # 把 strsplit(senate, 「」)[[1]] 存入 chars
    n <- length(chars)  # 把 长度(chars) 存入 元素个数
    radiant <- which(chars == "R") - 1L  # 把 which(chars 等于 「R」) 减 1L 存入 radiant
    dire <- which(chars != "R") - 1L  # 把 which(chars 不等于 「R」) 减 1L 存入 dire
    rh <- 1L
    dh <- 1L  # 把 1L; dh 小于 减 1L 存入 rh
    while (rh <= length(radiant) && dh <= length(dire)) {
        # 循环，直到不满足「rh 不超过 长度(radiant) 且 dh 不超过 长度(dire」
        r <- radiant[rh]
        rh <- rh + 1L  # 把 radiant[rh]; rh 小于 减 rh 加 1L 存入 右指针
        d <- dire[dh]
        dh <- dh + 1L  # 把 dire[dh]; dh 小于 减 dh 加 1L 存入 d
        if (r < d)
            radiant <- c(radiant, r + n) else dire <- c(dire, d + n)
    }
    if (rh > length(radiant))
        "Dire" else "Radiant"  # 若 rh 超过 长度(radiant)) 「Dire」 else 「Dire」
}
stopifnot(predict_party_victory("RD") == "Radiant")  # 断言校验
stopifnot(predict_party_victory("DDR") == "Dire")  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
