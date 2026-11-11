// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135037359
package main // 引入依赖

import (
	"fmt"
	"os"
	"strconv"
	"strings"
) // 引入依赖

func restoreIpAddresses(s string) []string { // 定义函数/方法 restoreIpAddresses
	res := []string{}                     // 把 []string{} 写入 res :
	var bt func(start int, path []string) // var bt func(起点 int, 当前路径 []string)
	bt = func(start int, path []string) { // 把 func(起点 int, 当前路径 []string) { 写入 bt
		if len(path) == 4 { // 若 长度(当前路径) 等于 4
			if start == len(s) { // 若 起点 等于 长度(字符串
				res = append(res, strings.Join(path, ".")) // 把 append(结果, strings.Join(当前路径, 「.」)) 写入 结果
			}
			return // return
		}
		for length := 1; length <= 3; length++ { // 让 长度 从 1 开始计数
			if start+length > len(s) { // 若 起点 加 长度 超过 长度(字符串
				break // 跳出循环
			}
			seg := s[start : start+length]     // 把 字符串[起点 : 起点 加 长度] 写入 seg :
			if len(seg) > 1 && seg[0] == '0' { // 若 长度(seg) 超过 1 且 seg[0] 等于 '0'
				continue // 跳过本轮，进入下一次
			}
			if v, _ := strconv.Atoi(seg); v > 255 { // 若 值, _ : 赋值为 strconv.Atoi(seg); 值 超过 255
				continue // 跳过本轮，进入下一次
			}
			bt(start+length, append(path, seg)) // bt(起点 加 长度, append(当前路径, seg))
		}
	}
	bt(0, []string{}) // bt(0, []string{})
	return res        // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   string   // in string
		want []string // want []string
	}{ // }{
		{"25525511135", []string{"255.255.11.135", "255.255.111.35"}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if g := restoreIpAddresses(c.in); fmt.Sprint(g) != fmt.Sprint(c.want) {
			ok = false                                          // 把 false 写入 ok
			fmt.Printf("FAIL %q=%v want %v\n", c.in, g, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
