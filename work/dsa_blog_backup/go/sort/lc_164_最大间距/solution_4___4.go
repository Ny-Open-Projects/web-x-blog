// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134379497
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 忠实翻译 python/sort/lc_164_最大间距/solution_4___4.py
func maximumGap(nums []int) int { // 定义函数/方法 maximumGap
	n := len(nums) // 把 长度(数组) 写入 n :
	if n < 2 {
		return 0
	} // 若 元素个数 小于 2 { return 0 }
	minVal := minSlice(nums)
	maxVal := maxSlice(nums) // 把 minSlice(数组); maxVal : 赋值为 maxSlice(数组) 写入 minVal :
	if minVal == maxVal {
		return 0
	} // 若 minVal 等于 maxVal { return 0 }
	d := maxInt(1, (maxVal-minVal)/(n-1)) // 把 maxInt(1, (maxVal 减 minVal) 除以 (元素个数 减 1)) 写入 d :
	bucketSize := (maxVal-minVal)/d + 1   // 把 (maxVal 减 minVal) 除以 d 加 1 写入 bucketSize :
	buckets := make([][2]int, bucketSize) // 把 make([][2]int, bucketSize) 写入 buckets :
	for i := range buckets {
		buckets[i] = [2]int{-1, -1}
	}
	for _, x := range nums { // 同时取 _ 与 x 遍历
		idx := (x - minVal) / d // 把 (x 减 minVal) 除以 d 写入 idx :
		if buckets[idx][0] == -1 {
			buckets[idx][0] = x
			buckets[idx][1] = x
		} else {
			if x < buckets[idx][0] {
				buckets[idx][0] = x
			} // 若 x 小于 buckets[idx][0] { buckets[idx][0] 赋值为 x }
			if x > buckets[idx][1] {
				buckets[idx][1] = x
			} // 若 x 超过 buckets[idx][1] { buckets[idx][1] 赋值为 x }
		}
	}
	maxGap := 0
	prev := -1                        // 把 0; 前一个 : 赋值为 减 1 写入 maxGap :
	for i := 0; i < bucketSize; i++ { // 让 下标 i 从 0 开始计数
		if buckets[i][0] == -1 {
			continue
		} // 若 buckets[下标 i][0] 等于 减 1 { continue }
		if prev != -1 { // 若 前一个 不等于 减 1
			if buckets[i][0]-buckets[prev][1] > maxGap {
				maxGap = buckets[i][0] - buckets[prev][1]
			}
		}
		prev = i // 把 下标 i 写入 前一个
	}
	return maxGap // 返回 maxGap
}

func minSlice(a []int) int {
	m := a[0]
	for _, v := range a {
		if v < m {
			m = v
		}
	}
	return m
} // 定义函数/方法 minSlice
func maxSlice(a []int) int {
	m := a[0]
	for _, v := range a {
		if v > m {
			m = v
		}
	}
	return m
} // 定义函数/方法 maxSlice
func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
} // 定义函数/方法 maxInt

func eqInt(a, b int) bool { return a == b } // 定义函数/方法 eqInt

func main() { // 程序入口：跑内嵌自测用例
	inputs := [][]int{ // 把 [][]int{ 写入 inputs :
		{3, 6, 9, 1},
		{10},
		{1, 2, 3},
		{5, 1, 100, 3, 50},
		{1, 1, 1, 1},
		{100, 3, 1, 200, 2},
		{9, 10, 12, 13, 1, 2, 3, 4, 7},
	}
	wants := []int{3, 0, 1, 50, 0, 100, 3} // 把 []int{3, 0, 1, 50, 0, 100, 3} 写入 wants :
	ok := true                             // 把 true 写入 ok :
	for i := range inputs {                // 把 range inputs { 写入 for i :
		got := maximumGap(append([]int{}, inputs[i]...)) // 把 maximumGap(append([]int{}, inputs[下标 i]...)) 写入 got :
		if got != wants[i] {                             // 若 got 不等于 wants[下标 i]
			ok = false                                                               // 把 false 写入 ok
			fmt.Printf("FAIL maximumGap(%v)=%v want %v\n", inputs[i], got, wants[i]) // 打印输出
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
