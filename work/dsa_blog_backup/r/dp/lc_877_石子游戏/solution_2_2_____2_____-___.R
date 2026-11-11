# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130709323 LeetCode 877. 石子游戏 — R
# 版（方案2）
stone_game <- function(piles) TRUE  # 定义函数 stone_game（参数：piles）
stopifnot(stone_game(c(5, 3, 4, 5)))  # 断言校验
stopifnot(stone_game(c(3, 7, 2, 3)))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
