// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113764246
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

// dfs 深度优先搜索：记录发现/结束时间戳，并对边分类
func dfs(graph [][]int, start int) ([]int, []int, map[[2]int]string, []int) { // 定义函数/方法 dfs
	n := len(graph)             // 把 长度(graph) 写入 n :
	status := make([]string, n) // 把 make([]string, 元素个数) 写入 status :
	for i := range status {     // 把 range status { 写入 for i :
		status[i] = "UNDISCOVERED" // 把 「UNDISCOVERED」 写入 status[i]
	}
	dTime := make([]int, n)  // 把 make([]int, 元素个数) 写入 dTime :
	fTime := make([]int, n)  // 把 make([]int, 元素个数) 写入 fTime :
	parent := make([]int, n) // 把 make([]int, 元素个数) 写入 parent :
	for i := range parent {  // 把 range parent { 写入 for i :
		parent[i] = -1 // 把 减 1 写入 parent[i]
	}
	edges := map[[2]int]string{} // 把 映射表[[2]int]string{} 写入 edges :
	clock := 0                   // 把 0 写入 clock :
	var visit func(v int)        // var visit func(值 int)
	visit = func(v int) {        // 把 func(值 int) { 写入 visit
		clock++                      // clock 加一
		dTime[v] = clock             // 把 clock 写入 dTime[v]
		status[v] = "DISCOVERED"     // 把 「DISCOVERED」 写入 status[v]
		for _, u := range graph[v] { // 同时取 _ 与 节点 u 遍历
			if status[u] == "UNDISCOVERED" { // 若 status[节点 u] 等于 「UNDISCOVERED」
				edges[[2]int{v, u}] = "TREE" // 把 「TREE」 写入 edges[[2]int{v, u}]
				parent[u] = v                // 把 值 写入 parent[u]
				visit(u)                     // visit(节点 u)
			} else if status[u] == "DISCOVERED" { // 否则，若 status[节点 u] 等于 「DISCOVERED」
				edges[[2]int{v, u}] = "BACKWARD" // 把 「BACKWARD」 写入 edges[[2]int{v, u}]
			} else { // 否则
				if dTime[v] < dTime[u] { // 若 dTime[值] 小于 dTime[节点 u]
					edges[[2]int{v, u}] = "FORWARD" // 把 「FORWARD」 写入 edges[[2]int{v, u}]
				} else { // 否则
					edges[[2]int{v, u}] = "CROSS" // 把 「CROSS」 写入 edges[[2]int{v, u}]
				}
			}
		}
		clock++               // clock 加一
		fTime[v] = clock      // 把 clock 写入 fTime[v]
		status[v] = "VISITED" // 把 「VISITED」 写入 status[v]
	}
	visit(start)                       // visit(起点)
	return dTime, fTime, edges, parent // 返回 dTime, fTime, 边集, parent
}

func main() { // 程序入口：跑内嵌自测用例
	graph := [][]int{ // 把 [][]int{ 写入 graph :
		{1, 5},
		{2},
		{},
		{4},
		{5, 6},
		{1, 6},
		{},
	}
	d, f, edges, _ := dfs(graph, 0)                        // 把 dfs(graph, 0) 写入 d, f, edges, _ :
	if !reflect.DeepEqual(d, []int{1, 2, 3, 0, 0, 6, 7}) { // 若 取反 reflect.DeepEqual(d, []int{1, 2, 3, 0, 0, 6, 7}
		fmt.Printf("FAIL dTime=%v\n", d) // 打印输出
		os.Exit(1)                       // os.Exit(1)
	}
	if !reflect.DeepEqual(f, []int{10, 5, 4, 0, 0, 9, 8}) { // 若 取反 reflect.DeepEqual(f, []int{10, 5, 4, 0, 0, 9, 8}
		fmt.Printf("FAIL fTime=%v\n", f) // 打印输出
		os.Exit(1)                       // os.Exit(1)
	}
	wantEdges := map[[2]int]string{ // 把 映射表[[2]int]string{ 写入 wantEdges :
		{0, 1}: "TREE",
		{1, 2}: "TREE",
		{0, 5}: "TREE",
		{5, 1}: "CROSS",
		{5, 6}: "TREE",
	}
	if !reflect.DeepEqual(edges, wantEdges) { // 若 取反 reflect.DeepEqual(边集, wantEdges
		fmt.Printf("FAIL edges=%v\n", edges) // 打印输出
		os.Exit(1)                           // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
