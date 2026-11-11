// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144848405
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func numDistinct(s, t string) int { // 定义函数/方法 numDistinct
	sLen, tLen := len(s), len(t) // 把 长度(字符串), 长度(另一字符串) 写入 sLen, tLen :
	dp := make([][]int, sLen+1)  // 把 make([][]int, sLen 加 1) 写入 dp :
	for i := range dp {          // 把 range DP 表 { 写入 for i :
		dp[i] = make([]int, tLen+1) // 把 make([]int, tLen 加 1) 写入 dp[i]
	}
	for i := 0; i <= sLen; i++ { // 让 下标 i 从 0 开始计数
		dp[i][0] = 1 // 把 1 写入 dp[i][0]
	}
	for i := 1; i <= sLen; i++ { // 让 下标 i 从 1 开始计数
		for j := 1; j <= tLen; j++ { // 让 下标 j 从 1 开始计数
			if s[i-1] == t[j-1] { // 若 字符串[下标 i 减 1] 等于 另一字符串[下标 j 减 1]
				dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
			} else { // 否则
				dp[i][j] = dp[i-1][j] // 把 DP 表[下标 i 减 1][下标 j] 写入 dp[i][j]
			}
		}
	}
	return dp[sLen][tLen] // 返回 DP 表[sLen][tLen]
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		s, t string // 字符串, 另一字符串 string
		want int    // want int
	}{ // }{
		{"rabbbit", "rabbit", 3},
		{"babgbag", "bag", 5},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if g := numDistinct(c.s, c.t); g != c.want { // 若 g : 赋值为 numDistinct(字符.字符串, 字符.另一字符串); g 不等于 字符.want
			ok = false                                                 // 把 false 写入 ok
			fmt.Printf("FAIL %q,%q=%v want %v\n", c.s, c.t, g, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
