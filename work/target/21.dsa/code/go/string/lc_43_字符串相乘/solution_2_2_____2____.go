// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381943
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func multiply(num1, num2 string) string { // 定义函数/方法 multiply
	if num1 == "0" || num2 == "0" { // 若 num1 等于 「0」 或 num2 等于 「0」
		return "0" // 返回 「0」
	}
	m, n := len(num1), len(num2)  // 把 长度(num1), 长度(num2) 写入 m, n :
	result := make([]int, m+n)    // 把 make([]int, 映射表 加 元素个数) 写入 result :
	for i := m - 1; i >= 0; i-- { // 把 映射表 减 1; 下标 i 不低于 0; 下标 i 减一 { 写入 for i :
		for j := n - 1; j >= 0; j-- { // 把 元素个数 减 1; 下标 j 不低于 0; 下标 j 减一 { 写入 for j :
			mul := int(num1[i]-'0') * int(num2[j]-'0') // 把 int(num1[下标 i] 减 '0') 乘 int(num2[下标 j] 减 '0') 写入 mul :
			p1, p2 := i+j, i+j+1                       // 把 下标 i 加 下标 j, 下标 i 加 下标 j 加 1 写入 p1, p2 :
			total := mul + result[p2]                  // 把 mul 加 结果[p2] 写入 total :
			result[p2] = total % 10                    // 把 总和 对…取模 10 写入 result[p2]
			result[p1] += total / 10                   // result[p1]累加 总和 除以 10
		}
	}
	out := ""                  // 把 「」 写入 out :
	for _, d := range result { // 同时取 _ 与 d 遍历
		if !(out == "" && d == 0) { // 若 取反 (out 等于 「」 且 d 等于 0
			out += string('0' + byte(d)) // out累加 string('0' 加 byte(d))
		}
	}
	if out == "" { // 若 out 等于 「」
		out = "0" // 把 「0」 写入 out
	}
	return out // 返回 out
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		a, b string // 数组, b string
		want string // want string
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"2", "3", "6"},
		{"123", "456", "56088"},
		{"0", "123", "0"},
		{"999", "999", "998001"},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := multiply(c.a, c.b); !reflect.DeepEqual(got, c.want) {
			ok = false                                                             // 把 false 写入 ok
			fmt.Printf("FAIL multiply(%q,%q)=%q want %q\n", c.a, c.b, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
