// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113548046
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

// bfs 广度优先搜索：逐层扩散（前锋面），返回访问顺序与生成树父指针。
func bfs(graph [][]int, start int) ([]int, []int) { // 定义函数/方法 bfs
	n := len(graph)             // 把 长度(graph) 写入 n :
	status := make([]string, n) // 把 make([]string, 元素个数) 写入 status :
	for i := range status {     // 把 range status { 写入 for i :
		status[i] = "UNDISCOVERED" // 把 「UNDISCOVERED」 写入 status[i]
	}
	parent := make([]int, n) // 把 make([]int, 元素个数) 写入 parent :
	for i := range parent {  // 把 range parent { 写入 for i :
		parent[i] = -1 // 把 减 1 写入 parent[i]
	}
	order := []int{}             // 把 []int{} 写入 order :
	q := []int{start}            // 把 []int{起点} 写入 q :
	status[start] = "DISCOVERED" // 把 「DISCOVERED」 写入 status[start]
	for len(q) > 0 {             // for 长度(节点) 超过 0 {
		v := q[0]                    // 把 节点[0] 写入 v :
		q = q[1:]                    // 把 节点[1:] 写入 节点
		order = append(order, v)     // 把 append(order, 值) 写入 order
		for _, u := range graph[v] { // 同时取 _ 与 节点 u 遍历
			if status[u] == "UNDISCOVERED" { // 若 status[节点 u] 等于 「UNDISCOVERED」
				status[u] = "DISCOVERED" // 把 「DISCOVERED」 写入 status[u]
				parent[u] = v            // 把 值 写入 parent[u]
				q = append(q, u)         // 把 append(节点, 节点 u) 写入 节点
			}
		}
		status[v] = "VISITED" // 把 「VISITED」 写入 status[v]
	}
	return order, parent // 返回 order, parent
}

func main() { // 程序入口：跑内嵌自测用例
	graph := [][]int{ // 把 [][]int{ 写入 graph :
		{1, 2},
		{0, 3, 4},
		{0, 5},
		{1},
		{1},
		{2},
	}
	order, parent := bfs(graph, 0)                          // 把 bfs(graph, 0) 写入 order, parent :
	if !reflect.DeepEqual(order, []int{0, 1, 2, 3, 4, 5}) { // 若 取反 reflect.DeepEqual(order, []int{0, 1, 2, 3, 4, 5}
		fmt.Printf("FAIL order=%v\n", order) // 打印输出
		os.Exit(1)                           // os.Exit(1)
	}
	if !reflect.DeepEqual(parent, []int{-1, 0, 0, 1, 1, 2}) { // 若 取反 reflect.DeepEqual(parent, []int{ 减 1, 0, 0, 1, 1, 2}
		fmt.Printf("FAIL parent=%v\n", parent) // 打印输出
		os.Exit(1)                             // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
