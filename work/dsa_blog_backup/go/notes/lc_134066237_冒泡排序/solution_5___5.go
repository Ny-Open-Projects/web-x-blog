// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066237
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

// 忠实翻译 python/notes/lc_134066237_冒泡排序/solution_5___5.py
func bubbleSort(nums []int) []int { // 定义函数/方法 bubbleSort
	n := len(nums)           // 把 长度(数组) 写入 n :
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		swapped := false             // 把 false 写入 swapped :
		for j := 0; j < n-i-1; j++ { // 让 下标 j 从 0 开始计数
			if nums[j] > nums[j+1] { // 若 数组[下标 j] 超过 数组[下标 j 加 1]
				nums[j], nums[j+1] = nums[j+1], nums[j] // 把 数组[下标 j 加 1], 数组[下标 j] 写入 nums[j], nums[j+1]
				swapped = true                          // 把 true 写入 swapped
			}
		}
		if !swapped { // 若 取反 swapped
			break // 跳出循环
		}
	}
	return nums // 返回 数组
}

func eqIntSlice(a, b []int) bool { return reflect.DeepEqual(a, b) } // 定义函数/方法 eqIntSlice

func main() { // 程序入口：跑内嵌自测用例
	inputs := [][]int{ // 把 [][]int{ 写入 inputs :
		{5, 4, 3, 2, 1},
		{3, 1, 2, 5, 4},
		{9, -20, 99, 3, 6, 8, 10, 1, 2, 1},
		{-1, -3, -2, 0, 5, -10},
		{},
		{5},
		{2, 2, 2},
		{1, 2, 3},
	}
	wants := [][]int{ // 把 [][]int{ 写入 wants :
		{1, 2, 3, 4, 5},
		{1, 2, 3, 4, 5},
		{-20, 1, 1, 2, 3, 6, 8, 9, 10, 99},
		{-10, -3, -2, -1, 0, 5},
		{},
		{5},
		{2, 2, 2},
		{1, 2, 3},
	}
	ok := true              // 把 true 写入 ok :
	for i := range inputs { // 把 range inputs { 写入 for i :
		got := bubbleSort(append([]int{}, inputs[i]...)) // 把 bubbleSort(append([]int{}, inputs[下标 i]...)) 写入 got :
		if !eqIntSlice(got, wants[i]) {                  // 若 取反 eqIntSlice(got, wants[下标 i]
			ok = false                                                               // 把 false 写入 ok
			fmt.Printf("FAIL bubbleSort(%v)=%v want %v\n", inputs[i], got, wants[i]) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
