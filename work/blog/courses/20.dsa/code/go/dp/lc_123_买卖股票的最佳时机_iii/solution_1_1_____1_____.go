// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144849793
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func max(a, b int) int { // 定义函数/方法 max
	if a > b { // 若 数组 超过 b
		return a // 返回 数组
	}
	return b // 返回 b
}

func maxProfit(prices []int) int { // 定义函数/方法 maxProfit
	n := len(prices)         // 把 长度(价格序列) 写入 n :
	dp := [5]int{}           // 把 [5]int{} 写入 dp :
	dp[1] = -prices[0]       // 把 减 价格序列[0] 写入 dp[1]
	dp[3] = -prices[0]       // 把 减 价格序列[0] 写入 dp[3]
	for i := 1; i < n; i++ { // 让 下标 i 从 1 开始计数
		dp[1] = max(dp[1], dp[0]-prices[i]) // 把 取较大值 DP 表[1], DP 表[0] 减 价格序列[下标 i]) 写入 dp[1]
		dp[2] = max(dp[2], dp[1]+prices[i]) // 把 取较大值 DP 表[2], DP 表[1] 加 价格序列[下标 i]) 写入 dp[2]
		dp[3] = max(dp[3], dp[2]-prices[i]) // 把 取较大值 DP 表[3], DP 表[2] 减 价格序列[下标 i]) 写入 dp[3]
		dp[4] = max(dp[4], dp[3]+prices[i]) // 把 取较大值 DP 表[4], DP 表[3] 加 价格序列[下标 i]) 写入 dp[4]
	}
	return dp[4] // 返回 DP 表[4]
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true          // 把 true 写入 ok :
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		want int   // want int
	}{ // }{
		{[]int{1, 2, 3}, 2},
		{[]int{3, 3, 5, 0, 0, 3, 1, 4}, 6},
		{[]int{1}, 0},
		{[]int{1, 2, 4, 2, 5, 7, 2, 4, 9, 0}, 13},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := maxProfit(c.in); got != c.want { // 若 got : 赋值为 maxProfit(字符.in); got 不等于 字符.want
			ok = false                                                       // 把 false 写入 ok
			fmt.Printf("FAIL maxProfit(%v)=%d want %d\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
