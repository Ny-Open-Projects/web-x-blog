// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133651611
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

var graph = map[int][]int{ // 把 映射表[int][]int{ 存入 graph
	0: {1, 2},
	1: {2},
	2: {0, 3},
	3: {3},
}

func bfs(start int) []int { // 定义函数/方法 bfs
	res := []int{}            // 把 []int{} 写入 res :
	visited := map[int]bool{} // 把 映射表[int]bool{} 写入 visited :
	q := []int{start}         // 把 []int{起点} 写入 q :
	visited[start] = true     // 把 true 写入 visited[start]
	for len(q) > 0 {          // for 长度(节点) 超过 0 {
		n := q[0]                    // 把 节点[0] 写入 n :
		q = q[1:]                    // 把 节点[1:] 写入 节点
		res = append(res, n)         // 把 append(结果, 元素个数) 写入 结果
		for _, c := range graph[n] { // 同时取 _ 与 字符 遍历
			if !visited[c] { // 若 取反 已访问集合[字符]
				q = append(q, c)  // 把 append(节点, 字符) 写入 节点
				visited[c] = true // 把 true 写入 visited[c]
			}
		}
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	res := bfs(2)                      // 把 bfs(2) 写入 res :
	want := []int{2, 0, 3, 1}          // 把 []int{2, 0, 3, 1} 写入 want :
	if !reflect.DeepEqual(res, want) { // 若 取反 reflect.DeepEqual(结果, want
		fmt.Println("FAIL bfs", res) // 打印输出
		os.Exit(1)                   // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
