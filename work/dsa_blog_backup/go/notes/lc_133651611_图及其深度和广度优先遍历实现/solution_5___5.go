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

func dfs(n int, visited map[int]bool, res *[]int) { // 定义函数/方法 dfs
	*res = append(*res, n)
	visited[n] = true            // 把 true 写入 visited[n]
	for _, c := range graph[n] { // 同时取 _ 与 字符 遍历
		if !visited[c] { // 若 取反 已访问集合[字符]
			dfs(c, visited, res) // dfs(字符, 已访问集合, 结果)
		}
	}
}

func main() { // 程序入口：跑内嵌自测用例
	visited := map[int]bool{}          // 把 映射表[int]bool{} 写入 visited :
	res := []int{}                     // 把 []int{} 写入 res :
	dfs(2, visited, &res)              // dfs(2, 已访问集合, 按位与 结果)
	want := []int{2, 0, 1, 3}          // 把 []int{2, 0, 1, 3} 写入 want :
	if !reflect.DeepEqual(res, want) { // 若 取反 reflect.DeepEqual(结果, want
		fmt.Println("FAIL dfs", res) // 打印输出
		os.Exit(1)                   // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
