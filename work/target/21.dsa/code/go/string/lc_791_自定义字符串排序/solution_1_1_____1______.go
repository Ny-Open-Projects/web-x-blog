// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func customSortString(order, s string) string { // 定义函数/方法 customSortString
	count := map[rune]int{} // 把 映射表[rune]int{} 写入 count :
	for _, c := range s {   // 同时取 _ 与 字符 遍历
		count[c]++ // 计数[字符] 加一
	}
	var result []rune         // var 结果 []rune
	for _, c := range order { // 同时取 _ 与 字符 遍历
		if n, ok := count[c]; ok { // 若 元素个数, ok : 赋值为 计数[字符]; ok
			for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
				result = append(result, c) // 把 append(结果, 字符) 写入 结果
			}
			delete(count, c) // delete(计数, 字符)
		}
	}
	for c, n := range count { // 同时取 字符 与 元素个数 遍历
		for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
			result = append(result, c) // 把 append(结果, 字符) 写入 结果
		}
	}
	return string(result) // 定义函数/方法 string
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		order, s, want string // order, 字符串, want string
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"cba", "abcd", "cbad"},
		{"cbafg", "abcd", "cbad"},
		{"kqep", "pekeq", "kqeep"},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := customSortString(c.order, c.s); !reflect.DeepEqual(got, c.want) {
			ok = false                                                                         // 把 false 写入 ok
			fmt.Printf("FAIL customSortString(%q,%q)=%q want %q\n", c.order, c.s, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
