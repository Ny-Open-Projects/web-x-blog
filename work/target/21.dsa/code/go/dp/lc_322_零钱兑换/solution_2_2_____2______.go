// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144851123
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func coinChange(coins []int, amount int) int { // 定义函数/方法 coinChange
	if amount < 0 { // 若 目标金额 小于 0
		return -1 // 返回 减 1
	}
	dp := make([]int, amount+1) // 把 make([]int, 目标金额 加 1) 写入 dp :
	for i := range dp {         // 把 range DP 表 { 写入 for i :
		dp[i] = amount + 1 // 把 目标金额 加 1 写入 dp[i]
	}
	dp[0] = 0                      // 把 0 写入 dp[0]
	for a := 1; a <= amount; a++ { // 让 数组 从 1 开始计数
		for _, c := range coins { // 同时取 _ 与 字符 遍历
			if c <= a && dp[a-c]+1 < dp[a] { // 若 字符 不超过 数组 且 DP 表[数组 减 字符] 加 1 小于 DP 表[数组]
				dp[a] = dp[a-c] + 1 // 把 DP 表[数组 减 字符] 加 1 写入 dp[a]
			}
		}
	}
	if dp[amount] > amount { // 若 DP 表[目标金额] 超过 目标金额
		return -1 // 返回 减 1
	}
	return dp[amount] // 返回 DP 表[目标金额]
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		coins  []int // 硬币面额 []int
		amount int   // 目标金额 int
		want   int   // want int
	}{ // }{
		{[]int{1, 2, 5}, 11, 3},
		{[]int{2}, 3, -1},
		{[]int{1}, 0, 0},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := coinChange(c.coins, c.amount) // 把 coinChange(字符.硬币面额, 字符.目标金额) 写入 got :
		if got != c.want {                   // 若 got 不等于 字符.want
			fmt.Printf("FAIL coins=%v amount=%d want=%d got=%d\n", c.coins, c.amount, c.want, got) // 打印输出
			ok = false                                                                             // 把 false 写入 ok
		}
	}
	if !ok { // 若 取反 ok
		fmt.Println("RESULT: FAIL") // 打印输出
		os.Exit(1)                  // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
