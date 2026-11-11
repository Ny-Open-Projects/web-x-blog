// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130713079
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func uniquePathsWithObstacles(obstacleGrid [][]int) int { // 定义函数/方法 uniquePathsWithObstacles
	m := len(obstacleGrid)       // 把 长度(obstacleGrid) 写入 m :
	n := len(obstacleGrid[0])    // 把 长度(obstacleGrid[0]) 写入 n :
	f := make([]int, n)          // 把 make([]int, 元素个数) 写入 f :
	if obstacleGrid[0][0] == 0 { // 若 obstacleGrid[0][0] 等于 0
		f[0] = 1 // 把 1 写入 f[0]
	}
	for j := 1; j < n; j++ { // 让 下标 j 从 1 开始计数
		if obstacleGrid[0][j] == 1 || f[j-1] == 0 { // 若 obstacleGrid[0][下标 j] 等于 1 或 f[下标 j 减 1] 等于 0
			f[j] = 0 // 把 0 写入 f[j]
		} else { // 否则
			f[j] = f[j-1] // 把 f[下标 j 减 1] 写入 f[j]
		}
	}
	for i := 1; i < m; i++ { // 让 下标 i 从 1 开始计数
		for j := 0; j < n; j++ { // 让 下标 j 从 0 开始计数
			if obstacleGrid[i][j] == 1 { // 若 obstacleGrid[下标 i][下标 j] 等于 1
				f[j] = 0 // 把 0 写入 f[j]
			} else if j > 0 { // 否则，若 下标 j 超过 0
				f[j] += f[j-1] // f[j]累加 f[下标 j 减 1]
			}
		}
	}
	return f[n-1] // 返回 f[元素个数 减 1]
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   [][]int // in [][]int
		want int     // want int
	}{ // }{
		{[][]int{{0, 0, 0}, {0, 1, 0}, {0, 0, 0}}, 2},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if g := uniquePathsWithObstacles(c.in); g != c.want { // 若 g : 赋值为 uniquePathsWithObstacles(字符.in); g 不等于 字符.want
			ok = false                                          // 把 false 写入 ok
			fmt.Printf("FAIL %v=%v want %v\n", c.in, g, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
