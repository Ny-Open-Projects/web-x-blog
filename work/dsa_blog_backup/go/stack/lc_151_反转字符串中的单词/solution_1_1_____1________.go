// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113405
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"strings" // 「strings」
)

func reverseWords(s string) string { // 定义函数/方法 reverseWords
	fields := strings.Fields(s) // 把 strings.Fields(字符串) 写入 fields :
	for i, j := 0, len(fields)-1; i < j; i, j = i+1, j-1 {
		fields[i], fields[j] = fields[j], fields[i] // 把 fields[下标 j], fields[下标 i] 写入 fields[i], fields[j]
	}
	return strings.Join(fields, " ") // 返回 strings.Join(fields, 「 」)
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   string // in string
		want string // want string
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"abc", "abc"},
		{"the sky is blue", "blue is sky the"},
		{"  hello world  ", "world hello"},
		{"a", "a"},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := reverseWords(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                          // 把 false 写入 ok
			fmt.Printf("FAIL reverseWords(%q)=%q want %q\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
