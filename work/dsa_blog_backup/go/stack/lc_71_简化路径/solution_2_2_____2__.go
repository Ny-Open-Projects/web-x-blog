// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145112805
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"strings" // 「strings」
)

func simplifyPath(path string) string { // 定义函数/方法 simplifyPath
	names := strings.Split(path, "/") // 把 strings.Split(当前路径, 「 除以 」) 写入 names :
	stack := []string{}               // 把 []string{} 写入 stack :
	for _, name := range names {      // 同时取 _ 与 name 遍历
		if name == ".." { // 若 name 等于 「..」
			if len(stack) > 0 { // 若 长度(栈) 超过 0
				stack = stack[:len(stack)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
			}
		} else if name != "" && name != "." { // 否则，若 name 不等于 「」 且 name 不等于 「」
			stack = append(stack, name) // 把 append(栈, name) 写入 栈
		}
	}
	return "/" + strings.Join(stack, "/") // 返回 「 除以 」 加 strings.Join(栈, 「 除以 」)
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   string // in string
		want string // want string
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"/home/", "/home"},
		{"/a/./b/../../c/", "/c"},
		{"/../", "/"},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := simplifyPath(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                          // 把 false 写入 ok
			fmt.Printf("FAIL simplifyPath(%q)=%q want %q\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
