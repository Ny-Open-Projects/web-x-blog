// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130414333
package main // 引入依赖

import (
	"fmt"
	"os"
	"strings"
) // 引入依赖

func reverseWords(s string) string { // 定义函数/方法 reverseWords
	words := strings.Split(s, " ") // 把 strings.Split(字符串, 「 」) 写入 words :
	for i, w := range words {      // 同时取 下标 i 与 权重 遍历
		words[i] = reverseString(w) // 把 reverseString(权重) 写入 words[i]
	}
	return strings.Join(words, " ") // 返回 strings.Join(单词列表, 「 」)
}

func reverseString(w string) string { // 定义函数/方法 reverseString
	r := []rune(w) // 把 []rune(权重) 写入 r :
	for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i] // 把 右指针[下标 j], 右指针[下标 i] 写入 r[i], r[j]
	}
	return string(r) // 定义函数/方法 string
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true          // 把 true 写入 ok :
	cases := []struct { // 把 []struct { 写入 cases :
		in   string // in string
		want string // want string
	}{ // }{
		{"Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"},
		{"ab cd", "ba dc"},
		{"", ""},
		{"a", "a"},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := reverseWords(c.in); got != c.want { // 若 got : 赋值为 reverseWords(字符.in); got 不等于 字符.want
			ok = false                                                          // 把 false 写入 ok
			fmt.Printf("FAIL reverseWords(%q)=%q want %q\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
