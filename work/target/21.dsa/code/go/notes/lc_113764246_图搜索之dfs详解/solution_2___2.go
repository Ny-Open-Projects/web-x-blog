// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113764246
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

// topoSortDFS 基于 DFS 的拓扑排序：回溯时将结点压栈，逆序即为拓扑序。
func topoSortDFS(graph [][]int) []int { // 定义函数/方法 topoSortDFS
	n := len(graph)             // 把 长度(graph) 写入 n :
	status := make([]string, n) // 把 make([]string, 元素个数) 写入 status :
	for i := range status {     // 把 range status { 写入 for i :
		status[i] = "UNDISCOVERED" // 把 「UNDISCOVERED」 写入 status[i]
	}
	stack := []int{}      // 把 []int{} 写入 stack :
	var visit func(v int) // var visit func(值 int)
	visit = func(v int) { // 把 func(值 int) { 写入 visit
		status[v] = "DISCOVERED"     // 把 「DISCOVERED」 写入 status[v]
		for _, u := range graph[v] { // 同时取 _ 与 节点 u 遍历
			if status[u] == "UNDISCOVERED" { // 若 status[节点 u] 等于 「UNDISCOVERED」
				visit(u) // visit(节点 u)
			}
		}
		status[v] = "VISITED"    // 把 「VISITED」 写入 status[v]
		stack = append(stack, v) // 把 append(栈, 值) 写入 栈
	}
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		if status[i] == "UNDISCOVERED" { // 若 status[下标 i] 等于 「UNDISCOVERED」
			visit(i) // visit(下标 i)
		}
	}
	for i, j := 0, len(stack)-1; i < j; i, j = i+1, j-1 {
		stack[i], stack[j] = stack[j], stack[i] // 把 栈[下标 j], 栈[下标 i] 写入 stack[i], stack[j]
	}
	return stack // 返回 栈
}

func main() { // 程序入口：跑内嵌自测用例
	graph := [][]int{ // 把 [][]int{ 写入 graph :
		{2}, // 0 A
		{2}, // 1 B
		{3}, // 2 C
		{4}, // 3 D
		{5}, // 4 E
		{},  // 5 F
	}
	got := topoSortDFS(graph)                             // 把 topoSortDFS(graph) 写入 got :
	if !reflect.DeepEqual(got, []int{1, 0, 2, 3, 4, 5}) { // 若 取反 reflect.DeepEqual(got, []int{1, 0, 2, 3, 4, 5}
		fmt.Printf("FAIL topo=%v\n", got) // 打印输出
		os.Exit(1)                        // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
