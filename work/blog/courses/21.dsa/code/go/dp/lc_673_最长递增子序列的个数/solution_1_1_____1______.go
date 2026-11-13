// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829143
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func findNumberOfLIS(nums []int) int { // 定义函数/方法 findNumberOfLIS
	n := len(nums) // 把 长度(数组) 写入 n :
	if n == 0 {    // 若 元素个数 等于 0
		return 0 // 返回 0
	}
	maxLen := 0           // 把 0 写入 maxLen :
	ans := 0              // 把 0 写入 ans :
	dp := make([]int, n)  // 把 make([]int, 元素个数) 写入 dp :
	cnt := make([]int, n) // 把 make([]int, 元素个数) 写入 cnt :
	for i := range dp {   // 把 range DP 表 { 写入 for i :
		dp[i] = 1  // 把 1 写入 dp[i]
		cnt[i] = 1 // 把 1 写入 cnt[i]
	}
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		for j := 0; j < i; j++ { // 让 下标 j 从 0 开始计数
			if nums[j] < nums[i] { // 若 数组[下标 j] 小于 数组[下标 i]
				if dp[j]+1 > dp[i] { // 若 DP 表[下标 j] 加 1 超过 DP 表[下标 i]
					dp[i] = dp[j] + 1 // 把 DP 表[下标 j] 加 1 写入 dp[i]
					cnt[i] = cnt[j]   // 把 计数[下标 j] 写入 cnt[i]
				} else if dp[j]+1 == dp[i] { // 否则，若 DP 表[下标 j] 加 1 等于 DP 表[下标 i]
					cnt[i] += cnt[j] // cnt[i]累加 计数[下标 j]
				}
			}
		}
		if dp[i] > maxLen { // 若 DP 表[下标 i] 超过 maxLen
			maxLen = dp[i] // 把 DP 表[下标 i] 写入 maxLen
			ans = cnt[i]   // 把 计数[下标 i] 写入 答案
		} else if dp[i] == maxLen { // 否则，若 DP 表[下标 i] 等于 maxLen
			ans += cnt[i] // 答案累加 计数[下标 i]
		}
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 3, 5, 4, 7}, 2},
		{[]int{2, 2, 2, 2, 2}, 5},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := findNumberOfLIS(c.in); got != c.want { // 若 got : 赋值为 findNumberOfLIS(字符.in); got 不等于 字符.want
			ok = false                                                             // 把 false 写入 ok
			fmt.Printf("FAIL findNumberOfLIS(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
