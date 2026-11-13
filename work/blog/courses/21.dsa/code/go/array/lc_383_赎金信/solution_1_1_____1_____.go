// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355797
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func canConstruct(ransomNote, magazine string) bool { // 定义函数/方法 canConstruct
	if len(ransomNote) > len(magazine) { // 定义函数/方法 len
		return false // 返回 false
	}
	cnt := make([]int, 26)       // 把 make([]int, 26) 写入 cnt :
	for _, c := range magazine { // 同时取 _ 与 字符 遍历
		cnt[c-'a']++ // 计数[字符 减 '数组'] 加一
	}
	for _, c := range ransomNote { // 同时取 _ 与 字符 遍历
		cnt[c-'a']--        // 计数[字符 减 '数组'] 减一
		if cnt[c-'a'] < 0 { // 若 计数[字符 减 '数组'] 小于 0
			return false // 返回 false
		}
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		ransom string // ransom string
		mag    string // mag string
		want   bool   // want bool
	}{ // }{
		{"a", "b", false},
		{"aa", "ab", false},
		{"aa", "aab", true},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := canConstruct(c.ransom, c.mag) // 把 canConstruct(字符.ransom, 字符.mag) 写入 got :
		if got != c.want {                   // 若 got 不等于 字符.want
			fmt.Printf("FAIL ransom=%q mag=%q want=%v got=%v\n", c.ransom, c.mag, c.want, got) // 打印输出
			ok = false                                                                         // 把 false 写入 ok
		}
	}
	if !ok { // 若 取反 ok
		fmt.Println("RESULT: FAIL") // 打印输出
		os.Exit(1)                  // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
