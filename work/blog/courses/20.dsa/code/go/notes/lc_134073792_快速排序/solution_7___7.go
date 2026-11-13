// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

// 忠实翻译 python/notes/lc_134073792_快速排序/solution_7___7.py
// qs_fn：取中点为基准但不 pop，rest 排除基准，等于基准的元素被丢弃（与 python 一致）
func quickSort(arr []int) []int { // 定义函数/方法 quickSort
	var qsFn func([]int) []int   // var qsFn func([]int) []int
	qsFn = func(a []int) []int { // 把 func(数组 []int) []int { 写入 qsFn
		if len(a) < 1 { // 若 长度(数组) 小于 1
			return a // 返回 数组
		}
		pivotIndex := len(a) / 2                   // 把 长度(数组) 除以 2 写入 pivotIndex :
		pivot := a[pivotIndex]                     // 把 数组[pivotIndex] 写入 pivot :
		rest := append([]int{}, a[:pivotIndex]...) // 把 append([]int{}, 数组[:pivotIndex]...) 写入 rest :
		rest = append(rest, a[pivotIndex+1:]...)   // 把 append(rest, 数组[pivotIndex 加 1:]...) 写入 rest
		left := []int{}                            // 把 []int{} 写入 left :
		right := []int{}                           // 把 []int{} 写入 right :
		for _, item := range rest {                // 同时取 _ 与 item 遍历
			if item < pivot { // 若 item 小于 pivot
				left = append(left, item) // 把 append(左边界, item) 写入 左边界
			} else if item > pivot { // 否则，若 item 超过 pivot
				right = append(right, item) // 把 append(右边界, item) 写入 右边界
			}
		}
		return append(append(qsFn(left), pivot), qsFn(right)...) // 定义函数/方法 append
	}
	res := qsFn(arr) // 把 qsFn(数组) 写入 res :
	copy(arr, res)   // copy(数组, 结果)
	return res       // 返回 结果
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
		{-20, 1, 2, 3, 6, 8, 9, 10, 99},
		{-100, -30, -20, -9, -2, 0, 1, 3, 4, 5, 9, 20, 88, 99, 100},
		{},
		{5},
		{2},
		{1, 2, 3},
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
