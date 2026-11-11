package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"strings" // 「strings」
)

// lengthOfLastWord 最后一个单词的长度。
// 忠实翻译 Python 参考实现 ref_lengthOfLastWord：len(s.split()[-1]) if s.split() else 0
func lengthOfLastWord(s string) int { // 定义函数/方法 lengthOfLastWord
	fields := strings.Fields(s) // 把 strings.Fields(字符串) 写入 fields :
	if len(fields) == 0 {       // 若 长度(fields) 等于 0
		return 0 // 返回 0
	}
	return len(fields[len(fields)-1]) // 定义函数/方法 len
}

func main() { // 程序入口：跑内嵌自测用例
	// 用例来自 _tools/correctness_check.py PROBLEMS["lc_58_最后一个单词的长度"]
	cases := []struct { // 把 []struct { 写入 cases :
		in   string // in string
		want int    // want int
	}{ // }{
		{"Hello World", 5},
		{"   fly me   to   the moon  ", 4},
		{"luffy is still joyboy", 6},
	}
	allOK := true             // 把 true 写入 allOK :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := lengthOfLastWord(c.in) // 把 lengthOfLastWord(字符.in) 写入 got :
		if got != c.want {            // 若 got 不等于 字符.want
			allOK = false                                                              // 把 false 写入 allOK
			fmt.Printf("FAIL lengthOfLastWord(%q) = %v, want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !allOK { // 若 取反 allOK
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
