// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133564001
package main // 引入依赖

import (
	"fmt"
	"os"
	"sort"
	"strings"
) // 引入依赖

func frequencySort(s string) string { // 定义函数/方法 frequencySort
	cnt := map[rune]int{}  // 把 映射表[rune]int{} 写入 cnt :
	for _, ch := range s { // 同时取 _ 与 字符 遍历
		cnt[ch]++ // 计数[字符] 加一
	}
	type pair struct { // 定义类型
		ch rune // 字符 rune
		c  int  // 字符 int
	}
	var arr []pair           // var 数组 []pair
	for ch, c := range cnt { // 同时取 字符 与 字符 遍历
		arr = append(arr, pair{ch, c}) // 把 append(数组, pair{字符, 字符}) 写入 数组
	}
	sort.Slice(arr, func(i, j int) bool { return arr[i].c > arr[j].c })
	var b strings.Builder   // var b strings.Builder
	for _, p := range arr { // 同时取 _ 与 节点 遍历
		for k := 0; k < p.c; k++ { // 让 下标 k 从 0 开始计数
			b.WriteRune(p.ch) // b.WriteRune(节点.字符)
		}
	}
	return b.String() // 返回 b.String()
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   string // in string
		want string // want string
	}{ // }{
		{"aaabbbbccccc", "cccccbbbbaaa"},
		{"aab", "aab"},
		{"xzzzz", "zzzzx"},
		{"", ""},
		{"a", "a"},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := frequencySort(c.in); got != c.want { // 若 got : 赋值为 frequencySort(字符.in); got 不等于 字符.want
			ok = false                                                           // 把 false 写入 ok
			fmt.Printf("FAIL frequencySort(%q)=%q want %q\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
