// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852792
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func isSubsequence(s, t string) bool { // 定义判定函数 isSubsequence
	n, m := len(s), len(t) // 把 长度(字符串), 长度(另一字符串) 写入 n, m :
	i, j := 0, 0           // 把 0, 0 写入 i, j :
	for i < n && j < m {   // for 下标 i 小于 元素个数 且 下标 j 小于 映射表 {
		if s[i] == t[j] { // 若 字符串[下标 i] 等于 另一字符串[下标 j]
			i++ // 下标 i 加一
		}
		j++ // 下标 j 加一
	}
	return i == n // 返回 下标 i 等于 元素个数
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		s, t string // 字符串, 另一字符串 string
		want bool   // want bool
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"abc", "ahbgdc", true},
		{"axc", "ahbgdc", false},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := isSubsequence(c.s, c.t); got != c.want { // 若 got : 赋值为 isSubsequence(字符.字符串, 字符.另一字符串); got 不等于 字符.want
			ok = false                                                                  // 把 false 写入 ok
			fmt.Printf("FAIL isSubsequence(%q,%q)=%v want %v\n", c.s, c.t, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
