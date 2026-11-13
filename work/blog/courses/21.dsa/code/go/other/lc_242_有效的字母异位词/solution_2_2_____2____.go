// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355461
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// isAnagram 判断两个字符串是否为字母异位词（哈希计数法）。
// 忠实翻译 Python 参考实现：Counter(s) == Counter(t)
func isAnagram(s string, t string) bool { // 定义判定函数 isAnagram
	if len(s) != len(t) { // 定义函数/方法 len
		return false // 返回 false
	}
	cnt := make(map[rune]int) // 把 make(映射表[rune]int) 写入 cnt :
	for _, r := range s {     // 同时取 _ 与 右指针 遍历
		cnt[r]++ // 计数[右指针] 加一
	}
	for _, r := range t { // 同时取 _ 与 右指针 遍历
		cnt[r]--        // 计数[右指针] 减一
		if cnt[r] < 0 { // 若 计数[右指针] 小于 0
			return false // 返回 false
		}
	}
	for _, v := range cnt { // 同时取 _ 与 值 遍历
		if v != 0 { // 若 值 不等于 0
			return false // 返回 false
		}
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	// 用例来自 _tools/correctness_check.py PROBLEMS["lc_242_有效的字母异位词"]
	cases := []struct { // 把 []struct { 写入 cases :
		s, t string // 字符串, 另一字符串 string
		want bool   // want bool
	}{ // }{
		{"anagram", "nagaram", true},
		{"rat", "car", false},
		{"aacc", "ccac", false},
	}
	allOK := true             // 把 true 写入 allOK :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := isAnagram(c.s, c.t) // 把 isAnagram(字符.字符串, 字符.另一字符串) 写入 got :
		if got != c.want {         // 若 got 不等于 字符.want
			allOK = false                                                              // 把 false 写入 allOK
			fmt.Printf("FAIL isAnagram(%q,%q) = %v, want %v\n", c.s, c.t, got, c.want) // 打印输出
		}
	}
	if !allOK { // 若 取反 allOK
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
