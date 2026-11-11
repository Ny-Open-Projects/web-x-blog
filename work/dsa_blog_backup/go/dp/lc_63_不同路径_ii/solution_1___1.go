// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130713079
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func uniquePathsWithObstacles(grid [][]int) int { // 定义函数/方法 uniquePathsWithObstacles
	m, n := len(grid), len(grid[0]) // 把 长度(网格), 长度(网格[0]) 写入 m, n :
	dp := make([][]int, m)          // 把 make([][]int, 映射表) 写入 dp :
	for i := range dp {             // 把 range DP 表 { 写入 for i :
		dp[i] = make([]int, n) // 把 make([]int, 元素个数) 写入 dp[i]
	}
	for i := 0; i < m; i++ { // 让 下标 i 从 0 开始计数
		if grid[i][0] == 0 { // 若 网格[下标 i][0] 等于 0
			dp[i][0] = 1 // 把 1 写入 dp[i][0]
		} else { // 否则
			break // 跳出循环
		}
	}
	for j := 0; j < n; j++ { // 让 下标 j 从 0 开始计数
		if grid[0][j] == 0 { // 若 网格[0][下标 j] 等于 0
			dp[0][j] = 1 // 把 1 写入 dp[0][j]
		} else { // 否则
			break // 跳出循环
		}
	}
	for i := 1; i < m; i++ { // 让 下标 i 从 1 开始计数
		for j := 1; j < n; j++ { // 让 下标 j 从 1 开始计数
			if grid[i][j] == 1 { // 若 网格[下标 i][下标 j] 等于 1
				continue // 跳过本轮，进入下一次
			}
			dp[i][j] = dp[i-1][j] + dp[i][j-1] // 把 DP 表[下标 i 减 1][下标 j] 加 DP 表[下标 i][下标 j 减 1] 写入 dp[i][j]
		}
	}
	return dp[m-1][n-1] // 返回 DP 表[映射表 减 1][元素个数 减 1]
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   [][]int // in [][]int
		want int     // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[][]int{{0, 0, 0}, {0, 1, 0}, {0, 0, 0}}, 2},
		{[][]int{{1, 0}}, 0},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := uniquePathsWithObstacles(c.in); got != c.want { // 若 got : 赋值为 uniquePathsWithObstacles(字符.in); got 不等于 字符.want
			ok = false                                                                      // 把 false 写入 ok
			fmt.Printf("FAIL uniquePathsWithObstacles(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
