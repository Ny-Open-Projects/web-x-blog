// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130442145
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func isValid(s string) bool { // 定义判定函数 isValid
	if len(s)%2 == 1 { // 若 长度(字符串) 对…取模 2 等于 1
		return false // 返回 false
	}
	pairs := map[rune]rune{')': '(', ']': '[', '}': '{'} // 把 映射表[rune]rune{')': '(', ']': '[', '}': '{'} 写入 pairs :
	stack := []rune{}                                    // 把 []rune{} 写入 stack :
	for _, c := range s {                                // 同时取 _ 与 字符 遍历
		if c == '(' || c == '[' || c == '{' { // 若 字符 等于 '(' 或 字符 等于 '[' 或 字符 等于 '{'
			stack = append(stack, c) // 把 append(栈, 字符) 写入 栈
		} else { // 否则
			if len(stack) == 0 || stack[len(stack)-1] != pairs[c] { // 若 长度(栈) 等于 0 或 栈[长度(栈) 减 1] 不等于 pairs[字符]
				return false // 返回 false
			}
			stack = stack[:len(stack)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
		}
	}
	return len(stack) == 0 // 返回 长度(栈) 等于 0
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   string // in string
		want bool   // want bool
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"()", true},
		{"()[]{}", true},
		{"(]", false},
		{"([)]", false},
		{"{[]}", true},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := isValid(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                     // 把 false 写入 ok
			fmt.Printf("FAIL isValid(%q)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
