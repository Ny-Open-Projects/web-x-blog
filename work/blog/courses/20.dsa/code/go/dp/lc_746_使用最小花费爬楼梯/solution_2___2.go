// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144853675
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func minCostClimbingStairs(cost []int) int { // 定义函数/方法 minCostClimbingStairs
	n := len(cost)           // 把 长度(cost) 写入 n :
	dp := make([]int, n)     // 把 make([]int, 元素个数) 写入 dp :
	dp[0] = cost[0]          // 把 cost[0] 写入 dp[0]
	dp[1] = cost[1]          // 把 cost[1] 写入 dp[1]
	for i := 2; i < n; i++ { // 让 下标 i 从 2 开始计数
		if dp[i-1] < dp[i-2] { // 若 DP 表[下标 i 减 1] 小于 DP 表[下标 i 减 2]
			dp[i] = dp[i-1] + cost[i] // 把 DP 表[下标 i 减 1] 加 cost[下标 i] 写入 dp[i]
		} else { // 否则
			dp[i] = dp[i-2] + cost[i] // 把 DP 表[下标 i 减 2] 加 cost[下标 i] 写入 dp[i]
		}
	}
	if dp[n-1] < dp[n-2] { // 若 DP 表[元素个数 减 1] 小于 DP 表[元素个数 减 2]
		return dp[n-1] // 返回 DP 表[元素个数 减 1]
	}
	return dp[n-2] // 返回 DP 表[元素个数 减 2]
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		cost []int // cost []int
		want int   // want int
	}{ // }{
		{[]int{10, 15, 20}, 15},
		{[]int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}, 6},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := minCostClimbingStairs(c.cost) // 把 minCostClimbingStairs(字符.cost) 写入 got :
		if got != c.want {                   // 若 got 不等于 字符.want
			fmt.Printf("FAIL: got %d expected %d\n", got, c.want) // 打印输出
			os.Exit(1)                                            // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
