// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

// 忠实翻译 python/notes/lc_134073792_快速排序/solution_2___2.py
// Lomuto 分区（基准取末尾），原地排序
func partition(nums []int, low, high int) int { // 定义函数/方法 partition
	pivot := nums[high]           // 把 数组[high] 写入 pivot :
	i := low - 1                  // 把 low 减 1 写入 i :
	for j := low; j < high; j++ { // 把 low; 下标 j 小于 high; 下标 j 加一 { 写入 for j :
		if nums[j] <= pivot { // 若 数组[下标 j] 不超过 pivot
			i++                                 // 下标 i 加一
			nums[i], nums[j] = nums[j], nums[i] // 把 数组[下标 j], 数组[下标 i] 写入 nums[i], nums[j]
		}
	}
	nums[i+1], nums[high] = nums[high], nums[i+1] // 把 数组[high], 数组[下标 i 加 1] 写入 nums[i+1], nums[high]
	return i + 1                                  // 返回 下标 i 加 1
}

func quickSort(nums []int) []int { // 定义函数/方法 quickSort
	var qs func([]int, int, int)        // var qs func([]int, int, int)
	qs = func(a []int, low, high int) { // 把 func(数组 []int, low, high int) { 写入 qs
		if low < high { // 若 low 小于 high
			pi := partition(a, low, high) // 把 partition(数组, low, high) 写入 pi :
			qs(a, low, pi-1)              // qs(数组, low, pi 减 1)
			qs(a, pi+1, high)             // qs(数组, pi 加 1, high)
		}
	}
	if len(nums) > 0 { // 若 长度(数组) 超过 0
		qs(nums, 0, len(nums)-1) // qs(数组, 0, 长度(数组) 减 1)
	}
	return nums // 返回 数组
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
