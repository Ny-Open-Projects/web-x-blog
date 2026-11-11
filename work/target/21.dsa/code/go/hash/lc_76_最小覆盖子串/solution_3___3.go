// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133465616
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func minWindow(s, t string) string { // 定义函数/方法 minWindow
	if len(t) == 0 { // 若 长度(另一字符串) 等于 0
		return "" // 返回 「」
	}
	need := map[byte]int{}        // 把 映射表[byte]int{} 写入 need :
	for i := 0; i < len(t); i++ { // 让 下标 i 从 0 开始计数
		need[t[i]]++ // need[另一字符串[下标 i]] 加一
	}
	mSize := len(need)            // 把 长度(need) 写入 mSize :
	l := 0                        // 把 0 写入 l :
	res := ""                     // 把 「」 写入 res :
	for r := 0; r < len(s); r++ { // 让 右指针 从 0 开始计数
		c := s[r]                 // 把 字符串[右指针] 写入 c :
		if _, ok := need[c]; ok { // 若 _, ok : 赋值为 need[字符]; ok
			need[c]--         // need[字符] 减一
			if need[c] == 0 { // 若 need[字符] 等于 0
				mSize-- // mSize 减一
			}
		}
		for mSize == 0 { // 把 赋值为 0 { 写入 for mSize
			newRes := s[l : r+1]                         // 把 字符串[左指针 : 右指针 加 1] 写入 newRes :
			if len(res) == 0 || len(newRes) < len(res) { // 定义函数/方法 len
				res = newRes // 把 newRes 写入 结果
			}
			c2 := s[l]                 // 把 字符串[左指针] 写入 c2 :
			if _, ok := need[c2]; ok { // 若 _, ok : 赋值为 need[c2]; ok
				need[c2]++         // need[c2] 加一
				if need[c2] == 1 { // 若 need[c2] 等于 1
					mSize++ // mSize 加一
				}
			}
			l++ // 左指针 加一
		}
	}
	return res // 返回 结果
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
