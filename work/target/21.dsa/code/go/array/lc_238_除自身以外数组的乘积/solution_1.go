package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func productExceptSelf(nums []int) []int { // 定义函数/方法 productExceptSelf
	n := len(nums)        // 把 长度(数组) 写入 n :
	out := make([]int, n) // 把 make([]int, 元素个数) 写入 out :
	for i := range out {  // 把 range out { 写入 for i :
		out[i] = 1 // 把 1 写入 out[i]
	}
	p := 1                   // 把 1 写入 p :
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		out[i] = p   // 把 节点 写入 out[i]
		p *= nums[i] // 把 数组[下标 i] 写入 p *
	}
	p = 1                         // 把 1 写入 节点
	for i := n - 1; i >= 0; i-- { // 把 元素个数 减 1; 下标 i 不低于 0; 下标 i 减一 { 写入 for i :
		out[i] *= p  // 把 节点 写入 out[i] *
		p *= nums[i] // 把 数组[下标 i] 写入 p *
	}
	return out // 返回 out
}

func eqIntSlice(a, b []int) bool { // 定义函数/方法 eqIntSlice
	if len(a) != len(b) { // 定义函数/方法 len
		return false // 返回 false
	}
	for i := range a { // 把 range 数组 { 写入 for i :
		if a[i] != b[i] { // 若 数组[下标 i] 不等于 b[下标 i]
			return false // 返回 false
		}
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		want []int // want []int
	}{ // }{
		{[]int{1, 2, 3, 4}, []int{24, 12, 8, 6}},
		{[]int{0, 0}, []int{0, 0}},
		{[]int{-1, 1, 0, -3, 3}, []int{0, 0, 9, 0, 0}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := productExceptSelf(c.in) // 把 productExceptSelf(字符.in) 写入 got :
		if !eqIntSlice(got, c.want) {  // 若 取反 eqIntSlice(got, 字符.want
			fmt.Printf("FAIL in=%v want=%v got=%v\n", c.in, c.want, got) // 打印输出
			ok = false                                                   // 把 false 写入 ok
		}
	}
	if !ok { // 若 取反 ok
		fmt.Println("RESULT: FAIL") // 打印输出
		os.Exit(1)                  // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
