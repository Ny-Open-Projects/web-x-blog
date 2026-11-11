// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134026430
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

func spiralOrder(matrix [][]int) []int { // 定义函数/方法 spiralOrder
	if len(matrix) == 0 || len(matrix[0]) == 0 { // 若 长度(矩阵) 等于 0 或 长度(矩阵[0]) 等于 0
		return nil // 返回 nil
	}
	result := []int{}                    // 把 []int{} 写入 result :
	top, bottom := 0, len(matrix)-1      // 把 0, 长度(矩阵) 减 1 写入 top, bottom :
	left, right := 0, len(matrix[0])-1   // 把 0, 长度(矩阵[0]) 减 1 写入 left, right :
	for top <= bottom && left <= right { // 把 bottom 且 左边界 不超过 右边界 { 写入 for top <
		for i := left; i <= right; i++ { // 把 左边界; 下标 i 不超过 右边界; 下标 i 加一 { 写入 for i :
			result = append(result, matrix[top][i]) // 把 append(结果, 矩阵[top][下标 i]) 写入 结果
		}
		top++                            // top 加一
		for i := top; i <= bottom; i++ { // 把 top; 下标 i 不超过 bottom; 下标 i 加一 { 写入 for i :
			result = append(result, matrix[i][right]) // 把 append(结果, 矩阵[下标 i][右边界]) 写入 结果
		}
		right--            // 右边界 减一
		if top <= bottom { // 若 top 不超过 bottom
			for i := right; i >= left; i-- { // 把 右边界; 下标 i 不低于 左边界; 下标 i 减一 { 写入 for i :
				result = append(result, matrix[bottom][i]) // 把 append(结果, 矩阵[bottom][下标 i]) 写入 结果
			}
			bottom-- // bottom 减一
		}
		if left <= right { // 若 左边界 不超过 右边界
			for i := bottom; i >= top; i-- { // 把 bottom; 下标 i 不低于 top; 下标 i 减一 { 写入 for i :
				result = append(result, matrix[i][left]) // 把 append(结果, 矩阵[下标 i][左边界]) 写入 结果
			}
			left++ // 左边界 加一
		}
	}
	return result // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   [][]int // in [][]int
		want []int   // want []int
	}{ // }{
		{[][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, []int{1, 2, 3, 6, 9, 8, 7, 4, 5}},
		{[][]int{{1, 2, 3, 4}}, []int{1, 2, 3, 4}},
		{nil, nil},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := spiralOrder(c.in)             // 把 spiralOrder(字符.in) 写入 got :
		if !reflect.DeepEqual(got, c.want) { // 若 取反 reflect.DeepEqual(got, 字符.want
			ok = false                                                         // 把 false 写入 ok
			fmt.Printf("FAIL spiralOrder(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
