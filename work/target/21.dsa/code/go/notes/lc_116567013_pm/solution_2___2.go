// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 忠实翻译 python/notes/lc_116567013_pm/solution_2___2.py
// Brute-Force 模式匹配（版本2：双循环对齐）。每次对齐后用内层循环逐字符比较。
func matchV2(P string, T string) int { // 定义函数/方法 matchV2
	n := len(T)                 // 把 长度(T) 写入 n :
	m := len(P)                 // 把 长度(P) 写入 m :
	for i := 0; i <= n-m; i++ { // 让 下标 i 从 0 开始计数
		j := 0                        // 把 0 写入 j :
		for j < m && T[i+j] == P[j] { // 把 赋值为 P[下标 j] { 写入 for j < m && T[i+j]
			j++ // 下标 j 加一
		}
		if j == m { // 若 下标 j 等于 映射表
			return i // 返回 下标 i
		}
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
		{"time", 11},
		{"o", 1},
		{"come", 39},
		{"xyz", -1},
		{"nope", -1},
		{"", 0},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := matchV2(c.P, T) // 把 matchV2(字符.P, T) 写入 got :
		if got != c.want {     // 若 got 不等于 字符.want
			ok = false                                                    // 把 false 写入 ok
			fmt.Printf("FAIL matchV2(%q)=%d want %d\n", c.P, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
