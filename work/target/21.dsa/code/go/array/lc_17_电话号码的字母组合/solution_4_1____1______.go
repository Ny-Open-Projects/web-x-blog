// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130444168
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func letterCombinations(digits string) []string { // 定义函数/方法 letterCombinations
	if len(digits) < 1 { // 若 长度(digits) 小于 1
		return []string{} // 返回 []string{}
	}
	d := map[byte]string{'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
	res := []string{""}                // 把 []string{「」} 写入 res :
	for i := 0; i < len(digits); i++ { // 让 下标 i 从 0 开始计数
		ch := digits[i]          // 把 digits[下标 i] 写入 ch :
		if _, ok := d[ch]; !ok { // 若 _, ok : 赋值为 d[字符]; 取反 ok
			continue // 跳过本轮，进入下一次
		}
		var nres []string       // var nres []string
		for _, p := range res { // 同时取 _ 与 节点 遍历
			for _, c := range d[ch] { // 同时取 _ 与 字符 遍历
				nres = append(nres, p+string(c)) // 把 append(nres, 节点 加 string(字符)) 写入 nres
			}
		}
		res = nres // 把 nres 写入 结果
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
