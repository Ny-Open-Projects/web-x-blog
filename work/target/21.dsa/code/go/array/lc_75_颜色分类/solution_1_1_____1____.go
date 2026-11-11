// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370043
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func eqIntSlice(a, b []int) bool { // 定义函数/方法 eqIntSlice
	if len(a) != len(b) {
		return false
	} // 若 长度(数组) 不等于 长度(b) { return false }
	for i := range a { // 把 range 数组 { 写入 for i :
		if a[i] != b[i] {
			return false
		} // 若 数组[下标 i] 不等于 b[下标 i] { return false }
	}
	return true // 返回 true
}

func sortColors(nums []int) { // 定义函数/方法 sortColors
	n := len(nums)           // 把 长度(数组) 写入 n :
	ptr := 0                 // 把 0 写入 ptr :
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		if nums[i] == 0 { // 若 数组[下标 i] 等于 0
			nums[i], nums[ptr] = nums[ptr], nums[i] // 把 数组[ptr], 数组[下标 i] 写入 nums[i], nums[ptr]
			ptr++                                   // ptr 加一
		}
	}
	for i := ptr; i < n; i++ { // 把 ptr; 下标 i 小于 元素个数; 下标 i 加一 { 写入 for i :
		if nums[i] == 1 { // 若 数组[下标 i] 等于 1
			nums[i], nums[ptr] = nums[ptr], nums[i] // 把 数组[ptr], 数组[下标 i] 写入 nums[i], nums[ptr]
			ptr++                                   // ptr 加一
		}
	}
}

func main() { // 程序入口：跑内嵌自测用例
	cases := [][2][]int{ // 把 [][2][]int{ 写入 cases :
		{{2, 0, 2, 1, 1, 0}, {0, 0, 1, 1, 2, 2}},
		{{0}, {0}},
		{{2, 0, 1}, {0, 1, 2}},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		input := c[0]                     // 把 字符[0] 写入 input :
		expected := c[1]                  // 把 字符[1] 写入 expected :
		sortColors(input)                 // sortColors(input)
		if !eqIntSlice(input, expected) { // 若 取反 eqIntSlice(input, expected
			fmt.Printf("FAIL: got %v expected %v\n", input, expected) // 打印输出
			os.Exit(1)                                                // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
