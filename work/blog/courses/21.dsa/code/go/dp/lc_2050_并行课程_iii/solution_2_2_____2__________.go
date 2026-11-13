// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145380834
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// minimumTime 是 Python 参考 solution_2 的忠实翻译（拓扑排序 DP，使用 earliest 命名）。
func minimumTime(n int, relations [][]int, time []int) int { // 定义函数/方法 minimumTime
	graph := make([][]int, n+1)   // 把 make([][]int, 元素个数 加 1) 写入 graph :
	indeg := make([]int, n+1)     // 把 make([]int, 元素个数 加 1) 写入 indeg :
	for _, r := range relations { // 同时取 _ 与 右指针 遍历
		u, v := r[0], r[1]             // 把 右指针[0], 右指针[1] 写入 u, v :
		graph[u] = append(graph[u], v) // 把 append(graph[节点 u], 值) 写入 graph[u]
		indeg[v]++                     // indeg[值] 加一
	}
	earliest := make([]int, n+1) // 把 make([]int, 元素个数 加 1) 写入 earliest :
	for i := 1; i <= n; i++ {    // 让 下标 i 从 1 开始计数
		earliest[i] = time[i-1] // 把 time[下标 i 减 1] 写入 earliest[i]
	}
	queue := []int{}          // 把 []int{} 写入 queue :
	for i := 1; i <= n; i++ { // 让 下标 i 从 1 开始计数
		if indeg[i] == 0 { // 若 indeg[下标 i] 等于 0
			queue = append(queue, i) // 把 append(队列, 下标 i) 写入 队列
		}
	}
	for len(queue) > 0 { // for 长度(队列) 超过 0 {
		u := queue[0]                // 把 队列[0] 写入 u :
		queue = queue[1:]            // 把 队列[1:] 写入 队列
		for _, v := range graph[u] { // 同时取 _ 与 值 遍历
			if earliest[u]+time[v-1] > earliest[v] { // 若 earliest[节点 u] 加 time[值 减 1] 超过 earliest[值]
				earliest[v] = earliest[u] + time[v-1] // 把 earliest[节点 u] 加 time[值 减 1] 写入 earliest[v]
			}
			indeg[v]--         // indeg[值] 减一
			if indeg[v] == 0 { // 若 indeg[值] 等于 0
				queue = append(queue, v) // 把 append(队列, 值) 写入 队列
			}
		}
	}
	ans := 0                  // 把 0 写入 ans :
	for i := 1; i <= n; i++ { // 让 下标 i 从 1 开始计数
		if earliest[i] > ans { // 若 earliest[下标 i] 超过 答案
			ans = earliest[i] // 把 earliest[下标 i] 写入 答案
		}
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		n         int     // 元素个数 int
		relations [][]int // relations [][]int
		time      []int   // time []int
		want      int     // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{3, [][]int{{1, 3}, {2, 3}}, []int{3, 2, 5}, 8},
		{3, [][]int{}, []int{1, 2, 3}, 3},
		{2, [][]int{{1, 2}}, []int{1, 2}, 3},
		{5, [][]int{{1, 2}, {2, 3}, {3, 4}, {4, 5}}, []int{1, 2, 3, 4, 5}, 15},
		{4, [][]int{{2, 1}, {3, 1}, {1, 4}}, []int{1, 1, 1, 1}, 3},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := minimumTime(c.n, c.relations, c.time); got != c.want {
			fmt.Printf("FAIL n=%d rel=%v time=%v got=%d want=%d\n", c.n, c.relations, c.time, got, c.want) // 打印输出
			os.Exit(1)                                                                                     // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
