// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133982215
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

func pacificAtlantic(matrix [][]int) [][]int { // 定义函数/方法 pacificAtlantic
	if len(matrix) == 0 || len(matrix[0]) == 0 { // 若 长度(矩阵) 等于 0 或 长度(矩阵[0]) 等于 0
		return [][]int{} // 返回 [][]int{}
	}
	m, n := len(matrix), len(matrix[0]) // 把 长度(矩阵), 长度(矩阵[0]) 写入 m, n :
	pacific := make([][]bool, m)        // 把 make([][]bool, 映射表) 写入 pacific :
	atlantic := make([][]bool, m)       // 把 make([][]bool, 映射表) 写入 atlantic :
	for i := 0; i < m; i++ {            // 让 下标 i 从 0 开始计数
		pacific[i] = make([]bool, n)  // 把 make([]bool, 元素个数) 写入 pacific[i]
		atlantic[i] = make([]bool, n) // 把 make([]bool, 元素个数) 写入 atlantic[i]
	}
	var dfs func(r, c int, flow [][]bool) // var dfs func(右指针, 字符 int, flow [][]bool)
	dfs = func(r, c int, flow [][]bool) { // 把 func(右指针, 字符 int, flow [][]bool) { 写入 dfs
		flow[r][c] = true                                  // 把 true 写入 flow[r][c]
		dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} // 把 [][2]int{{ 减 1, 0}, {1, 0}, {0, 减 1}, {0, 1}} 写入 dirs :
		for _, d := range dirs {                           // 同时取 _ 与 d 遍历
			nr, nc := r+d[0], c+d[1] // 把 右指针 加 d[0], 字符 加 d[1] 写入 nr, nc :
			if nr >= 0 && nr < m && nc >= 0 && nc < n && !flow[nr][nc] && matrix[nr][nc] >= matrix[r][c] {
				dfs(nr, nc, flow) // dfs(nr, nc, flow)
			}
		}
	}
	for r := 0; r < m; r++ { // 让 右指针 从 0 开始计数
		dfs(r, 0, pacific)    // dfs(右指针, 0, pacific)
		dfs(r, n-1, atlantic) // dfs(右指针, 元素个数 减 1, atlantic)
	}
	for c := 0; c < n; c++ { // 让 字符 从 0 开始计数
		dfs(0, c, pacific)    // dfs(0, 字符, pacific)
		dfs(m-1, c, atlantic) // dfs(映射表 减 1, 字符, atlantic)
	}
	var res [][]int          // var 结果 [][]int
	for r := 0; r < m; r++ { // 让 右指针 从 0 开始计数
		for c := 0; c < n; c++ { // 让 字符 从 0 开始计数
			if pacific[r][c] && atlantic[r][c] { // 若 pacific[右指针][字符] 且 atlantic[右指针][字符]
				res = append(res, []int{r, c}) // 把 append(结果, []int{右指针, 字符}) 写入 结果
			}
		}
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true // 把 true 写入 ok :
	if got := pacificAtlantic(nil); !reflect.DeepEqual(got, [][]int{}) {
		ok = false                   // 把 false 写入 ok
		fmt.Println("FAIL nil", got) // 打印输出
	}
	mat := [][]int{ // 把 [][]int{ 写入 mat :
		{1, 2, 2, 3, 5},
		{3, 2, 3, 4, 4},
		{2, 4, 5, 3, 1},
		{6, 7, 1, 4, 5},
		{5, 1, 1, 2, 4},
	}
	want := [][]int{{0, 4}, {1, 3}, {1, 4}, {2, 2}, {3, 0}, {3, 1}, {4, 0}}
	if got := pacificAtlantic(mat); !reflect.DeepEqual(got, want) {
		ok = false                   // 把 false 写入 ok
		fmt.Println("FAIL mat", got) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
