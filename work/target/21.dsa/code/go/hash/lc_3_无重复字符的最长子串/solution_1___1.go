// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133461048
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func lengthOfLongestSubstring(s string) int { // 定义函数/方法 lengthOfLongestSubstring
	seen := map[byte]bool{}                   // 把 映射表[byte]bool{} 写入 seen :
	left := 0                                 // 把 0 写入 left :
	maxLen := 0                               // 把 0 写入 maxLen :
	for right := 0; right < len(s); right++ { // 让 右边界 从 0 开始计数
		ch := s[right] // 把 字符串[右边界] 写入 ch :
		for seen[ch] { // for 已见集合[字符] {
			delete(seen, s[left]) // delete(已见集合, 字符串[左边界])
			left++                // 左边界 加一
		}
		seen[ch] = true            // 把 true 写入 seen[ch]
		if right-left+1 > maxLen { // 若 右边界 减 左边界 加 1 超过 maxLen
			maxLen = right - left + 1 // 把 右边界 减 左边界 加 1 写入 maxLen
		}
	}
	return maxLen // 返回 maxLen
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   string // in string
		want int    // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"abc", 3},
		{"bbbbb", 1},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := lengthOfLongestSubstring(c.in); got != c.want { // 若 got : 赋值为 lengthOfLongestSubstring(字符.in); got 不等于 字符.want
			ok = false                                                                      // 把 false 写入 ok
			fmt.Printf("FAIL lengthOfLongestSubstring(%q)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
