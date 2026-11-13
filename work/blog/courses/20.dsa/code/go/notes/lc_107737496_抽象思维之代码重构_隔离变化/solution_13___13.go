// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// match 扫描 text，若任一位置匹配 regexp 则返回 true（同 grep，方案 13）。
func match(regexp, text string) bool { // 定义函数/方法 match
	if len(regexp) > 0 && regexp[0] == '^' { // 若 长度(regexp) 超过 0 且 regexp[0] 等于 ' 按位异或 '
		return matchhere(regexp[1:], text) // 定义函数/方法 matchhere
	}
	i := 0 // 把 0 写入 i :
	for {  // for {
		if matchhere(regexp, text[i:]) { // 定义函数/方法 matchhere
			return true // 返回 true
		}
		if i >= len(text) { // 若 下标 i 不低于 长度(text
			break // 跳出循环
		}
		i++ // 下标 i 加一
	}
	return false // 返回 false
}

func matchhere(regexp, text string) bool { // 定义函数/方法 matchhere
	if regexp == "" { // 若 regexp 等于 「」
		return true // 返回 true
	}
	if len(regexp) >= 2 && regexp[1] == '*' { // 若 长度(regexp) 不低于 2 且 regexp[1] 等于 ' 乘 '
		return matchstar(regexp[0], regexp[2:], text) // 定义函数/方法 matchstar
	}
	if regexp[0] == '$' && len(regexp) == 1 { // 若 regexp[0] 等于 '$' 且 长度(regexp) 等于 1
		return text == "" // 返回 text 等于 「」
	}
	if len(text) > 0 && (regexp[0] == '.' || regexp[0] == text[0]) { // 定义函数/方法 len
		return matchhere(regexp[1:], text[1:]) // 定义函数/方法 matchhere
	}
	return false // 返回 false
}

func matchstar(c byte, regexp, text string) bool { // 定义函数/方法 matchstar
	i := 0 // 把 0 写入 i :
	for {  // for {
		if matchhere(regexp, text[i:]) { // 定义函数/方法 matchhere
			return true // 返回 true
		}
		if i >= len(text) { // 若 下标 i 不低于 长度(text
			break // 跳出循环
		}
		if text[i] != c && c != '.' { // 若 text[下标 i] 不等于 字符 且 字符 不等于 '.'
			break // 跳出循环
		}
		i++ // 下标 i 加一
	}
	return false // 返回 false
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		regexp string // regexp string
		text   string // text string
		want   bool   // want bool
	}{ // }{
		{"abc", "xxabcxx", true},
		{"a.c", "axc", true},
		{"a*", "aaaa", true},
		{"^a", "ba", false},
		{"c$", "abc", true},
		{"a.*c", "aXYZc", true},
		{"a*", "", true},
		{"^abc$", "abc", true},
		{"^abc$", "abcd", false},
		{"xyz", "abc", false},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := match(c.regexp, c.text); got != c.want { // 若 got : 赋值为 match(字符.regexp, 字符.text); got 不等于 字符.want
			ok = false                                                                  // 把 false 写入 ok
			fmt.Printf("FAIL match(%q,%q)=%v want %v\n", c.regexp, c.text, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
