// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355653
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func isPowerOfThree(n int) bool { // 定义判定函数 isPowerOfThree
	if n <= 0 { // 若 元素个数 不超过 0
		return false // 返回 false
	}
	for n%3 == 0 { // 把 赋值为 0 { 写入 for n%3
		n /= 3 // 把 3 写入 n /
	}
	return n == 1 // 返回 元素个数 等于 1
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true       // 把 true 写入 ok :
	tc := []struct { // 把 []struct { 写入 tc :
		in   int  // in int
		want bool // want bool
	}{ // }{
		{1, true}, {3, true}, {9, true}, {2, false}, {0, false}, {27, true},
	}
	for _, c := range tc { // 同时取 _ 与 字符 遍历
		if got := isPowerOfThree(c.in); got != c.want { // 若 got : 赋值为 isPowerOfThree(字符.in); got 不等于 字符.want
			ok = false                                                            // 把 false 写入 ok
			fmt.Printf("FAIL isPowerOfThree(%d)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
