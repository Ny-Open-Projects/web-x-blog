// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
package main // 引入依赖

import (
	"fmt"
	"os"
	"strings"
) // 引入依赖

func isNumber(s string) bool { // 定义判定函数 isNumber
	s = strings.TrimSpace(s) // 把 strings.TrimSpace(字符串) 写入 字符串
	if len(s) == 0 {         // 若 长度(字符串) 等于 0
		return false // 返回 false
	}
	hasDot, hasE, hasDigit := false, false, false // 把 false, false, false 写入 hasDot, hasE, hasDigit :
	for i := 0; i < len(s); i++ {                 // 让 下标 i 从 0 开始计数
		c := s[i]                 // 把 字符串[下标 i] 写入 c :
		if c >= '0' && c <= '9' { // 若 字符 不低于 '0' 且 字符 不超过 '9'
			hasDigit = true // 把 true 写入 hasDigit
		} else if c == '+' || c == '-' { // 否则，若 字符 等于 ' 加 ' 或 字符 等于 ' 减 '
			if i > 0 && (s[i-1] != 'e' && s[i-1] != 'E') { // 若 下标 i 超过 0 且 (字符串[下标 i 减 1] 不等于 'e' 且 字符串[下标 i 减 1] 不等于 'E'
				return false // 返回 false
			}
		} else if c == '.' { // 否则，若 字符 等于 '.'
			if hasDot || hasE { // 若 hasDot 或 hasE
				return false // 返回 false
			}
			hasDot = true // 把 true 写入 hasDot
		} else if c == 'e' || c == 'E' { // 否则，若 字符 等于 'e' 或 字符 等于 'E'
			if hasE || !hasDigit { // 若 hasE 或 取反 hasDigit
				return false // 返回 false
			}
			hasE = true // 把 true 写入 hasE
		} else { // 否则
			return false // 返回 false
		}
	}
	return hasDigit // 返回 hasDigit
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   string // in string
		want bool   // want bool
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"0", true},
		{"abc", false},
		{"123", true},
		{"", false},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := isNumber(c.in); got != c.want { // 若 got : 赋值为 isNumber(字符.in); got 不等于 字符.want
			ok = false                                                      // 把 false 写入 ok
			fmt.Printf("FAIL isNumber(%q)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
