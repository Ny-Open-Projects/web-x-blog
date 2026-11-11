// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114949
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// isPalindrome 验证回文串（筛选 + 双指针）。
// 忠实翻译 Python 参考实现：t = [c.lower() for c in s if c.isalnum()]; t == t[::-1]
func isPalindrome(s string) bool { // 定义判定函数 isPalindrome
	filtered := make([]rune, 0, len(s)) // 把 make([]rune, 0, 长度(字符串)) 写入 filtered :
	for _, r := range s {               // 同时取 _ 与 右指针 遍历
		if isAlnum(r) { // 定义判定函数 isAlnum
			filtered = append(filtered, toLower(r)) // 把 append(filtered, toLower(右指针)) 写入 filtered
		}
	}
	for i, j := 0, len(filtered)-1; i < j; i, j = i+1, j-1 {
		if filtered[i] != filtered[j] { // 若 filtered[下标 i] 不等于 filtered[下标 j]
			return false // 返回 false
		}
	}
	return true // 返回 true
}

func isAlnum(r rune) bool { // 定义判定函数 isAlnum
	return (r >= 'a' && r <= 'z') || (r >= 'A' && r <= 'Z') || (r >= '0' && r <= '9')
}

func toLower(r rune) rune { // 定义函数/方法 toLower
	if r >= 'A' && r <= 'Z' { // 若 右指针 不低于 'A' 且 右指针 不超过 'Z'
		return r + ('a' - 'A') // 返回 右指针 加 ('数组' 减 'A')
	}
	return r // 返回 右指针
}

func main() { // 程序入口：跑内嵌自测用例
	// 用例来自 _tools/correctness_check.py PROBLEMS["lc_125_验证回文串"]
	cases := []struct { // 把 []struct { 写入 cases :
		s    string // 字符串 string
		want bool   // want bool
	}{ // }{
		{"A man, a plan, a canal: Panama", true},
		{"race a car", false},
		{" ", true},
	}
	allOK := true             // 把 true 写入 allOK :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := isPalindrome(c.s) // 把 isPalindrome(字符.字符串) 写入 got :
		if got != c.want {       // 若 got 不等于 字符.want
			allOK = false                                                         // 把 false 写入 allOK
			fmt.Printf("FAIL isPalindrome(%q) = %v, want %v\n", c.s, got, c.want) // 打印输出
		}
	}
	if !allOK { // 若 取反 allOK
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
