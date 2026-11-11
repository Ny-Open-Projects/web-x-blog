// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130423018
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// countBinarySubstrings2 忠实翻译 python ref solution_4___4.py（prev/curr 一次遍历）
func countBinarySubstrings2(s string) int { // 定义函数/方法 countBinarySubstrings2
	prev, curr := 0, 1            // 把 0, 1 写入 prev, curr :
	res := 0                      // 把 0 写入 res :
	for i := 1; i < len(s); i++ { // 让 下标 i 从 1 开始计数
		if s[i] != s[i-1] { // 若 字符串[下标 i] 不等于 字符串[下标 i 减 1]
			res += min(prev, curr) // 结果累加 取较小值 前一个, 当前值)
			prev, curr = curr, 1   // 把 当前值, 1 写入 prev, curr
		} else { // 否则
			curr++ // 当前值 加一
		}
	}
	return res + min(prev, curr) // 返回 结果 加 取较小值 前一个, 当前值)
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
		if got := countBinarySubstrings2(c.in); got != c.want { // 若 got : 赋值为 countBinarySubstrings2(字符.in); got 不等于 字符.want
			ok = false                                                   // 把 false 写入 ok
			fmt.Printf("FAIL solve(%q)=%d want %d\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
