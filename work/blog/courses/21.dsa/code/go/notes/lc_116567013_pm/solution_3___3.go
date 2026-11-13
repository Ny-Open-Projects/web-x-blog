// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

// 忠实翻译 python/notes/lc_116567013_pm/solution_3___3.py
// 构造 KMP 的 next 失效函数（look-up table）。
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

// KMP 模式匹配：借助 next 表在失配时大步跳跃，最坏 O(n)。
func kmpMatch(P string, T string) int { // 定义函数/方法 kmpMatch
	N := buildNext(P)    // 把 buildNext(P) 写入 N :
	n := len(T)          // 把 长度(T) 写入 n :
	m := len(P)          // 把 长度(P) 写入 m :
	i := 0               // 把 0 写入 i :
	j := 0               // 把 0 写入 j :
	for j < m && i < n { // for 下标 j 小于 映射表 且 下标 i 小于 元素个数 {
		if j < 0 || T[i] == P[j] { // 若 下标 j 小于 0 或 T[下标 i] 等于 P[下标 j]
			i++ // 下标 i 加一
			j++ // 下标 j 加一
		} else { // 否则
			j = N[j] // 把 N[下标 j] 写入 下标 j
		}
	}
	if j == m { // 若 下标 j 等于 映射表
		return i - j // 返回 下标 i 减 下标 j
	}
	return -1 // 返回 减 1
}

func main() { // 程序入口：跑内嵌自测用例
	T := "now is the time for all good people to come" // 把 「now is the time for all good people to come」 写入 T :
	type tc struct {                                   // 定义类型
		P    string // P string
		want int    // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"people", 29},
		{"all", 20},
		{"time", 11},
		{"o", 1},
		{"come", 39},
		{"xyz", -1},
		{"nope", -1},
		{"", 0},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := kmpMatch(c.P, T) // 把 kmpMatch(字符.P, T) 写入 got :
		if got != c.want {      // 若 got 不等于 字符.want
			ok = false                                                     // 把 false 写入 ok
			fmt.Printf("FAIL kmpMatch(%q)=%d want %d\n", c.P, got, c.want) // 打印输出
		}
	}
	// 附带校验 next 表
	tableCases := []struct { // 把 []struct { 写入 tableCases :
		P    string // P string
		want []int  // want []int
	}{ // }{
		{"ababaca", []int{-1, 0, 0, 1, 2, 3, 0}},
		{"aaaa", []int{-1, 0, 1, 2}},
		{"a", []int{-1}},
		{"ab", []int{-1, 0}},
		{"", []int{}},
	}
	for _, c := range tableCases { // 同时取 _ 与 字符 遍历
		got := buildNext(c.P)                                                             // 把 buildNext(字符.P) 写入 got :
		if len(got) != len(c.want) || (len(got) > 0 && !reflect.DeepEqual(got, c.want)) { // 定义函数/方法 len
			ok = false                                                      // 把 false 写入 ok
			fmt.Printf("FAIL buildNext(%q)=%v want %v\n", c.P, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
