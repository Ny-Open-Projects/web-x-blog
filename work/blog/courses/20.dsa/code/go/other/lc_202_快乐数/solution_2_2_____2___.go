// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355335
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func getNum(n int) bool { // 定义函数/方法 getNum
	seen := make(map[int]bool) // 把 make(映射表[int]bool) 写入 seen :
	for n != 1 {               // 把 1 { 写入 for n !
		if seen[n] { // 若 已见集合[元素个数]
			return false // 返回 false
		}
		seen[n] = true // 把 true 写入 seen[n]
		s := 0         // 把 0 写入 s :
		t := n         // 把 元素个数 写入 t :
		for t > 0 {    // for 另一字符串 超过 0 {
			d := t % 10 // 把 另一字符串 对…取模 10 写入 d :
			s += d * d  // 字符串累加 d 乘 d
			t /= 10     // 把 10 写入 t /
		}
		n = s // 把 字符串 写入 元素个数
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true       // 把 true 写入 ok :
	tc := []struct { // 把 []struct { 写入 tc :
		in   int  // in int
		want bool // want bool
	}{ // }{
		{1, true}, {19, true}, {2, false}, {7, true},
	}
	for _, c := range tc { // 同时取 _ 与 字符 遍历
		if got := getNum(c.in); got != c.want { // 若 got : 赋值为 getNum(字符.in); got 不等于 字符.want
			ok = false                                                    // 把 false 写入 ok
			fmt.Printf("FAIL getNum(%d)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
