// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130444168
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func letterCombinations(digits string) []string { // 定义函数/方法 letterCombinations
	mapping := map[byte]string{'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
	var res []string                           // var 结果 []string
	var backtrack func(path []byte, index int) // var backtrack func(当前路径 []byte, index int)
	backtrack = func(path []byte, index int) { // 把 func(当前路径 []byte, index int) { 写入 backtrack
		if index == len(digits) { // 若 index 等于 长度(digits
			res = append(res, string(path)) // 把 append(结果, string(当前路径)) 写入 结果
			return                          // return
		}
		for _, ch := range mapping[digits[index]] { // 同时取 _ 与 字符 遍历
			backtrack(append(path, byte(ch)), index+1) // backtrack(append(当前路径, byte(字符)), index 加 1)
		}
	}
	if len(digits) > 0 { // 若 长度(digits) 超过 0
		backtrack([]byte{}, 0) // backtrack([]byte{}, 0)
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   string   // in string
		want []string // want []string
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"23", []string{"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}},
		{"2", []string{"a", "b", "c"}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := letterCombinations(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                                // 把 false 写入 ok
			fmt.Printf("FAIL letterCombinations(%q)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
