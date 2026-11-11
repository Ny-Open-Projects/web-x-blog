// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113405
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"strings" // 「strings」
)

func reverseWords(s string) string { // 定义函数/方法 reverseWords
	left, right := 0, len(s)-1 // 把 0, 长度(字符串) 减 1 写入 left, right :
	words := []string{}        // 把 []string{} 写入 words :
	word := []rune{}           // 把 []rune{} 写入 word :
	for left <= right {        // 把 右边界 { 写入 for left <
		if s[left] == ' ' && len(word) > 0 { // 若 字符串[左边界] 等于 ' ' 且 长度(单词) 超过 0
			words = append([]string{string(word)}, words...) // 把 append([]string{string(单词)}, 单词列表...) 写入 单词列表
			word = []rune{}                                  // 把 []rune{} 写入 单词
		} else if s[left] != ' ' { // 否则，若 字符串[左边界] 不等于 ' '
			word = append(word, rune(s[left])) // 把 append(单词, rune(字符串[左边界])) 写入 单词
		}
		left++ // 左边界 加一
	}
	if len(word) > 0 { // 若 长度(单词) 超过 0
		words = append([]string{string(word)}, words...) // 把 append([]string{string(单词)}, 单词列表...) 写入 单词列表
	}
	return strings.Join(words, " ") // 返回 strings.Join(单词列表, 「 」)
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
