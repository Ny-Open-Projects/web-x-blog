# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
# LeetCode LCP 10. 二叉树任务调度 — R 版（方案1：深度优先-贪心）

new_node <- function(val) {  # 用 environment 表示节点：引用语义，队列建树时可原地挂孩子
  node <- new.env(parent = emptyenv())
  node$val <- val  # val 为自身执行时间
  node
}

build_tree <- function(vals) {  # 层序数组建树，NULL 表示空节点（list 会保留 NULL 元素）
  if (length(vals) == 0) return(NULL)
  root <- new_node(vals[[1]])
  queue <- list(root)  # 队列里只放非空节点
  i <- 2
  while (length(queue) > 0 && i <= length(vals)) {
    node <- queue[[1]]  # 出队一个父节点
    queue <- queue[-1]
    if (i <= length(vals) && !is.null(vals[[i]])) {  # 左孩子
      node$left <- new_node(vals[[i]])
      queue <- c(queue, list(node$left))
    }
    i <- i + 1
    if (i <= length(vals) && !is.null(vals[[i]])) {  # 右孩子
      node$right <- new_node(vals[[i]])
      queue <- c(queue, list(node$right))
    }
    i <- i + 1
  }
  root
}

dfs <- function(node) {  # 返回 c(子树总耗时, 两台机器并行可节省的耗时)
  if (is.null(node)) return(c(0, 0))  # 空子树：总耗时 0，节省 0
  left <- dfs(node$left)
  right <- dfs(node$right)
  a <- left[1]; b <- left[2]     # a: 左子树总耗时, b: 左子树已节省
  cc <- right[1]; d <- right[2]  # cc: 右子树总耗时（避开 R 内置函数 c 的名字）, d: 右子树已节省
  if ((cc - 2 * d <= a && a <= cc) || (a - 2 * b <= cc && cc <= a)) {
    # 一侧的串行下界落在另一侧的耗时区间内：两台机器互相填空，左右几乎完全并行
    saved <- (a + cc) / 2.0  # R 的 / 永远是浮点除法：总和为奇数时会出现 0.5
  } else if (a - 2 * b > cc) {
    # 左子树串行段太长：右子树整体塞进左边空闲的那台机器
    saved <- b + cc
  } else {
    # 右子树占主导：左子树整体塞进右边空闲的那台机器
    saved <- a + d
  }
  c(a + cc + node$val, saved)  # 加上当前节点自身的执行时间
}

minimal_execution_time <- function(root) {  # 答案 = 子树总和 - 并行节省
  r <- dfs(root)
  r[1] - r[2]
}

cases <- list(  # 三个官方用例
  list(list(47, 74, 31), 121.0),
  list(list(15, 21, NULL, 24, NULL, 27, 26), 87.0),
  list(list(1, 3, 2, NULL, NULL, 4, 4), 7.5)
)
fail <- FALSE
for (k in seq_along(cases)) {
  got <- minimal_execution_time(build_tree(cases[[k]][[1]]))
  if (abs(got - cases[[k]][[2]]) >= 1e-6) {  # 浮点比较用 1e-6 容差（与 all.equal 同口径）
    cat("FAIL got", got, "want", cases[[k]][[2]], "\n")  # 失败打印 FAIL
    fail <- TRUE
  }
}
if (fail) quit(status = 1)  # 非零退出
cat("PASS\n")  # 全部用例通过，输出 PASS
