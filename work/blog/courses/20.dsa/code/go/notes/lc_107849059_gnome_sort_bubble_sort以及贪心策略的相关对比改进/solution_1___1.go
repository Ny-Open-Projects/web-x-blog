// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107849059
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

// gnomeSort 侏儒排序
func gnomeSort(arr []int) []int { // 定义函数/方法 gnomeSort
	i := 0             // 把 0 写入 i :
	for i < len(arr) { // for 下标 i 小于 长度(数组) {
		if i == 0 || arr[i] >= arr[i-1] { // 若 下标 i 等于 0 或 数组[下标 i] 不低于 数组[下标 i 减 1]
			i++ // 下标 i 加一
		} else { // 否则
			arr[i-1], arr[i] = arr[i], arr[i-1] // 把 数组[下标 i], 数组[下标 i 减 1] 写入 arr[i-1], arr[i]
			i--                                 // 下标 i 减一
		}
	}
	return arr // 返回 数组
}

// bubbleSort 冒泡排序
func bubbleSort(arr []int) []int { // 定义函数/方法 bubbleSort
	a := make([]int, len(arr)) // 把 make([]int, 长度(数组)) 写入 a :
	copy(a, arr)               // copy(数组, 数组)
	swapped := true            // 把 true 写入 swapped :
	for swapped {              // for swapped {
		swapped = false                 // 把 false 写入 swapped
		for i := 0; i < len(a)-1; i++ { // 让 下标 i 从 0 开始计数
			if a[i] > a[i+1] { // 若 数组[下标 i] 超过 数组[下标 i 加 1]
				a[i], a[i+1] = a[i+1], a[i] // 把 数组[下标 i 加 1], 数组[下标 i] 写入 a[i], a[i+1]
				swapped = true              // 把 true 写入 swapped
			}
		}
	}
	return a // 返回 数组
}

// coinChange 贪心找零
func coinChange(coins []int, amount int) int { // 定义函数/方法 coinChange
	c := make([]int, len(coins))              // 把 make([]int, 长度(硬币面额)) 写入 c :
	copy(c, coins)                            // copy(字符, 硬币面额)
	sort.Sort(sort.Reverse(sort.IntSlice(c))) // sort.Sort(sort.Reverse(sort.IntSlice(字符)))
	remaining := amount                       // 把 目标金额 写入 remaining :
	count := 0                                // 把 0 写入 count :
	for _, coin := range c {                  // 同时取 _ 与 coin 遍历
		for remaining >= coin { // 把 coin { 写入 for remaining >
			remaining -= coin // remaining累减 coin
			count++           // 计数 加一
		}
	}
	if remaining == 0 { // 若 remaining 等于 0
		return count // 返回 计数
	}
	return -1 // 返回 减 1
}

func main() { // 程序入口：跑内嵌自测用例
	g := gnomeSort([]int{3, 2, 1})             // 把 gnomeSort([]int{3, 2, 1}) 写入 g :
	if !reflect.DeepEqual(g, []int{1, 2, 3}) { // 若 取反 reflect.DeepEqual(g, []int{1, 2, 3}
		fmt.Printf("FAIL gnomeSort=%v\n", g) // 打印输出
		os.Exit(1)                           // os.Exit(1)
	}
	b := bubbleSort([]int{3, 2, 1})            // 把 bubbleSort([]int{3, 2, 1}) 写入 b :
	if !reflect.DeepEqual(b, []int{1, 2, 3}) { // 若 取反 reflect.DeepEqual(b, []int{1, 2, 3}
		fmt.Printf("FAIL bubbleSort=%v\n", b) // 打印输出
		os.Exit(1)                            // os.Exit(1)
	}
	if coinChange([]int{1, 5, 10, 25}, 63) != 6 { // 若 coinChange([]int{1, 5, 10, 25}, 63) 不等于 6
		fmt.Println("FAIL coinChange") // 打印输出
		os.Exit(1)                     // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
