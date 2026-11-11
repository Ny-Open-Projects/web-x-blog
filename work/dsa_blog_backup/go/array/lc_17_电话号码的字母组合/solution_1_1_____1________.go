// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130444168
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"strings" // 「strings」
)

func letterCombinations(digits string) []string { // 定义函数/方法 letterCombinations
	if len(digits) < 1 { // 若 长度(digits) 小于 1
		return []string{} // 返回 []string{}
	}
	dictMap := map[byte]string{'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
	var code []string                  // var code []string
	for i := 0; i < len(digits); i++ { // 让 下标 i 从 0 开始计数
		item := digits[i]               // 把 digits[下标 i] 写入 item :
		if _, ok := dictMap[item]; ok { // 若 _, ok : 赋值为 dictMap[item]; ok
			code = append(code, dictMap[item]) // 把 append(code, dictMap[item]) 写入 code
		}
	}
	var comb func(arr []string) []string // var comb func(数组 []string) []string
	comb = func(arr []string) []string { // 把 func(数组 []string) []string { 写入 comb
		if len(arr) == 1 { // 若 长度(数组) 等于 1
			return strings.Split(arr[0], "") // 返回 strings.Split(数组[0], 「」)
		}
		var tmp []string           // var 临时变量 []string
		for _, a := range arr[0] { // 同时取 _ 与 数组 遍历
			for _, b := range comb(arr[1:]) { // 同时取 _ 与 b 遍历
				tmp = append(tmp, string(a)+b) // 把 append(临时变量, string(数组) 加 b) 写入 临时变量
			}
		}
		return tmp // 返回 临时变量
	}
	if len(code) == 0 { // 若 长度(code) 等于 0
		return []string{} // 返回 []string{}
	}
	return comb(code) // 定义函数/方法 comb
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
