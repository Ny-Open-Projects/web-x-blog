// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
package main // 引入依赖

import (
	"fmt"
	"os"
	"strings"
) // 引入依赖

func isNumber(s string) bool { // 定义判定函数 isNumber
	graph := map[int]map[string]int{ // 把 映射表[int]映射表[string]int{ 写入 graph :
		0: {"blank": 0, "sign": 1, ".": 2, "digit": 6},
		1: {"digit": 6, ".": 2},
		2: {"digit": 3},
		3: {"digit": 3, "e": 4},
		4: {"digit": 5, "sign": 7},
		5: {"digit": 5},
		6: {"digit": 6, ".": 3, "e": 4},
		7: {"digit": 5},
	}
	state := 0             // 把 0 写入 state :
	for _, ch := range s { // 同时取 _ 与 字符 遍历
		c := string(ch)             // 把 string(字符) 写入 c :
		if ch >= '0' && ch <= '9' { // 若 字符 不低于 '0' 且 字符 不超过 '9'
			c = "digit" // 把 「digit」 写入 字符
		} else if ch == ' ' { // 否则，若 字符 等于 ' '
			c = "blank" // 把 「blank」 写入 字符
		} else if ch == '+' || ch == '-' { // 否则，若 字符 等于 ' 加 ' 或 字符 等于 ' 减 '
			c = "sign" // 把 「sign」 写入 字符
		} else { // 否则
			c = strings.ToLower(string(ch)) // 把 strings.ToLower(string(字符)) 写入 字符
		}
		next, ok := graph[state][c] // 把 graph[state][字符] 写入 next, ok :
		if !ok {                    // 若 取反 ok
			return false // 返回 false
		}
		state = next // 把 下一个 写入 state
	}
	return state == 3 || state == 5 || state == 6 // 返回 state 等于 3 或 state 等于 5 或 state 等于 6
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
