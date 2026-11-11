// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381786
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
	"sort"
) // 引入依赖

func diagonalSort(mat [][]int) [][]int { // 定义函数/方法 diagonalSort
	rows := len(mat) // 把 长度(mat) 写入 rows :
	if rows == 0 {   // 若 行数 等于 0
		return mat // 返回 mat
	}
	cols := len(mat[0])          // 把 长度(mat[0]) 写入 cols :
	diagonals := map[int][]int{} // 把 映射表[int][]int{} 写入 diagonals :
	for r := 0; r < rows; r++ {  // 让 右指针 从 0 开始计数
		for c := 0; c < cols; c++ { // 让 字符 从 0 开始计数
			diagonals[r-c] = append(diagonals[r-c], mat[r][c])
		}
	}
	for k := range diagonals { // 把 range diagonals { 写入 for k :
		sort.Ints(diagonals[k]) // sort.Ints(diagonals[下标 k])
	}
	idx := map[int]int{}        // 把 映射表[int]int{} 写入 idx :
	for r := 0; r < rows; r++ { // 让 右指针 从 0 开始计数
		for c := 0; c < cols; c++ { // 让 字符 从 0 开始计数
			d := r - c                       // 把 右指针 减 字符 写入 d :
			mat[r][c] = diagonals[d][idx[d]] // 把 diagonals[d][idx[d]] 写入 mat[r][c]
			idx[d]++                         // idx[d] 加一
		}
	}
	return mat // 返回 mat
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   [][]int // in [][]int
		want [][]int // want [][]int
	}{ // }{
		{
			[][]int{{3, 3, 1, 1}, {2, 2, 1, 2}, {1, 1, 1, 2}},
			[][]int{{1, 1, 1, 1}, {1, 2, 2, 2}, {1, 2, 3, 3}},
		},
		{
			[][]int{{1, 2}, {3, 4}},
			[][]int{{1, 2}, {3, 4}},
		},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := diagonalSort(c.in)            // 把 diagonalSort(字符.in) 写入 got :
		if !reflect.DeepEqual(got, c.want) { // 若 取反 reflect.DeepEqual(got, 字符.want
			ok = false                                                          // 把 false 写入 ok
			fmt.Printf("FAIL diagonalSort(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
