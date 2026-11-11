// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144847773
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 不同路径：一维动态规划（忠实翻译 Python ref_uniquePaths）
// dp = [1]*n
// for _ in range(1, m): for j in range(1, n): dp[j] += dp[j-1]
func uniquePaths(m, n int) int { // 定义函数/方法 uniquePaths
	dp := make([]int, n) // 把 make([]int, 元素个数) 写入 dp :
	for i := range dp {  // 把 range DP 表 { 写入 for i :
		dp[i] = 1 // 把 1 写入 dp[i]
	}
	for r := 1; r < m; r++ { // 让 右指针 从 1 开始计数
		for j := 1; j < n; j++ { // 让 下标 j 从 1 开始计数
			dp[j] += dp[j-1] // dp[j]累加 DP 表[下标 j 减 1]
		}
	}
	return dp[n-1] // 返回 DP 表[元素个数 减 1]
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct{ m, n, want int }                // 定义类型
	cases := []tc{{3, 7, 28}, {3, 2, 3}, {1, 1, 1}} // 把 []tc{{3, 7, 28}, {3, 2, 3}, {1, 1, 1}} 写入 cases :
	ok := true                                      // 把 true 写入 ok :
	for _, c := range cases {                       // 同时取 _ 与 字符 遍历
		got := uniquePaths(c.m, c.n) // 把 uniquePaths(字符.映射表, 字符.元素个数) 写入 got :
		if got != c.want {           // 若 got 不等于 字符.want
			fmt.Printf("FAIL: uniquePaths(%d,%d)=%d want %d\n", c.m, c.n, got, c.want) // 打印输出
			ok = false                                                                 // 把 false 写入 ok
		}
	}
	if !ok { // 若 取反 ok
		fmt.Println("FAIL") // 打印输出
		os.Exit(1)          // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
