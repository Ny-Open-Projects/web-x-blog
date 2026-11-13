// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func climbStairsCount(h int) int { // 定义函数/方法 climbStairsCount
	if h < 0 {
		return 0
	} // 若 h 小于 0 { return 0 }
	if h == 0 {
		return 1
	} // 若 h 等于 0 { return 1 }
	if h == 1 {
		return 1
	} // 若 h 等于 1 { return 1 }
	if h == 2 {
		return 2
	} // 若 h 等于 2 { return 2 }
	dp := make([]int, h+1)        // 把 make([]int, h 加 1) 写入 dp :
	dp[0], dp[1], dp[2] = 1, 1, 2 // 把 1, 1, 2 写入 dp[0], dp[1], dp[2]
	for i := 3; i <= h; i++ {     // 让 下标 i 从 3 开始计数
		dp[i] = dp[i-1] + dp[i-2] + dp[i-3] // 把 DP 表[下标 i 减 1] 加 DP 表[下标 i 减 2] 加 DP 表[下标 i 减 3] 写入 dp[i]
	}
	return dp[h] // 返回 DP 表[h]
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		h    int
		want int
	}{ // 把 []struct{ h int; want int }{ 写入 cases :
		{4, 7},
		{6, 24},
		{10, 274},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := climbStairsCount(c.h); got != c.want { // 若 got : 赋值为 climbStairsCount(字符.h); got 不等于 字符.want
			ok = false
			fmt.Printf("FAIL h=%d got %d want %d\n", c.h, got, c.want) // 打印输出
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
