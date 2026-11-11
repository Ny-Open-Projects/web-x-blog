// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116781
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func eqStrSlice(a, b []string) bool { // 定义函数/方法 eqStrSlice
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

func reverseString(s []string) { // 定义函数/方法 reverseString
	left, right := 0, len(s)-1 // 把 0, 长度(字符串) 减 1 写入 left, right :
	for left <= right {        // 把 右边界 { 写入 for left <
		s[left], s[right] = s[right], s[left] // 把 字符串[右边界], 字符串[左边界] 写入 s[left], s[right]
		left++                                // 左边界 加一
		right--                               // 右边界 减一
	}
}

func main() { // 程序入口：跑内嵌自测用例
	cases := [][2][]string{ // 把 [][2][]string{ 写入 cases :
		{{"h", "e", "l", "l", "o"}, {"o", "l", "l", "e", "h"}},
		{{"H", "a", "n", "n", "a", "h"}, {"h", "a", "n", "n", "a", "H"}},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		input := c[0]                     // 把 字符[0] 写入 input :
		expected := c[1]                  // 把 字符[1] 写入 expected :
		reverseString(input)              // reverseString(input)
		if !eqStrSlice(input, expected) { // 若 取反 eqStrSlice(input, expected
			fmt.Printf("FAIL: got %v expected %v\n", input, expected) // 打印输出
			os.Exit(1)                                                // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
