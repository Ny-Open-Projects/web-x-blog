// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130717572
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// findCheapestPrice 忠实翻译 python ref solution_1___1.py（二维 DP：dp[i][j] 恰好经过 i 条边到达 j 的最低价格）
func findCheapestPrice(n int, flights [][]int, src, dst, k int) int { // 定义函数/方法 findCheapestPrice
	const INF = int64(1) << 62 // 把 int64(1) 小于 小于 62 存入 INF
	dp := make([][]int64, k+2) // 把 make([][]int64, 下标 k 加 2) 写入 dp :
	for i := range dp {        // 把 range DP 表 { 写入 for i :
		dp[i] = make([]int64, n) // 把 make([]int64, 元素个数) 写入 dp[i]
		for j := range dp[i] {   // 把 range DP 表[下标 i] { 写入 for j :
			dp[i][j] = INF // 把 INF 写入 dp[i][j]
		}
	}
	for i := 0; i < k+2; i++ { // 让 下标 i 从 0 开始计数
		dp[i][src] = 0 // 把 0 写入 dp[i][src]
	}
	for i := 1; i < k+2; i++ { // 让 下标 i 从 1 开始计数
		for _, f := range flights { // 同时取 _ 与 f 遍历
			frm, to, price := f[0], f[1], int64(f[2]) // 把 f[0], f[1], int64(f[2]) 写入 frm, to, price :
			if dp[i-1][frm] != INF {                  // 若 DP 表[下标 i 减 1][frm] 不等于 INF
				if dp[i-1][frm]+price < dp[i][to] { // 若 DP 表[下标 i 减 1][frm] 加 price 小于 DP 表[下标 i][to]
					dp[i][to] = dp[i-1][frm] + price // 把 DP 表[下标 i 减 1][frm] 加 price 写入 dp[i][to]
				}
			}
		}
	}
	ans := INF                 // 把 INF 写入 ans :
	for i := 1; i < k+2; i++ { // 让 下标 i 从 1 开始计数
		if dp[i][dst] < ans { // 若 DP 表[下标 i][dst] 小于 答案
			ans = dp[i][dst] // 把 DP 表[下标 i][dst] 写入 答案
		}
	}
	if ans != INF { // 若 答案 不等于 INF
		return int(ans) // 定义函数/方法 int
	}
	return -1 // 返回 减 1
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		n           int     // 元素个数 int
		flights     [][]int // flights [][]int
		src, dst, k int     // src, dst, 下标 k int
		want        int     // want int
	}{ // }{
		{4, [][]int{{0, 1, 100}, {1, 2, 100}, {2, 0, 100}, {1, 3, 600}, {2, 3, 200}}, 0, 3, 1, 700},
		{3, [][]int{{0, 1, 100}, {1, 2, 100}, {0, 2, 500}}, 0, 2, 0, 500},
		{3, [][]int{{0, 1, 100}, {1, 2, 100}, {0, 2, 500}}, 0, 2, 1, 200},
		{3, [][]int{{0, 1, 100}}, 0, 2, 3, -1},
		{3, [][]int{{0, 1, 100}}, 0, 0, 2, 0},
		{4, [][]int{{0, 1, 1}, {0, 2, 5}, {1, 2, 1}, {2, 3, 1}}, 0, 3, 1, 6},
		{5, [][]int{{0, 1, 10}, {1, 2, 10}, {2, 3, 10}, {3, 4, 10}, {0, 4, 100}, {1, 4, 50}}, 0, 4, 2, 60},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := findCheapestPrice(c.n, c.flights, c.src, c.dst, c.k); got != c.want {
			ok = false                                                                                            // 把 false 写入 ok
			fmt.Printf("FAIL solve(%d,%v,%d,%d,%d)=%d want %d\n", c.n, c.flights, c.src, c.dst, c.k, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
