// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145112805
package main // 引入依赖

import (
	"fmt"
	"os"
	"strings"
) // 引入依赖

func simplifyPath(path string) string { // 定义函数/方法 simplifyPath
	stk := []string{}                            // 把 []string{} 写入 stk :
	for _, s := range strings.Split(path, "/") { // 同时取 _ 与 字符串 遍历
		if s == "" || s == "." { // 若 字符串 等于 「」 或 字符串 等于 「」
			continue // 跳过本轮，进入下一次
		}
		if s != ".." { // 若 字符串 不等于 「..」
			stk = append(stk, s) // 把 append(栈, 字符串) 写入 栈
		} else if len(stk) > 0 { // 否则，若 长度(栈) 超过 0
			stk = stk[:len(stk)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
		}
	}
	return "/" + strings.Join(stk, "/") // 返回 「 除以 」 加 strings.Join(栈, 「 除以 」)
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   string // in string
		want string // want string
	}{ // }{
		{"/home/", "/home"},
		{"/a/./b/../../c/", "/c"},
		{"/../", "/"},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if g := simplifyPath(c.in); g != c.want { // 若 g : 赋值为 simplifyPath(字符.in); g 不等于 字符.want
			ok = false                                          // 把 false 写入 ok
			fmt.Printf("FAIL %q=%v want %v\n", c.in, g, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
