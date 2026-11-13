// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144848060
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func minDistance(w1, w2 string) int { // 定义函数/方法 minDistance
	m, n := len(w1), len(w2) // 把 长度(w1), 长度(w2) 写入 m, n :
	dp := make([][]int, m+1) // 把 make([][]int, 映射表 加 1) 写入 dp :
	for i := range dp {
		dp[i] = make([]int, n+1)
	}
	for i := 0; i <= m; i++ {
		dp[i][0] = i
	} // 让 下标 i 从 0 开始计数
	for j := 0; j <= n; j++ {
		dp[0][j] = j
	} // 让 下标 j 从 0 开始计数
	for i := 1; i <= m; i++ { // 让 下标 i 从 1 开始计数
		for j := 1; j <= n; j++ { // 让 下标 j 从 1 开始计数
			cost := 1
			if w1[i-1] == w2[j-1] {
				cost = 0
			}
			dp[i][j] = min3(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+cost)
		}
	}
	return dp[m][n] // 返回 DP 表[映射表][元素个数]
}
func min3(a, b, c int) int {
	x := a
	if b < x {
		x = b
	}
	if c < x {
		x = c
	}
	return x
} // 定义函数/方法 min3
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		a, b string
		want int
	}{ // 把 []struct{ 数组, b string; want int }{ 写入 cases :
		{"horse", "ros", 3}, {"intention", "execution", 5}, {"", "", 0},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := minDistance(c.a, c.b); got != c.want {
			ok = false
			fmt.Printf("FAIL=%v want %v\n", got, c.want)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
