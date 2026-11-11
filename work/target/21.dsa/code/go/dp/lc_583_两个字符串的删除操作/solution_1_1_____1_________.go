// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144853278
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func minDistance(word1, word2 string) int { // 定义函数/方法 minDistance
	m, n := len(word1), len(word2) // 把 长度(word1), 长度(word2) 写入 m, n :
	dp := make([][]int, m+1)       // 把 make([][]int, 映射表 加 1) 写入 dp :
	for i := range dp {            // 把 range DP 表 { 写入 for i :
		dp[i] = make([]int, n+1) // 把 make([]int, 元素个数 加 1) 写入 dp[i]
	}
	for i := 1; i <= m; i++ { // 让 下标 i 从 1 开始计数
		c1 := word1[i-1]          // 把 word1[下标 i 减 1] 写入 c1 :
		for j := 1; j <= n; j++ { // 让 下标 j 从 1 开始计数
			c2 := word2[j-1] // 把 word2[下标 j 减 1] 写入 c2 :
			if c1 == c2 {    // 若 c1 等于 c2
				dp[i][j] = dp[i-1][j-1] + 1 // 把 DP 表[下标 i 减 1][下标 j 减 1] 加 1 写入 dp[i][j]
			} else { // 否则
				v := dp[i-1][j]     // 把 DP 表[下标 i 减 1][下标 j] 写入 v :
				if dp[i][j-1] > v { // 若 DP 表[下标 i][下标 j 减 1] 超过 值
					v = dp[i][j-1] // 把 DP 表[下标 i][下标 j 减 1] 写入 值
				}
				dp[i][j] = v // 把 值 写入 dp[i][j]
			}
		}
	}
	lcs := dp[m][n]          // 把 DP 表[映射表][元素个数] 写入 lcs :
	return m - lcs + n - lcs // 返回 映射表 减 lcs 加 元素个数 减 lcs
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		a, b string // 数组, b string
		want int    // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"sea", "eat", 2},
		{"", "", 0},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := minDistance(c.a, c.b); got != c.want { // 若 got : 赋值为 minDistance(字符.数组, 字符.b); got 不等于 字符.want
			ok = false                                                                // 把 false 写入 ok
			fmt.Printf("FAIL minDistance(%q,%q)=%v want %v\n", c.a, c.b, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
