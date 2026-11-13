// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133461048
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func lengthOfLongestSubstring(s string) int { // 定义函数/方法 lengthOfLongestSubstring
	last := map[byte]int{}        // 把 映射表[byte]int{} 写入 last :
	l := 0                        // 把 0 写入 l :
	res := 0                      // 把 0 写入 res :
	for r := 0; r < len(s); r++ { // 让 右指针 从 0 开始计数
		ch := s[r]                           // 把 字符串[右指针] 写入 ch :
		if p, ok := last[ch]; ok && p >= l { // 若 节点, ok : 赋值为 last[字符]; ok 且 节点 不低于 左指针
			l = p + 1 // 把 节点 加 1 写入 左指针
		}
		if r-l+1 > res { // 若 右指针 减 左指针 加 1 超过 结果
			res = r - l + 1 // 把 右指针 减 左指针 加 1 写入 结果
		}
		last[ch] = r // 把 右指针 写入 last[ch]
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   string // in string
		want int    // want int
	}{ // }{
		{"abcabcbb", 3},
		{"bbbbb", 1},
		{"pwwkew", 3},
		{"", 0},
		{"au", 2},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if g := lengthOfLongestSubstring(c.in); g != c.want { // 若 g : 赋值为 lengthOfLongestSubstring(字符.in); g 不等于 字符.want
			ok = false                                          // 把 false 写入 ok
			fmt.Printf("FAIL %q=%v want %v\n", c.in, g, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
