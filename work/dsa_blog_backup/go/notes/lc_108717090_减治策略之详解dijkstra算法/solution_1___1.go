// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108717090
package main // 引入依赖

import (
	"container/heap" // 「container 除以 堆」
	"fmt"            // 「fmt」
	"os"             // 「os」
	"reflect"        // 「reflect」
)

type Edge struct{ to, w int }          // 定义类型
type Item struct{ node, d, index int } // 定义类型
type PQ []*Item                        // 定义类型
func (pq PQ) Len() int                 { return len(pq) }                                                // 定义函数/方法 Len
func (pq PQ) Less(i, j int) bool       { return pq[i].d < pq[j].d }                                      // 定义函数/方法 Less
func (pq PQ) Swap(i, j int)            { pq[i], pq[j] = pq[j], pq[i]; pq[i].index = i; pq[j].index = j } // 定义函数/方法 Swap
func (pq *PQ) Push(x interface{})      { it := x.(*Item); it.index = len(*pq); *pq = append(*pq, it) }   // 定义函数/方法 Push
func (pq *PQ) Pop() interface{} {
	old := *pq
	n := len(old)
	it := old[n-1]
	old[n-1] = nil
	*pq = old[:n-1]
	return it
} // 定义函数/方法 Pop

// 忠实翻译 python/notes/lc_108717090_减治策略之详解dijkstra算法/solution_1___1.py
func dijkstra(graph [][]Edge, src int) ([]int, []int) { // 定义函数/方法 dijkstra
	n := len(graph)          // 把 长度(graph) 写入 n :
	dist := make([]int, n)   // 把 make([]int, 元素个数) 写入 dist :
	parent := make([]int, n) // 把 make([]int, 元素个数) 写入 parent :
	for i := range dist {
		dist[i] = 1 << 62
		parent[i] = -1
	}
	dist[src] = 0                          // 把 0 写入 dist[src]
	pq := make(PQ, 0)                      // 把 make(PQ, 0) 写入 pq :
	heap.Push(&pq, &Item{node: src, d: 0}) // 堆.Push( 按位与 优先队列, 按位与 Item{节点: src, d: 0})
	for pq.Len() > 0 {                     // for 优先队列.Len() 超过 0 {
		it := heap.Pop(&pq).(*Item) // 把 堆.Pop( 按位与 优先队列).( 乘 Item) 写入 it :
		u := it.node
		d := it.d // 把 it.节点; d : 赋值为 it.d 写入 u :
		if d > dist[u] {
			continue
		} // 若 d 超过 dist[节点 u] { continue }
		for _, e := range graph[u] { // 同时取 _ 与 e 遍历
			if dist[u]+e.w < dist[e.to] { // 若 dist[节点 u] 加 e.权重 小于 dist[e.to]
				dist[e.to] = dist[u] + e.w                       // 把 dist[节点 u] 加 e.权重 写入 dist[e.to]
				parent[e.to] = u                                 // 把 节点 u 写入 parent[e.to]
				heap.Push(&pq, &Item{node: e.to, d: dist[e.to]}) // 堆.Push( 按位与 优先队列, 按位与 Item{节点: e.to, d: dist[e.to]})
			}
		}
	}
	return dist, parent // 返回 dist, parent
}

func eqIntSlice(a, b []int) bool { return reflect.DeepEqual(a, b) } // 定义函数/方法 eqIntSlice

func main() { // 程序入口：跑内嵌自测用例
	graph1 := [][]Edge{{{1, 4}, {2, 1}}, {{3, 1}}, {{1, 2}, {3, 5}}, {{4, 3}}, {}}
	graph2 := [][]Edge{{{1, 10}}, {{2, 5}}, {{3, 1}}, {}} // 把 [][]Edge{ {{1, 10}}, {{2, 5}}, {{3, 1}}, {} } 写入 graph2 :
	type caseT struct {
		graph [][]Edge
		src   int
		distW []int
		parW  []int
	} // 定义类型
	cases := []caseT{ // 把 []caseT{ 写入 cases :
		{graph1, 0, []int{0, 3, 1, 4, 7}, []int{-1, 2, 0, 1, 3}},
		{graph2, 0, []int{0, 10, 15, 16}, []int{-1, 0, 1, 2}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		dist, parent := dijkstra(c.graph, c.src) // 把 dijkstra(字符.graph, 字符.src) 写入 dist, parent :
		if !eqIntSlice(dist, c.distW) || !eqIntSlice(parent, c.parW) {
			ok = false                                                                                // 把 false 写入 ok
			fmt.Printf("FAIL dijkstra dist=%v parent=%v want %v %v\n", dist, parent, c.distW, c.parW) // 打印输出
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
