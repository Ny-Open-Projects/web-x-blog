// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130442145
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func isValid(s string) bool { // 定义判定函数 isValid
	stack := []byte{}                                    // 把 []byte{} 写入 stack :
	pairs := map[byte]byte{')': '(', ']': '[', '}': '{'} // 把 映射表[byte]byte{')': '(', ']': '[', '}': '{'} 写入 pairs :
	for i := 0; i < len(s); i++ {                        // 让 下标 i 从 0 开始计数
		ch := s[i]                      // 把 字符串[下标 i] 写入 ch :
		if close, ok := pairs[ch]; ok { // 若 close, ok : 赋值为 pairs[字符]; ok
			top := byte('#')    // 把 byte('#') 写入 top :
			if len(stack) > 0 { // 若 长度(栈) 超过 0
				top = stack[len(stack)-1]    // 把 栈[长度(栈) 减 1] 写入 top
				stack = stack[:len(stack)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
			}
			if top != close { // 若 top 不等于 close
				return false // 返回 false
			}
		} else { // 否则
			stack = append(stack, ch) // 把 append(栈, 字符) 写入 栈
		}
	}
	return len(stack) == 0 // 返回 长度(栈) 等于 0
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   string // in string
		want bool   // want bool
	}{ // }{
		{"()", true},
		{"()[]{}", true},
		{"(]", false},
		{"", true},
		{"([])", true},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if g := isValid(c.in); g != c.want { // 若 g : 赋值为 isValid(字符.in); g 不等于 字符.want
			ok = false                                          // 把 false 写入 ok
			fmt.Printf("FAIL %q=%v want %v\n", c.in, g, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
