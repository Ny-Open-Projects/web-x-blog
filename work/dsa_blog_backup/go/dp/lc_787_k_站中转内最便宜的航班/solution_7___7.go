// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130717572
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// findCheapestPrice 忠实翻译 python ref solution_7___7.py（Bellman-Ford，最多 k+1 条边）
func findCheapestPrice(n int, flights [][]int, src, dst, k int) int { // 定义函数/方法 findCheapestPrice
	const INF = int64(1) << 62 // 把 int64(1) 小于 小于 62 存入 INF
	dist := make([]int64, n)   // 把 make([]int64, 元素个数) 写入 dist :
	for i := range dist {      // 把 range dist { 写入 for i :
		dist[i] = INF // 把 INF 写入 dist[i]
	}
	dist[src] = 0                       // 把 0 写入 dist[src]
	for iter := 0; iter < k+1; iter++ { // 让 iter 从 0 开始计数
		prev := make([]int64, n)    // 把 make([]int64, 元素个数) 写入 prev :
		copy(prev, dist)            // copy(前一个, dist)
		for _, f := range flights { // 同时取 _ 与 f 遍历
			frm, to, price := f[0], f[1], int64(f[2]) // 把 f[0], f[1], int64(f[2]) 写入 frm, to, price :
			if prev[frm] != INF {                     // 若 前一个[frm] 不等于 INF
				if prev[frm]+price < dist[to] { // 若 前一个[frm] 加 price 小于 dist[to]
					dist[to] = prev[frm] + price // 把 前一个[frm] 加 price 写入 dist[to]
				}
			}
		}
	}
	if dist[dst] != INF { // 若 dist[dst] 不等于 INF
		return int(dist[dst]) // 定义函数/方法 int
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
