// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135037359
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

// restoreIpAddresses 是 Python 参考 solution_3 的忠实翻译（回溯）。
func restoreIpAddresses(s string) []string { // 定义函数/方法 restoreIpAddresses
	res := []string{}                            // 把 []string{} 写入 res :
	var backtrack func(start int, path []string) // var backtrack func(起点 int, 当前路径 []string)
	backtrack = func(start int, path []string) { // 把 func(起点 int, 当前路径 []string) { 写入 backtrack
		if len(path) == 4 { // 若 长度(当前路径) 等于 4
			if start == len(s) { // 若 起点 等于 长度(字符串
				ip := ""                 // 把 「」 写入 ip :
				for i, p := range path { // 同时取 下标 i 与 节点 遍历
					if i > 0 { // 若 下标 i 超过 0
						ip += "." // ip累加 「.」
					}
					ip += p // ip累加 节点
				}
				res = append(res, ip) // 把 append(结果, ip) 写入 结果
			}
			return // return
		}
		for length := 1; length <= 3; length++ { // 让 长度 从 1 开始计数
			if start+length > len(s) { // 若 起点 加 长度 超过 长度(字符串
				break // 跳出循环
			}
			segment := s[start : start+length] // 把 字符串[起点 : 起点 加 长度] 写入 segment :
			if (len(segment) > 1 && segment[0] == '0') || atoiSafe(segment) > 255 {
				continue // 跳过本轮，进入下一次
			}
			backtrack(start+length, append(path, segment)) // backtrack(起点 加 长度, append(当前路径, segment))
		}
	}
	backtrack(0, []string{}) // backtrack(0, []string{})
	return res               // 返回 结果
}

func atoiSafe(s string) int { // 定义函数/方法 atoiSafe
	n := 0                // 把 0 写入 n :
	for _, c := range s { // 同时取 _ 与 字符 遍历
		n = n*10 + int(c-'0') // 把 元素个数 乘 10 加 int(字符 减 '0') 写入 元素个数
	}
	return n // 返回 元素个数
}

// normStrSlice 排序以便做无序比较。
func normStrSlice(a []string) []string { // 定义函数/方法 normStrSlice
	b := make([]string, len(a)) // 把 make([]string, 长度(数组)) 写入 b :
	copy(b, a)                  // copy(b, 数组)
	sort.Strings(b)             // sort.Strings(b)
	return b                    // 返回 b
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		s    string   // 字符串 string
		want []string // want []string
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"101023", []string{"1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"}},
		{"25525511135", []string{"255.255.11.135", "255.255.111.35"}},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := normStrSlice(restoreIpAddresses(c.s)) // 把 normStrSlice(restoreIpAddresses(字符.字符串)) 写入 got :
		want := normStrSlice(c.want)                 // 把 normStrSlice(字符.want) 写入 want :
		if !reflect.DeepEqual(got, want) {           // 若 取反 reflect.DeepEqual(got, want
			fmt.Printf("FAIL %q got=%v want=%v\n", c.s, got, want) // 打印输出
			os.Exit(1)                                             // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
