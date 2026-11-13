// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

// 忠实翻译 python/notes/lc_134073792_快速排序/solution_8___8.py
// 分区（基准取首元素），原地排序
func partition(arr []int, left, right int) int { // 定义函数/方法 partition
	pivot := arr[left] // 把 数组[左边界] 写入 pivot :
	i := left + 1      // 把 左边界 加 1 写入 i :
	j := right         // 把 右边界 写入 j :
	for i <= j {       // 把 下标 j { 写入 for i <
		for i <= j && arr[j] >= pivot { // 把 下标 j 且 数组[下标 j] 不低于 pivot { 写入 for i <
			j-- // 下标 j 减一
		}
		for i <= j && arr[i] <= pivot { // 把 下标 j 且 数组[下标 i] 不超过 pivot { 写入 for i <
			i++ // 下标 i 加一
		}
		if i <= j { // 若 下标 i 不超过 下标 j
			arr[i], arr[j] = arr[j], arr[i] // 把 数组[下标 j], 数组[下标 i] 写入 arr[i], arr[j]
		}
	}
	arr[left], arr[j] = arr[j], arr[left] // 把 数组[下标 j], 数组[左边界] 写入 arr[left], arr[j]
	return j                              // 返回 下标 j
}

func quickSort(arr []int) []int { // 定义函数/方法 quickSort
	var qs func([]int, int, int)          // var qs func([]int, int, int)
	qs = func(a []int, left, right int) { // 把 func(数组 []int, 左边界, 右边界 int) { 写入 qs
		if left < right { // 若 左边界 小于 右边界
			pi := partition(a, left, right) // 把 partition(数组, 左边界, 右边界) 写入 pi :
			qs(a, left, pi-1)               // qs(数组, 左边界, pi 减 1)
			qs(a, pi+1, right)              // qs(数组, pi 加 1, 右边界)
		}
	}
	if len(arr) > 0 { // 若 长度(数组) 超过 0
		qs(arr, 0, len(arr)-1) // qs(数组, 0, 长度(数组) 减 1)
	}
	return arr // 返回 数组
}

func eqIntSlice(a, b []int) bool { return reflect.DeepEqual(a, b) } // 定义函数/方法 eqIntSlice

func main() { // 程序入口：跑内嵌自测用例
	inputs := [][]int{ // 把 [][]int{ 写入 inputs :
		{15, 4, 23, 52, 1},
		{3, 1, 2, 5, 4},
		{9, -20, 99, 3, 6, 8, 10, 1, 2, 1},
		{-2, 1, 0, -9, 1, 3, 9, 99, 9, -30, -100, 100, 88, 88, 20, 1, 0, 3, 4, 5, -20},
		{},
		{5},
		{2, 2, 2},
		{3, 3, 1, 2, 3, 1},
	}
	wants := [][]int{ // 把 [][]int{ 写入 wants :
		{1, 4, 15, 23, 52},
		{1, 2, 3, 4, 5},
		{-20, 1, 1, 2, 3, 6, 8, 9, 10, 99},
		{-100, -30, -20, -9, -2, 0, 0, 1, 1, 1, 3, 3, 4, 5, 9, 9, 20, 88, 88, 99, 100},
		{},
		{5},
		{2, 2, 2},
		{1, 1, 2, 3, 3, 3},
	}
	ok := true              // 把 true 写入 ok :
	for i := range inputs { // 把 range inputs { 写入 for i :
		got := quickSort(append([]int{}, inputs[i]...)) // 把 quickSort(append([]int{}, inputs[下标 i]...)) 写入 got :
		if !eqIntSlice(got, wants[i]) {                 // 若 取反 eqIntSlice(got, wants[下标 i]
			ok = false                                                              // 把 false 写入 ok
			fmt.Printf("FAIL quickSort(%v)=%v want %v\n", inputs[i], got, wants[i]) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
