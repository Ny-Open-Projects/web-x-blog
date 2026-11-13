// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130423018
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// countBinarySubstrings 忠实翻译 python ref solution_3___3.py（for 循环分组 + 相邻 min 求和）
func countBinarySubstrings(s string) int { // 定义函数/方法 countBinarySubstrings
	groups := []int{}             // 把 []int{} 写入 groups :
	count := 1                    // 把 1 写入 count :
	for i := 1; i < len(s); i++ { // 让 下标 i 从 1 开始计数
		if s[i] == s[i-1] { // 若 字符串[下标 i] 等于 字符串[下标 i 减 1]
			count++ // 计数 加一
		} else { // 否则
			groups = append(groups, count) // 把 append(groups, 计数) 写入 groups
			count = 1                      // 把 1 写入 计数
		}
	}
	groups = append(groups, count)       // 把 append(groups, 计数) 写入 groups
	ans := 0                             // 把 0 写入 ans :
	for i := 0; i+1 < len(groups); i++ { // 让 下标 i 从 0 开始计数
		ans += min(groups[i], groups[i+1]) // 答案累加 取较小值 groups[下标 i], groups[下标 i 加 1])
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   string // in string
		want int    // want int
	}{ // }{
		{"00110011", 6},
		{"10101", 4},
		{"", 0},
		{"0", 0},
		{"0011", 2},
		{"000111", 3},
		{"00100", 2},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := countBinarySubstrings(c.in); got != c.want { // 若 got : 赋值为 countBinarySubstrings(字符.in); got 不等于 字符.want
			ok = false                                                   // 把 false 写入 ok
			fmt.Printf("FAIL solve(%q)=%d want %d\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
