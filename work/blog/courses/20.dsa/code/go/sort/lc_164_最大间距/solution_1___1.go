// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134379497
package main // 引入依赖

import (
	"fmt"  // 「fmt」
	"os"   // 「os」
	"sort" // 「sort」
)

// 忠实翻译 python/sort/lc_164_最大间距/solution_1___1.py
func maximumGap(nums []int) int { // 定义函数/方法 maximumGap
	if len(nums) < 2 {
		return 0
	} // 若 长度(数组) 小于 2 { return 0 }
	sort.Ints(nums)                  // sort.Ints(数组)
	maxGap := 0                      // 把 0 写入 maxGap :
	for i := 1; i < len(nums); i++ { // 让 下标 i 从 1 开始计数
		if nums[i]-nums[i-1] > maxGap {
			maxGap = nums[i] - nums[i-1]
		}
	}
	return maxGap // 返回 maxGap
}

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
