// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829625
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// longestCommonSubsequence 是 Python 参考 solution_1 的忠实翻译（2D DP）。
func longestCommonSubsequence(text1, text2 string) int { // 定义函数/方法 longestCommonSubsequence
	m := len(text1)          // 把 长度(text1) 写入 m :
	n := len(text2)          // 把 长度(text2) 写入 n :
	dp := make([][]int, m+1) // 把 make([][]int, 映射表 加 1) 写入 dp :
	for i := range dp {      // 把 range DP 表 { 写入 for i :
		dp[i] = make([]int, n+1) // 把 make([]int, 元素个数 加 1) 写入 dp[i]
	}
	for i := 1; i <= m; i++ { // 让 下标 i 从 1 开始计数
		c1 := text1[i-1]          // 把 text1[下标 i 减 1] 写入 c1 :
		for j := 1; j <= n; j++ { // 让 下标 j 从 1 开始计数
			c2 := text2[j-1] // 把 text2[下标 j 减 1] 写入 c2 :
			if c1 == c2 {    // 若 c1 等于 c2
				dp[i][j] = dp[i-1][j-1] + 1 // 把 DP 表[下标 i 减 1][下标 j 减 1] 加 1 写入 dp[i][j]
			} else { // 否则
				if dp[i-1][j] > dp[i][j-1] { // 若 DP 表[下标 i 减 1][下标 j] 超过 DP 表[下标 i][下标 j 减 1]
					dp[i][j] = dp[i-1][j] // 把 DP 表[下标 i 减 1][下标 j] 写入 dp[i][j]
				} else { // 否则
					dp[i][j] = dp[i][j-1] // 把 DP 表[下标 i][下标 j 减 1] 写入 dp[i][j]
				}
			}
		}
	}
	return dp[m][n] // 返回 DP 表[映射表][元素个数]
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		t1, t2 string // t1, t2 string
		want   int    // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"abcde", "ace", 3},
		{"abc", "abc", 3},
		{"abc", "def", 0},
		{"aaaaa", "bbbba", 1},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := longestCommonSubsequence(c.t1, c.t2); got != c.want {
			fmt.Printf("FAIL %q %q got=%d want=%d\n", c.t1, c.t2, got, c.want) // 打印输出
			os.Exit(1)                                                         // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
