// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113405
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func trimSpaces(s string) []rune { // 定义函数/方法 trimSpaces
	left, right := 0, len(s)-1            // 把 0, 长度(字符串) 减 1 写入 left, right :
	for left <= right && s[left] == ' ' { // 把 右边界 且 字符串[左边界] 等于 ' ' { 写入 for left <
		left++ // 左边界 加一
	}
	for left <= right && s[right] == ' ' { // 把 右边界 且 字符串[右边界] 等于 ' ' { 写入 for left <
		right-- // 右边界 减一
	}
	out := []rune{}     // 把 []rune{} 写入 out :
	for left <= right { // 把 右边界 { 写入 for left <
		if s[left] != ' ' { // 若 字符串[左边界] 不等于 ' '
			out = append(out, rune(s[left])) // 把 append(out, rune(字符串[左边界])) 写入 out
		} else if len(out) > 0 && out[len(out)-1] != ' ' { // 否则，若 长度(out) 超过 0 且 out[长度(out) 减 1] 不等于 ' '
			out = append(out, ' ') // 把 append(out, ' ') 写入 out
		}
		left++ // 左边界 加一
	}
	return out // 返回 out
}

func reverse(l []rune, left, right int) { // 定义函数/方法 reverse
	for left < right { // for 左边界 小于 右边界 {
		l[left], l[right] = l[right], l[left] // 把 左指针[右边界], 左指针[左边界] 写入 l[left], l[right]
		left++                                // 左边界 加一
		right--                               // 右边界 减一
	}
}

func reverseEachWord(l []rune) { // 定义函数/方法 reverseEachWord
	n := len(l)        // 把 长度(左指针) 写入 n :
	start, end := 0, 0 // 把 0, 0 写入 start, end :
	for start < n {    // for 起点 小于 元素个数 {
		for end < n && l[end] != ' ' { // 把 ' ' { 写入 for end < n && l[end] !
			end++ // 终点 加一
		}
		reverse(l, start, end-1) // reverse(左指针, 起点, 终点 减 1)
		start = end + 1          // 把 终点 加 1 写入 起点
		end = start              // 把 起点 写入 终点
	}
}

func reverseWords(s string) string { // 定义函数/方法 reverseWords
	l := trimSpaces(s)      // 把 trimSpaces(字符串) 写入 l :
	reverse(l, 0, len(l)-1) // reverse(左指针, 0, 长度(左指针) 减 1)
	reverseEachWord(l)      // reverseEachWord(左指针)
	return string(l)        // 定义函数/方法 string
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   string // in string
		want string // want string
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"abc", "abc"},
		{"the sky is blue", "blue is sky the"},
		{"  hello world  ", "world hello"},
		{"a", "a"},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := reverseWords(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                          // 把 false 写入 ok
			fmt.Printf("FAIL reverseWords(%q)=%q want %q\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
