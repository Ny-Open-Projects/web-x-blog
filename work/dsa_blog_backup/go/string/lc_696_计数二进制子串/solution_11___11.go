// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130423018
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// countBinarySubstrings 忠实翻译 python ref solution_11___11.py（groups 分组 + 相邻 min 求和）
func countBinarySubstrings(s string) int { // 定义函数/方法 countBinarySubstrings
	groups := []int{} // 把 []int{} 写入 groups :
	i := 0            // 把 0 写入 i :
	n := len(s)       // 把 长度(字符串) 写入 n :
	for i < n {       // for 下标 i 小于 元素个数 {
		ch := s[i]                // 把 字符串[下标 i] 写入 ch :
		cnt := 0                  // 把 0 写入 cnt :
		for i < n && s[i] == ch { // 把 赋值为 字符 { 写入 for i < n && s[i]
			cnt++ // 计数 加一
			i++   // 下标 i 加一
		}
		groups = append(groups, cnt) // 把 append(groups, 计数) 写入 groups
	}
	ans := 0                           // 把 0 写入 ans :
	for j := 1; j < len(groups); j++ { // 让 下标 j 从 1 开始计数
		ans += min(groups[j-1], groups[j]) // 答案累加 取较小值 groups[下标 j 减 1], groups[下标 j])
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
