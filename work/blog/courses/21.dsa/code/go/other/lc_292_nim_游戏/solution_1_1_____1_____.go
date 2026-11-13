// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355568
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func canWinNim(n int) bool { // 定义函数/方法 canWinNim
	return n%4 != 0 // 返回 元素个数 对…取模 4 不等于 0
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true       // 把 true 写入 ok :
	tc := []struct { // 把 []struct { 写入 tc :
		in   int  // in int
		want bool // want bool
	}{ // }{
		{1, true}, {4, false}, {7, true}, {8, false},
	}
	for _, c := range tc { // 同时取 _ 与 字符 遍历
		if got := canWinNim(c.in); got != c.want { // 若 got : 赋值为 canWinNim(字符.in); got 不等于 字符.want
			ok = false                                                       // 把 false 写入 ok
			fmt.Printf("FAIL canWinNim(%d)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
