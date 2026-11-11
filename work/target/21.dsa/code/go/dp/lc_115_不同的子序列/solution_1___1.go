// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144848405
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// numDistinct 是 Python 参考 solution_1 的忠实翻译（从后往前的二维 DP）。
func numDistinct(s, t string) int { // 定义函数/方法 numDistinct
	m := len(s)              // 把 长度(字符串) 写入 m :
	n := len(t)              // 把 长度(另一字符串) 写入 n :
	dp := make([][]int, m+1) // 把 make([][]int, 映射表 加 1) 写入 dp :
	for i := range dp {      // 把 range DP 表 { 写入 for i :
		dp[i] = make([]int, n+1) // 把 make([]int, 元素个数 加 1) 写入 dp[i]
	}
	for i := 0; i <= m; i++ { // 让 下标 i 从 0 开始计数
		dp[i][n] = 1 // 把 1 写入 dp[i][n]
	}
	for i := m - 1; i >= 0; i-- { // 把 映射表 减 1; 下标 i 不低于 0; 下标 i 减一 { 写入 for i :
		for j := n - 1; j >= 0; j-- { // 把 元素个数 减 1; 下标 j 不低于 0; 下标 j 减一 { 写入 for j :
			if s[i] == t[j] { // 若 字符串[下标 i] 等于 另一字符串[下标 j]
				dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
			} else { // 否则
				dp[i][j] = dp[i+1][j] // 把 DP 表[下标 i 加 1][下标 j] 写入 dp[i][j]
			}
		}
	}
	return dp[0][0] // 返回 DP 表[0][0]
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		s, t string // 字符串, 另一字符串 string
		want int    // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"rabbbit", "rabbit", 3},
		{"babgbag", "bag", 5},
		{"a", "a", 1},
		{"abc", "", 1},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := numDistinct(c.s, c.t); got != c.want { // 若 got : 赋值为 numDistinct(字符.字符串, 字符.另一字符串); got 不等于 字符.want
			fmt.Printf("FAIL %q %q got=%d want=%d\n", c.s, c.t, got, c.want) // 打印输出
			os.Exit(1)                                                       // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
