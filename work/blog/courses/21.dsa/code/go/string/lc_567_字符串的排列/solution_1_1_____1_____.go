// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

// 忠实翻译 python/string/lc_567_字符串的排列/solution_1_1_____1_____.py
func checkInclusion(s1, s2 string) bool { // 定义判定函数 checkInclusion
	if len(s1) > len(s2) {
		return false
	} // 若 长度(s1) 超过 长度(s2) { return false }
	s1c := make([]int, 26)         // 把 make([]int, 26) 写入 s1c :
	s2c := make([]int, 26)         // 把 make([]int, 26) 写入 s2c :
	for i := 0; i < len(s1); i++ { // 让 下标 i 从 0 开始计数
		s1c[s1[i]-'a']++ // s1c[s1[下标 i] 减 '数组'] 加一
		s2c[s2[i]-'a']++ // s2c[s2[下标 i] 减 '数组'] 加一
	}
	if eqArr(s1c, s2c) {
		return true
	} // 若 eqArr(s1c, s2c) { return true }
	L := len(s1)                   // 把 长度(s1) 写入 L :
	for i := L; i < len(s2); i++ { // 把 L; 下标 i 小于 长度(s2); 下标 i 加一 { 写入 for i :
		s2c[s2[i]-'a']++   // s2c[s2[下标 i] 减 '数组'] 加一
		s2c[s2[i-L]-'a']-- // s2c[s2[下标 i 减 L] 减 '数组'] 减一
		if eqArr(s1c, s2c) {
			return true
		} // 若 eqArr(s1c, s2c) { return true }
	}
	return false // 返回 false
}

func eqArr(a, b []int) bool { return reflect.DeepEqual(a, b) } // 定义函数/方法 eqArr

func main() { // 程序入口：跑内嵌自测用例
	type caseT struct {
		s1, s2 string
		want   bool
	} // 定义类型
	cases := []caseT{ // 把 []caseT{ 写入 cases :
		{"ab", "eidbaooo", true},
		{"ab", "eidboaoo", false},
		{"hello", "ooolleoooleh", false},
		{"a", "a", true},
		{"abc", "cccccbabbbaaaa", true},
		{"ab", "xyz", false},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := checkInclusion(c.s1, c.s2); got != c.want { // 若 got : 赋值为 checkInclusion(字符.s1, 字符.s2); got 不等于 字符.want
			ok = false                                                                     // 把 false 写入 ok
			fmt.Printf("FAIL checkInclusion(%q,%q)=%v want %v\n", c.s1, c.s2, got, c.want) // 打印输出
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
