// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130442145
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"strings" // 「strings」
)

func isValid(s string) bool { // 定义判定函数 isValid
	for strings.Contains(s, "()") || strings.Contains(s, "{}") || strings.Contains(s, "[]") {
		s = strings.ReplaceAll(s, "()", "") // 把 strings.ReplaceAll(字符串, 「()」, 「()」) 写入 字符串
		s = strings.ReplaceAll(s, "{}", "") // 把 strings.ReplaceAll(字符串, 「{}」, 「{}」) 写入 字符串
		s = strings.ReplaceAll(s, "[]", "") // 把 strings.ReplaceAll(字符串, 「[]」, 「[]」) 写入 字符串
	}
	return s == "" // 返回 字符串 等于 「」
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   string // in string
		want bool   // want bool
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"()", true},
		{"()[]{}", true},
		{"(]", false},
		{"([)]", false},
		{"{[]}", true},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := isValid(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                     // 把 false 写入 ok
			fmt.Printf("FAIL isValid(%q)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
