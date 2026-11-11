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
	n := len(nums)   // 把 长度(数组) 写入 n :
	p0, p2 := 0, n-1 // 把 0, 元素个数 减 1 写入 p0, p2 :
	i := 0           // 把 0 写入 i :
	for i <= p2 {    // 把 p2 { 写入 for i <
		for i <= p2 && nums[i] == 2 { // 把 p2 且 数组[下标 i] 等于 2 { 写入 for i <
			nums[i], nums[p2] = nums[p2], nums[i] // 把 数组[p2], 数组[下标 i] 写入 nums[i], nums[p2]
			p2--                                  // p2 减一
		}
		if nums[i] == 0 { // 若 数组[下标 i] 等于 0
			nums[i], nums[p0] = nums[p0], nums[i] // 把 数组[p0], 数组[下标 i] 写入 nums[i], nums[p0]
			p0++                                  // p0 加一
		}
		i++ // 下标 i 加一
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
