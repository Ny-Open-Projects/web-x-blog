// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113951689
// LeetCode 113951689. 动态规划之 LCS — Go 版（最长公共子序列：DP 填表 + 回溯构造）
package main // 引入依赖

import "fmt" // 引入依赖

func lcsLength(a, b string) int { // 定义函数/方法 lcsLength
	m, n := len(a), len(b)   // 把 长度(数组), 长度(b) 写入 m, n :
	dp := make([][]int, m+1) // 把 make([][]int, 映射表 加 1) 写入 dp :
	for i := range dp {      // 把 range DP 表 { 写入 for i :
		dp[i] = make([]int, n+1) // 把 make([]int, 元素个数 加 1) 写入 dp[i]
	}
	for i := 1; i <= m; i++ { // 让 下标 i 从 1 开始计数
		for j := 1; j <= n; j++ { // 让 下标 j 从 1 开始计数
			if a[i-1] == b[j-1] { // 若 数组[下标 i 减 1] 等于 b[下标 j 减 1]
				dp[i][j] = dp[i-1][j-1] + 1 // 把 DP 表[下标 i 减 1][下标 j 减 1] 加 1 写入 dp[i][j]
			} else { // 否则
				dp[i][j] = dp[i-1][j]      // 把 DP 表[下标 i 减 1][下标 j] 写入 dp[i][j]
				if dp[i][j-1] > dp[i][j] { // 若 DP 表[下标 i][下标 j 减 1] 超过 DP 表[下标 i][下标 j]
					dp[i][j] = dp[i][j-1] // 把 DP 表[下标 i][下标 j 减 1] 写入 dp[i][j]
				}
			}
		}
	}
	return dp[m][n] // 返回 DP 表[映射表][元素个数]
}

func lcsString(a, b string) string { // 定义函数/方法 lcsString
	m, n := len(a), len(b)   // 把 长度(数组), 长度(b) 写入 m, n :
	dp := make([][]int, m+1) // 把 make([][]int, 映射表 加 1) 写入 dp :
	for i := range dp {      // 把 range DP 表 { 写入 for i :
		dp[i] = make([]int, n+1) // 把 make([]int, 元素个数 加 1) 写入 dp[i]
	}
	for i := 1; i <= m; i++ { // 让 下标 i 从 1 开始计数
		for j := 1; j <= n; j++ { // 让 下标 j 从 1 开始计数
			if a[i-1] == b[j-1] { // 若 数组[下标 i 减 1] 等于 b[下标 j 减 1]
				dp[i][j] = dp[i-1][j-1] + 1 // 把 DP 表[下标 i 减 1][下标 j 减 1] 加 1 写入 dp[i][j]
			} else { // 否则
				dp[i][j] = dp[i-1][j]      // 把 DP 表[下标 i 减 1][下标 j] 写入 dp[i][j]
				if dp[i][j-1] > dp[i][j] { // 若 DP 表[下标 i][下标 j 减 1] 超过 DP 表[下标 i][下标 j]
					dp[i][j] = dp[i][j-1] // 把 DP 表[下标 i][下标 j 减 1] 写入 dp[i][j]
				}
			}
		}
	}
	out := make([]byte, 0, dp[m][n]) // 把 make([]byte, 0, DP 表[映射表][元素个数]) 写入 out :
	i, j := m, n                     // 把 映射表, 元素个数 写入 i, j :
	for i > 0 && j > 0 {             // for 下标 i 超过 0 且 下标 j 超过 0 {
		if a[i-1] == b[j-1] { // 若 数组[下标 i 减 1] 等于 b[下标 j 减 1]
			out = append(out, a[i-1]) // 把 append(out, 数组[下标 i 减 1]) 写入 out
			i--                       // 下标 i 减一
			j--                       // 下标 j 减一
		} else if dp[i-1][j] >= dp[i][j-1] { // 否则，若 DP 表[下标 i 减 1][下标 j] 不低于 DP 表[下标 i][下标 j 减 1]
			i-- // 下标 i 减一
		} else { // 否则
			j-- // 下标 j 减一
		}
	}
	// 反转
	for l, r := 0, len(out)-1; l < r; l, r = l+1, r-1 {
		out[l], out[r] = out[r], out[l] // 把 out[右指针], out[左指针] 写入 out[l], out[r]
	}
	return string(out) // 定义函数/方法 string
}

func isCommonSub(a, b, s string) bool { // 定义判定函数 isCommonSub
	ia, ib := 0, 0         // 把 0, 0 写入 ia, ib :
	for _, ch := range s { // 同时取 _ 与 字符 遍历
		for ia < len(a) && a[ia] != byte(ch) { // 把 byte(字符) { 写入 for ia < len(a) && a[ia] !
			ia++ // ia 加一
		}
		for ib < len(b) && b[ib] != byte(ch) { // 把 byte(字符) { 写入 for ib < len(b) && b[ib] !
			ib++ // ib 加一
		}
		if ia >= len(a) || ib >= len(b) { // 若 ia 不低于 长度(数组) 或 ib 不低于 长度(b
			return false // 返回 false
		}
		ia++ // ia 加一
		ib++ // ib 加一
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		a, b string // 数组, b string
		want int    // want int
	}{ // }{
		{"ABCBDAB", "BDCABA", 4},
		{"AGGTAB", "GXTXAYB", 4},
		{"abc", "abc", 3},
		{"", "abc", 0},
		{"abc", "xyz", 0},
	}
	for idx, c := range cases { // 同时取 idx 与 字符 遍历
		if got := lcsLength(c.a, c.b); got != c.want { // 若 got : 赋值为 lcsLength(字符.数组, 字符.b); got 不等于 字符.want
			fmt.Printf("case %d failed: got %d want %d\n", idx, got, c.want) // 打印输出
			return                                                           // return
		}
	}
	for _, p := range [][2]string{{"ABCBDAB", "BDCABA"}, {"AGGTAB", "GXTXAYB"}} { // 同时取 _ 与 节点 遍历
		s := lcsString(p[0], p[1])                                          // 把 lcsString(节点[0], 节点[1]) 写入 s :
		if len(s) != lcsLength(p[0], p[1]) || !isCommonSub(p[0], p[1], s) { // 定义函数/方法 len
			fmt.Println("lcsString failed:", s) // 打印输出
			return                              // return
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
