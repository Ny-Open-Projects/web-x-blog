// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133465616
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func minWindow(s, t string) string { // 定义函数/方法 minWindow
	if len(s) == 0 || len(t) == 0 { // 若 长度(字符串) 等于 0 或 长度(另一字符串) 等于 0
		return "" // 返回 「」
	}
	target := map[byte]int{}      // 把 映射表[byte]int{} 写入 target :
	for i := 0; i < len(t); i++ { // 让 下标 i 从 0 开始计数
		target[t[i]]++ // 目标值[另一字符串[下标 i]] 加一
	}
	required := len(target)                   // 引入依赖
	window := map[byte]int{}                  // 把 映射表[byte]int{} 写入 window :
	left := 0                                 // 把 0 写入 left :
	formed := 0                               // 把 0 写入 formed :
	minLen := 0                               // 把 0 写入 minLen :
	minLeft := 0                              // 把 0 写入 minLeft :
	found := false                            // 把 false 写入 found :
	for right := 0; right < len(s); right++ { // 让 右边界 从 0 开始计数
		ch := s[right]                                        // 把 字符串[右边界] 写入 ch :
		window[ch]++                                          // window[字符] 加一
		if need, ok := target[ch]; ok && window[ch] == need { // 若 need, ok : 赋值为 目标值[字符]; ok 且 window[字符] 等于 need
			formed++ // formed 加一
		}
		for left <= right && formed == required { // 把 右边界 且 formed 等于 required { 写入 for left <
			l := right - left + 1     // 把 右边界 减 左边界 加 1 写入 l :
			if !found || l < minLen { // 若 取反 found 或 左指针 小于 minLen
				found = true   // 把 true 写入 found
				minLen = l     // 把 左指针 写入 minLen
				minLeft = left // 把 左边界 写入 minLeft
			}
			c := s[left]                                       // 把 字符串[左边界] 写入 c :
			window[c]--                                        // window[字符] 减一
			if need, ok := target[c]; ok && window[c] < need { // 若 need, ok : 赋值为 目标值[字符]; ok 且 window[字符] 小于 need
				formed-- // formed 减一
			}
			left++ // 左边界 加一
		}
	}
	if !found { // 若 取反 found
		return "" // 返回 「」
	}
	return s[minLeft : minLeft+minLen] // 返回 字符串[minLeft : minLeft 加 minLen]
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		s, t string // 字符串, 另一字符串 string
		want string // want string
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"ADOBECODEBANC", "ABC", "BANC"},
		{"a", "a", "a"},
		{"a", "aa", ""},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := minWindow(c.s, c.t); got != c.want { // 若 got : 赋值为 minWindow(字符.字符串, 字符.另一字符串); got 不等于 字符.want
			ok = false                                                              // 把 false 写入 ok
			fmt.Printf("FAIL minWindow(%q,%q)=%q want %q\n", c.s, c.t, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
