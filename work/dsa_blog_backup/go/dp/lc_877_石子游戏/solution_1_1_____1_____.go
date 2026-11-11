// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355902
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func stoneGame(piles []int) bool { // 定义函数/方法 stoneGame
	n := len(piles)        // 把 长度(piles) 写入 n :
	dp := make([][]int, n) // 把 make([][]int, 元素个数) 写入 dp :
	for i := range dp {
		dp[i] = make([]int, n)
	} // 把 range DP 表 { DP 表[下标 i] 赋值为 make([]int, 元素个数) } 写入 for i :
	for i := 0; i < n; i++ {
		dp[i][i] = piles[i]
	} // 让 下标 i 从 0 开始计数
	for l := 2; l <= n; l++ { // 让 左指针 从 2 开始计数
		for i := 0; i <= n-l; i++ { // 让 下标 i 从 0 开始计数
			j := i + l - 1             // 把 下标 i 加 左指针 减 1 写入 j :
			a := piles[i] - dp[i+1][j] // 把 piles[下标 i] 减 DP 表[下标 i 加 1][下标 j] 写入 a :
			b := piles[j] - dp[i][j-1] // 把 piles[下标 j] 减 DP 表[下标 i][下标 j 减 1] 写入 b :
			if a > b {
				dp[i][j] = a
			} else {
				dp[i][j] = b
			}
		}
	}
	return dp[0][n-1] > 0 // 返回 DP 表[0][元素个数 减 1] 超过 0
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		in   []int
		want bool
	}{ // 把 []struct{ in []int; want bool }{ 写入 cases :
		{[]int{5, 3, 4, 5}, true}, {[]int{3, 9, 1, 2}, true}, {[]int{1, 2}, true},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := stoneGame(c.in); got != c.want {
			ok = false
			fmt.Printf("FAIL stoneGame=%v want %v\n", got, c.want)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
