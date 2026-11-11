// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

// 忠实翻译 python/notes/lc_116567013_pm/solution_4___4.py
// 构造 KMP 的 next 表（单独呈现，对应 C++ buildNext）。
func buildNext(P string) []int { // 定义函数/方法 buildNext
	m := len(P)         // 把 长度(P) 写入 m :
	N := make([]int, m) // 把 make([]int, 映射表) 写入 N :
	for i := range N {  // 把 range N { 写入 for i :
		N[i] = -1 // 把 减 1 写入 N[i]
	}
	if m == 0 { // 若 映射表 等于 0
		return N // 返回 N
	}
	j := 0        // 把 0 写入 j :
	t := -1       // 把 减 1 写入 t :
	for j < m-1 { // for 下标 j 小于 映射表 减 1 {
		if t < 0 || P[j] == P[t] { // 若 另一字符串 小于 0 或 P[下标 j] 等于 P[另一字符串]
			j++      // 下标 j 加一
			t++      // 另一字符串 加一
			N[j] = t // 把 另一字符串 写入 N[j]
		} else { // 否则
			t = N[t] // 把 N[另一字符串] 写入 另一字符串
		}
	}
	return N // 返回 N
}

func eqIntSlice(a []int, b []int) bool { // 定义函数/方法 eqIntSlice
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
		P    string // P string
		want []int  // want []int
	}{ // }{
		{"ababaca", []int{-1, 0, 0, 1, 2, 3, 0}},
		{"aaaa", []int{-1, 0, 1, 2}},
		{"a", []int{-1}},
		{"ab", []int{-1, 0}},
		{"", []int{}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := buildNext(c.P)         // 把 buildNext(字符.P) 写入 got :
		if !eqIntSlice(got, c.want) { // 若 取反 eqIntSlice(got, 字符.want
			ok = false                                                      // 把 false 写入 ok
			fmt.Printf("FAIL buildNext(%q)=%v want %v\n", c.P, got, c.want) // 打印输出
		}
	}
	_ = reflect.DeepEqual // 把 reflect.DeepEqual 写入 _
	if !ok {              // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
