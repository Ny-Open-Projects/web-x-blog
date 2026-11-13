// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113877588
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// longestManhattanPath 最长曼哈顿路径（只能向右/向下，求路径上权重之和最大）
func longestManhattanPath(grid [][]int) int { // 定义函数/方法 longestManhattanPath
	if len(grid) == 0 || len(grid[0]) == 0 { // 若 长度(网格) 等于 0 或 长度(网格[0]) 等于 0
		return 0 // 返回 0
	}
	m, n := len(grid), len(grid[0]) // 把 长度(网格), 长度(网格[0]) 写入 m, n :
	dp := make([][]int, m)          // 把 make([][]int, 映射表) 写入 dp :
	for i := range dp {             // 把 range DP 表 { 写入 for i :
		dp[i] = make([]int, n) // 把 make([]int, 元素个数) 写入 dp[i]
	}
	dp[0][0] = grid[0][0]    // 把 网格[0][0] 写入 dp[0][0]
	for i := 0; i < m; i++ { // 让 下标 i 从 0 开始计数
		for j := 0; j < n; j++ { // 让 下标 j 从 0 开始计数
			if i == 0 && j == 0 { // 若 下标 i 等于 0 且 下标 j 等于 0
				continue // 跳过本轮，进入下一次
			}
			up := -1 << 60 // 把 减 1 小于 小于 60 写入 up :
			if i > 0 {     // 若 下标 i 超过 0
				up = dp[i-1][j] // 把 DP 表[下标 i 减 1][下标 j] 写入 up
			}
			left := -1 << 60 // 把 减 1 小于 小于 60 写入 left :
			if j > 0 {       // 若 下标 j 超过 0
				left = dp[i][j-1] // 把 DP 表[下标 i][下标 j 减 1] 写入 左边界
			}
			best := up       // 把 up 写入 best :
			if left > best { // 若 左边界 超过 当前最优
				best = left // 把 左边界 写入 当前最优
			}
			dp[i][j] = grid[i][j] + best // 把 网格[下标 i][下标 j] 加 当前最优 写入 dp[i][j]
		}
	}
	return dp[m-1][n-1] // 返回 DP 表[映射表 减 1][元素个数 减 1]
}

func main() { // 程序入口：跑内嵌自测用例
	grid := [][]int{{5, 1, 3}, {2, 4, 2}, {3, 2, 1}} // 把 [][]int{{5, 1, 3}, {2, 4, 2}, {3, 2, 1}} 写入 grid :
	if longestManhattanPath(grid) != 14 {            // 若 longestManhattanPath(网格) 不等于 14
		fmt.Println("FAIL longestManhattanPath") // 打印输出
		os.Exit(1)                               // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
