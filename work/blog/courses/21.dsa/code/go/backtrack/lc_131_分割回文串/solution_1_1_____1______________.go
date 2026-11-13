// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145240399
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

// partition 忠实翻译 python ref solution_1_1_____1______________.py（回溯，直接切片判回文）
func partition(s string) [][]string { // 定义函数/方法 partition
	var result [][]string                        // var 结果 [][]string
	var backtrack func(start int, path []string) // var backtrack func(起点 int, 当前路径 []string)
	backtrack = func(start int, path []string) { // 把 func(起点 int, 当前路径 []string) { 写入 backtrack
		if start == len(s) { // 若 起点 等于 长度(字符串
			cp := make([]string, len(path)) // 把 make([]string, 长度(当前路径)) 写入 cp :
			copy(cp, path)                  // copy(cp, 当前路径)
			result = append(result, cp)     // 把 append(结果, cp) 写入 结果
			return                          // return
		}
		for end := start + 1; end <= len(s); end++ { // 把 起点 加 1; 终点 不超过 长度(字符串); 终点 加一 { 写入 for end :
			sub := s[start:end]         // 把 字符串[起点:终点] 写入 sub :
			if sub == reverseStr(sub) { // 若 sub 等于 reverseStr(sub
				path = append(path, sub)  // 把 append(当前路径, sub) 写入 当前路径
				backtrack(end, path)      // backtrack(终点, 当前路径)
				path = path[:len(path)-1] // 把 当前路径[:长度(当前路径) 减 1] 写入 当前路径
			}
		}
	}
	backtrack(0, []string{}) // backtrack(0, []string{})
	return result            // 返回 结果
}

func reverseStr(s string) string { // 定义函数/方法 reverseStr
	b := []byte(s) // 把 []byte(字符串) 写入 b :
	for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
		b[i], b[j] = b[j], b[i] // 把 b[下标 j], b[下标 i] 写入 b[i], b[j]
	}
	return string(b) // 定义函数/方法 string
}

func main() { // 程序入口：跑内嵌自测用例
	// want 由 python ref 实跑得到（含回溯顺序）
	cases := []struct { // 把 []struct { 写入 cases :
		in   string     // in string
		want [][]string // want [][]string
	}{ // }{
		{"aab", [][]string{{"a", "a", "b"}, {"aa", "b"}}},
		{"abc", [][]string{{"a", "b", "c"}}},
		{"", [][]string{{}}},
		{"a", [][]string{{"a"}}},
		{"aba", [][]string{{"a", "b", "a"}, {"aba"}}},
		{"bb", [][]string{{"b", "b"}, {"bb"}}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := partition(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                   // 把 false 写入 ok
			fmt.Printf("FAIL solve(%q)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
