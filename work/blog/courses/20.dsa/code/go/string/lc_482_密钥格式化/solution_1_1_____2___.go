// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"strings" // 「strings」
)

func licenseKeyFormatting(s string, k int) string { // 定义函数/方法 licenseKeyFormatting
	s = strings.ReplaceAll(s, "-", "") // 把 strings.ReplaceAll(字符串, 「 减 」, 「 减 」) 写入 字符串
	s = strings.ToUpper(s)             // 把 strings.ToUpper(字符串) 写入 字符串
	var result []byte                  // var 结果 []byte
	for i := len(s) - 1; i >= 0; i-- { // 把 长度(字符串) 减 1; 下标 i 不低于 0; 下标 i 减一 { 写入 for i :
		result = append(result, s[i])          // 把 append(结果, 字符串[下标 i]) 写入 结果
		if (len(result)-1)%k == k-1 && i > 0 { // 若 长度(结果) 减 1) 对…取模 下标 k 等于 下标 k 减 1 且 下标 i 超过 0
			result = append(result, '-') // 把 append(结果, ' 减 ') 写入 结果
		}
	}
	for i, j := 0, len(result)-1; i < j; i, j = i+1, j-1 {
		result[i], result[j] = result[j], result[i] // 把 结果[下标 j], 结果[下标 i] 写入 result[i], result[j]
	}
	return string(result) // 定义函数/方法 string
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		s    string // 字符串 string
		k    int    // 下标 k int
		want string // want string
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"abc", 1, "A-B-C"},
		{"5F3Z-2e-9-w", 4, "5-F3Z-2E9W"},
		{"2-5g-3-J", 2, "2-5-G-3J"},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := licenseKeyFormatting(c.s, c.k); !reflect.DeepEqual(got, c.want) {
			ok = false                                                                         // 把 false 写入 ok
			fmt.Printf("FAIL licenseKeyFormatting(%q,%d)=%q want %q\n", c.s, c.k, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
