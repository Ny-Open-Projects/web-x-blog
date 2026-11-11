// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func reverseStr(s string, k int) string { // 定义函数/方法 reverseStr
	n := len(s)                     // 把 长度(字符串) 写入 n :
	arr := make([]byte, n)          // 把 make([]byte, 元素个数) 写入 arr :
	copy(arr, s)                    // copy(数组, 字符串)
	for i := 0; i < n; i += 2 * k { // 让 下标 i 从 0 开始计数
		left := i          // 把 下标 i 写入 left :
		right := i + k - 1 // 把 下标 i 加 下标 k 减 1 写入 right :
		if right >= n {    // 若 右边界 不低于 元素个数
			right = n - 1 // 把 元素个数 减 1 写入 右边界
		}
		for left < right { // for 左边界 小于 右边界 {
			arr[left], arr[right] = arr[right], arr[left] // 把 数组[右边界], 数组[左边界] 写入 arr[left], arr[right]
			left++                                        // 左边界 加一
			right--                                       // 右边界 减一
		}
	}
	return string(arr) // 定义函数/方法 string
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		s    string // 字符串 string
		k    int    // 下标 k int
		want string // want string
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"abc", 1, "abc"},
		{"abcdefg", 2, "bacdfeg"},
		{"abcd", 2, "bacd"},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := reverseStr(c.s, c.k); got != c.want { // 若 got : 赋值为 reverseStr(字符.字符串, 字符.下标 k); got 不等于 字符.want
			ok = false                                                               // 把 false 写入 ok
			fmt.Printf("FAIL reverseStr(%q,%v)=%q want %q\n", c.s, c.k, got, c.want) // 打印输出
		}
	}
	_ = reflect.DeepEqual // 把 reflect.DeepEqual 写入 _
	if !ok {              // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
