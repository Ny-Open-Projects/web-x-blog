# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
# LeetCode LCP 10. 二叉树任务调度 — R 版（方案2：深度优先-优化）

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

dfs <- function(node) {  # 返回 c(子树总耗时, 子树最小完成时间 max_exec)
  if (is.null(node)) return(c(0, 0))  # 空子树
  left <- dfs(node$left)    # 左子树的总耗时与最小完成时间
  right <- dfs(node$right)  # 右子树的总耗时与最小完成时间
  # 当前任务自身必须独占串行跑完；孩子任务两条机器可穿插：
  # 下界取「较慢的一侧」与「两侧工作量均分到两台机器」的较大者
  parallel <- (left[1] + right[1]) / 2.0  # 两台机器均摊左右子树总工作量（浮点）
  max_exec <- node$val + max(max(left[2], right[2]), parallel)
  c(left[1] + right[1] + node$val, max_exec)
}

minimal_execution_time <- function(root) {  # 答案 = 整棵树的最小完成时间
  dfs(root)[2]
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
