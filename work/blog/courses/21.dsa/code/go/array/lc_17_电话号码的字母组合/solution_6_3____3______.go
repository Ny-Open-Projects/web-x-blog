// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130444168
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

func letterCombinations(digits string) []string { // 定义函数/方法 letterCombinations
	if digits == "" { // 若 digits 等于 「」
		return []string{} // 返回 []string{}
	}
	mapping := map[byte]string{'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
	combos := []string{""}             // 把 []string{「」} 写入 combos :
	for i := 0; i < len(digits); i++ { // 让 下标 i 从 0 开始计数
		d := digits[i]             // 把 digits[下标 i] 写入 d :
		var next []string          // var 下一个 []string
		for _, p := range combos { // 同时取 _ 与 节点 遍历
			for _, c := range mapping[d] { // 同时取 _ 与 字符 遍历
				next = append(next, p+string(c)) // 把 append(下一个, 节点 加 string(字符)) 写入 下一个
			}
		}
		combos = next // 把 下一个 写入 combos
	}
	return combos // 返回 combos
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   string   // in string
		want []string // want []string
	}{ // }{
		{"23", []string{"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}},
		{"", []string{}},
		{"2", []string{"a", "b", "c"}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if g := letterCombinations(c.in); !reflect.DeepEqual(g, c.want) {
			ok = false                                          // 把 false 写入 ok
			fmt.Printf("FAIL %q=%v want %v\n", c.in, g, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
