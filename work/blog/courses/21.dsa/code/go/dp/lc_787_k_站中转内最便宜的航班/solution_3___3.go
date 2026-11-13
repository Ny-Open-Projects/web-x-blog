// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130717572
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// findCheapestPrice 忠实翻译 python ref solution_3___3.py（lru_cache 记忆化 DFS，rem 为剩余可乘边数）
func findCheapestPrice(n int, flights [][]int, src, dst, k int) int { // 定义函数/方法 findCheapestPrice
	const INF = int64(1) << 62   // 把 int64(1) 小于 小于 62 存入 INF
	graph := make([][][2]int, n) // 把 make([][][2]int, 元素个数) 写入 graph :
	for _, f := range flights {  // 同时取 _ 与 f 遍历
		graph[f[0]] = append(graph[f[0]], [2]int{f[1], f[2]}) // 把 append(graph[f[0]], [2]int{f[1], f[2]}) 写入 graph[f[0]]
	}
	memo := make(map[[2]int]int64)    // 把 make(映射表[[2]int]int64) 写入 memo :
	var dfs func(city, rem int) int64 // var dfs func(city, rem int) int64
	dfs = func(city, rem int) int64 { // 把 func(city, rem int) int64 { 写入 dfs
		if city == dst { // 若 city 等于 dst
			return 0 // 返回 0
		}
		if rem == 0 { // 若 rem 等于 0
			return INF // 返回 INF
		}
		key := [2]int{city, rem}    // 把 [2]int{city, rem} 写入 key :
		if v, ok := memo[key]; ok { // 若 值, ok : 赋值为 记忆化表[key]; ok
			return v // 返回 值
		}
		best := INF                     // 把 INF 写入 best :
		for _, e := range graph[city] { // 同时取 _ 与 e 遍历
			to, price := e[0], int64(e[1]) // 把 e[0], int64(e[1]) 写入 to, price :
			nxt := dfs(to, rem-1)          // 把 dfs(to, rem 减 1) 写入 nxt :
			if nxt != INF {                // 若 nxt 不等于 INF
				if price+nxt < best { // 若 price 加 nxt 小于 当前最优
					best = price + nxt // 把 price 加 nxt 写入 当前最优
				}
			}
		}
		memo[key] = best // 把 当前最优 写入 memo[key]
		return best      // 返回 当前最优
	}
	res := dfs(src, k+1) // 把 dfs(src, 下标 k 加 1) 写入 res :
	if res == INF {      // 若 结果 等于 INF
		return -1 // 返回 减 1
	}
	return int(res) // 定义函数/方法 int
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
